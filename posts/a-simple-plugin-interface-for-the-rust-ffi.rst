.. title: A simple plugin interface for the Rust FFI
.. slug: a-simple-plugin-interface-for-the-rust-ffi
.. date: 2019-06-16 09:33:33 UTC+02:00
.. tags: rust, c
.. category: 
.. link: 
.. description: I present a straight-forward design of a plugin interface using the Rust FFI
.. type: text

In a recent post I explored `how to pass complex datatypes through the Rust FFI`_. (The FFI is the
foreign function interface, a part of the Rust language for calling code written in other
languages.)

I am exploring the Rust FFI because I want to use it in `a small web application`_ that I am
writing and that will be used to interact with hardware peripherals connected to a system on a chip
(SoC). One use-case that I have in mind is to monitor readings from moisture and temperature
sensors implanted in the soil of my houseplants. In many cases the general purpose input/output
(GPIO) pins of a SoC are controlled through a C library such as `WiringPi`_ for the Raspberry Pi,
which means my monitoring system needs to interface with C libraries such as this one.

In this post I will describe my current understanding for how best to integrate C-language plugins
with a Rust application. I have omitted all application-specific logic from the example and will
instead focus on the design of the plugin interface itself.

You may find `the source code for this post here`_. I was heavily inspired by both the `Rust FFI
Omnibus`_ and `The (unofficial) Rust FFI Guide`_. This post was written using version 1.35.0 of the
Rust compiler.

The C plugin
============

I wrote a very simple of C library that is located in the `ffi-test`_ folder of the example
repository and that will serve the purpose of this demonstration. It consists of two source files
(``ffi-test.c`` and ``ffi-test.h``) and a ``Makefile``. The plugin's interface is defined as usual
in the header file:

.. code-block:: c
   :linenos:

   #ifndef FFI_TEST_H
   #define FFI_TEST_H

   #include <stdlib.h>

   struct object;

   struct object* init(void);
   void free_object(struct object*);
   int get_api_version(void);
   int get_info(const struct object*);
   void set_info(struct object*, int);
   size_t sizeof_obj(void);

   #endif /* FFI_TEST_H */

In particular, there is an opaque struct that is declared by the line :code:`struct object;`. (An
opaque struct is a struct whose definition is hidden from the public API; the definition is
provided in the file ``ffi-test.c``.) This object will hold the data for our plugin, but, because
it is opaque, we will only be able to interact with it through functions such as ``init``,
``free_object``, etc. that are provided by the API.

To build the C library on UNIX-like systems, simply execute the ``make`` command from within the
``ffi-test`` library.

.. code-block:: console

   $ make
   gcc -c -o libffi-test.o -fpic ffi-test.c -Wall -Werror
   gcc -shared -o libffi-test.so libffi-test.o

The Rust-C plugin interface
===========================

The Rust code is contained in one source file, `src/main.rs`_. The design pattern contained within
consists of three kinds of objects:

- type definitions for the functions in the C library
- a ``VTable`` struct that holds the external function types
- a ``Plugin`` struct that holds the plugin's library, the ``VTable``, and a raw pointer to the
  object provided by the C library

Let's take a look at each of these abstractions.

External function types
-----------------------

The external function types are defined as follows:

.. code-block:: rust

   #[repr(C)]
   struct Object {
       _private: [u8; 0],
   }
   type FreeObject = extern "C" fn(*mut Object);
   type Init = extern "C" fn() -> *mut Object;
   type GetApiVersion = extern "C" fn() -> c_int;
   type GetInfo = extern "C" fn(*const Object) -> c_int;
   type SetInfo = extern "C" fn(*mut Object, c_int);

The opaque struct from the C library is represented as rust ``struct`` with a single, private field
containing an empty array. `This is currently the recommended way`_ to represent opaque structs in
the Rust FFI. Following the ``struct`` definition are the type definitions for the foreign
functions.

.. code-block:: rust

   type FreeObject = extern "C" fn(*mut Object);
   type Init = extern "C" fn() -> *mut Object;
   // ...

For example, the ``Init`` type represents a foreign C function that takes no arguments and returns
a mutable raw pointer to an ``Object`` instance. This function type therefore represents the
``Object`` constructor in Rust.

The VTable
----------

The ``VTable`` serves as a way to collect the types associated with the C library functions into
one place. Furthermore, I added a version number to make it ``VTableV0``. The purpose in doing this
is to easily maintain backwards compatability with and follow changes to the C API.

By looking at its definition, you can see that it contains a few ``RawSymbol`` instances:

.. code-block:: rust

   struct VTableV0 {
       free_object: RawSymbol<FreeObject>,
       get_info: RawSymbol<GetInfo>,
       set_info: RawSymbol<SetInfo>,
   }

A ``RawSymbol`` is a name that I gave to Unix-specific symbols from the ``libloading`` Rust
library. (See the ``use`` statements at the top of the source code file.) I am not storing plain
``Symbols`` from that library inside the VTable because the lifetime constraints associated with
plain ``Symbols`` and their corresponding ``Library`` do not allow me to take ownership of them
inside the struct. (You can find a few attempts in the commit history of this repository where I
tried to own plain ``Symbols``; none of these attempts would compile.)

Instead, if I had used a plain ``Symbol``, then I would have had to lookup the symbols inside the C
library each time that I wanted to call them.

The way to obtain ``RawSymbols`` is to use the ``into_raw`` method of a plain ``Symbol``. You can
find an example of this inside the ``VTable``'s constructor:

.. code-block:: rust

    unsafe fn new(library: &Library) -> VTableV0 {
        println!("Loading API version 0...");
        let free_object: Symbol<FreeObject> = library.get(b"free_object\0").unwrap();
        let free_object = free_object.into_raw();
	// ...

First, the ``free_object`` ``Symbol`` is imported from the library using the ``get()`` method from
the library, then it is converted to a ``RawSymbol`` in the following line so that it can be stored
inside the ``VTableV0`` struct that is returned by the constructor. The whole function is marked as
``unsafe`` because of the multiple calls to the ``get`` method.

The Plugin
----------

Finally we reach the top of the hierarchy of the components that comprise this design, the
``Plugin`` struct. Its implementation follows:

.. code-block:: rust

   struct Plugin {
       #[allow(dead_code)]
       library: Library,
       object: *mut Object,
       vtable: VTableV0,
   }

   impl Plugin {
       unsafe fn new(library_name: &OsStr) -> Plugin {
       let library = Library::new(library_name).unwrap();
           let get_api_version: Symbol<GetApiVersion> = library.get(b"get_api_version\0").unwrap();
           let vtable = match get_api_version() {
               0 => VTableV0::new(&library),
               _ => panic!("Unrecognized C API version number."),
           };

           let init: Symbol<Init> = library.get(b"init\0").unwrap();
           let object: *mut Object = init();

           Plugin {
               library: library,
               object: object,
               vtable: vtable,
           }
       }
   }

   impl Drop for Plugin {
       fn drop(&mut self) {
           (self.vtable.free_object)(self.object);
       }
   }

The interesting parts here are the ``Plugin``'s constructor ``new`` and the implementation of the
``Drop`` trait. After loading the library, the constructor calls the C library function that
returns its API version; if the version matches one for which we have a ``VTable``, then we create
the new ``VTable``. Next, we instantiate an ``Object`` by calling its constructor to obtain a raw
pointer to it.

.. code-block:: rust

           let init: Symbol<Init> = library.get(b"init\0").unwrap();
           let object: *mut Object = init();

The constructor packs the library, the ``VTable``, and the object pointer into a new ``Plugin``
struct and returns it.

The ``Drop`` trait implementation is used to automatically free the memory that has been allocated
when the pointer held by the ``Plugin`` struct goes out-of-scope. It does this by calling the
``free_object`` method in the VTable.

.. code-block:: rust

   impl Drop for Plugin {
       fn drop(&mut self) {
           (self.vtable.free_object)(self.object);
       }
   }

Running the example
-------------------

To run the example, run the following commands from the root directory of the example repository.

.. code-block:: console

   $ cargo build
   Compiling rust-libloading v0.1.0 (/home/kmdouglass/src/rust-libloading-example)
    Finished dev [unoptimized + debuginfo] target(s) in 0.27s
   $ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/rust-libloading`
   Loading API version 0...
   Original value: 0
   New value: 42

The ``main`` method of the Rust code creates the plugin, prints the default value of the data held
by the object (which is instantiated by the C library), and then mutates the data to the value
``42``.

It then prints this value, demonstrating that the FFI calls work.
   
Discussion
==========

The most difficult part of developing this design was finding a way to own the symbols exposed by
the plugin library. For me, it was not completely evident from the `libloading documentation`_ that
this was the purpose of the ``into_raw`` method on a ``Symbol``.

What I like about this design is that the whole plugin interface fits nicely within a simple
hierarchy with a collection of foreign method types at its base. It also supports changes to the C
API because a new ``VTable`` can be created each time the API changes.

One current disadvantage of the design is that ``free_object`` is exposed through the VTable. I
think that this opens the possibility for a double-free error. One way to prevent this is to hide
the ``free_object`` method, loading its corresponding symbol only when the ``drop`` method is
called.

Another disadvantage of this design is that it relies on the particular C API exposed by the
library. C programmers have a large amount of freedom in designing APIs for their libraries. They
are not forced to use opaque structs or to version their APIs. As a result, I don't believe that
the plugin design presented here can be completely generalized to any C library.

The ``Plugin`` struct is almost certainly not thread safe. To make it thread safe, it may be
necessary to wrap the raw pointer in a ``Mutex``. It may even be simpler to wrap the entire struct
in a ``Mutex``.

Finally, owning raw symbols is not platform independent. You can see at the top of the Rust source
code that I am importing the ``Symbol`` object specific to UNIX systems. One would need to change
this if it was intended to work on Windows.

Summary
=======

- I presented a design pattern for managing C-language plugins in Rust.
- The design pattern consists of a collection of foreign object function types, the
  ``VTable``. This collection is part of a larger collection which owns pointers to the opaque data
  types exposed by the library, as well as the plugin library itself.
- The trick to owning symbols (instead of looking them up in the library each time you want to use
  them), is use ``into_raw`` method that is implemented on libloading's ``Symbol``.
- This design cannot be completely generalized to any C library, but should provide a good starting
  point to work with FFI plugins in Rust.

.. _`how to pass complex datatypes through the Rust FFI`: http://kmdouglass.github.io/posts/complex-data-types-and-the-rust-ffi/
.. _`a small web application`: https://github.com/kmdouglass/kpal
.. _`WiringPi`: http://wiringpi.com
.. _`Rust FFI Omnibus`: http://jakegoulding.com/rust-ffi-omnibus/
.. _`The (unofficial) Rust FFI Guide`: https://michael-f-bryan.github.io/rust-ffi-guide/
.. _`the source code for this post here`: https://github.com/kmdouglass/rust-libloading-example
.. _`ffi-test`: https://github.com/kmdouglass/rust-libloading-example/tree/master/ffi-test
.. _`src/main.rs`: https://github.com/kmdouglass/rust-libloading-example/blob/master/src/main.rs
.. _`This is currently the recommended way`: https://doc.rust-lang.org/nomicon/ffi.html#representing-opaque-structs
.. _`libloading documentation`: https://docs.rs/libloading/0.5.1/libloading/
