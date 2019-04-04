.. title: Complex data types and the Rust FFI
.. slug: complex-data-types-and-the-rust-ffi
.. date: 2019-04-04 19:51:55 UTC+02:00
.. tags: rust, c
.. category: 
.. link: 
.. description: Exploring the Rust FFI to pass complex data between Rust and C
.. type: text

The `Rust Foreign Function Interface`_ (FFI, for short) is a feature of Rust that enables the
sharing of data and functions between parts of code that have been written in different
languages. I am interested in the FFI because many libraries used in embedded systems are written
in C, and I would like to leverage them for my embedded work with Rust.

I quickly learned from my initial experiments with the Rust FFI that one of its challenges is
casting data types into a form that may be consumed by other languages. This challenge is not
unique to the Rust FFI, and there are numerous reasons for it. For one, different languages use
different mechanisms to layout data in the computer's memory. What's more, names for functions and
data types are often mangled, which means that the symbol in a library that maps to a function may
be different than the name that you give to the function in your code. As far as I know, C
compilers do not mangle symbol names, and partly for this reason the C language is often used as an
intermediary language in FFIs. Converting Rust to C is therefore an important skill when using Rust
for multi-language work.

There are a few good resources on the internet about using the Rust FFI to expose functions written
in Rust to other languages. However, I found little information about passing data types between
languages. To help remedy this situation, I describe in this post a simple Rust library that I
wrote to explore how to pass complex data types from Rust to C.

An example FFI project
======================

I created the Rust library in the typical way by first starting a new project with Cargo:

.. code-block:: shell

   $ cargo new --lib rstruct
   $ cd rstruct

Inside, I modified the contents of ``Cargo.toml`` to the following:

.. code-block::

   [package]
   name = "rstruct"
   version = "0.1.0"
   authors = ["Kyle M. Douglass"]
   edition = "2018"

   [lib]
   crate-type = ["cdylib"]

   [dependencies]

The only lines that I added were ``[lib]`` and ``crate-type = ["cdylib"]``. As described in the
`2018 edition guide`_, this type of crate produces a binary that has no Rust-specific information
in it and is intended for use through a C FFI.

Next, I opened the ``src/lib.rs`` source file, removed the auto-generated content, and added the
following source.

.. code-block:: rust
   :linenos:

   use std::boxed::Box;
   use std::ffi::CString;
   use std::os::raw::c_char;

   #[repr(C)]
   pub struct RStruct {
       name: *const c_char,
       value: Value,
   }

   #[repr(C)]
   pub enum Value {
       _Int(i32),
       _Float(f64),
   }

   #[no_mangle]
   pub extern "C" fn data_new() -> *mut RStruct {
       println!("{}", "Inside data_new().".to_string());

       Box::into_raw(Box::new(RStruct {
           name: CString::new("my_rstruct")
               .expect("Error: CString::new()")
               .into_raw(),
           value: Value::_Int(42),
       }))
   }

   #[no_mangle]
   pub extern "C" fn data_free(ptr: *mut RStruct) {
       if ptr.is_null() {
           return;
       }
       unsafe {
           Box::from_raw(ptr);
       }
   }

Roughly speaking, this simple library does two things. First, it defines two data types, a struct
called ``RStruct`` and a Rust enum (not to be confused with a C enum!) called ``Value``. Second, it
exposes two functions that may be used to access instances of these data types from C:
``data_new()`` and ``data_free()``.

Let's take closer look now at what the code is doing.

Defining structs and enums for use in C
=======================================

I want to expose instances of the RStruct type to C code. The definition of ``RStruct`` is

.. code-block:: rust

   #[repr(C)]
   pub struct RStruct {
       name: *const c_char,
       value: Value,
   }

The first line here is ``[repr(C)]``. This is an attribute that modifies the layout of the struct
in memory to "do what C does." As described in the `Rustonomicon`_,

   The order, size, and alignment of fields is exactly what you would expect from C or C++. Any
   type you expect to pass through an FFI boundary should have repr(C), as C is the lingua-franca
   of the programming world.

Next, we define a public struct just as we would if we were writing typical Rust code. In this
example, the struct has two fields. The first is a field called ``name``, which has a type ``*const
c_char``. The Rust data types ``String`` and ``&str`` cannot be interpreted in C, so instead we
define the data type as a `raw pointer`_ to a ``c_char``. (In this case, ``*`` is not dereferencing
the pointer but is `part of the type name`_ ``*const T``.)

The second field is an enum whose definition follows:

.. code-block:: rust

   #[repr(C)]
   pub enum Value {
       _Int(i32),
       _Float(f64),
   }

Again we use ``#[repr(C)]`` to indicate that we want the enum to be laid out in memory in the same
manner as in C. The enum ``Value`` has two variants, ``_Int`` and ``_Float``, that each contain a
value of ``i32`` and ``f64``, respectively. If you're familiar with C, then you may have already
noticed that C enums are differnt from Rust enums in that they do not hold any data themselves. How
this minor annoyance is solved will be seen later when we generate the C header for this library.

The data types i32 and f64 are easily translated into C's equivalent numeric data types, so there
is no need to do anything special with them.

Instantiating and freeing Memory
--------------------------------

Following the data type definitions, there are two functions that are exposed through the FFI
boundary, one for instantiating an ``RStruct`` and one for freeing the memory associated with an
``RStruct``. The method for instantiation is first:

.. code-block:: rust

   #[no_mangle]
   pub extern "C" fn data_new() -> *mut RStruct {
       println!("{}", "Inside data_new().".to_string());

       Box::into_raw(Box::new(RStruct {
           name: CString::new("my_rstruct")
               .expect("Error: CString::new()")
               .into_raw(),
           value: Value::_Int(42),
       }))
   }

The first line contains an attribute called ``#[no_mangle]``. As defined in `the Book`_:

   Mangling is when a compiler changes the name we’ve given a function to a different name that
   contains more information for other parts of the compilation process to consume but is less
   human readable.


Placing the ``#[no_mangle]`` attribute before the function definition ensures that the function
name matches that of the corresponding symbol in the library.

Next is the function definition ``pub extern "C" fn data_new() -> *mut RStruct``. Let's break this
down into parts to understand it better:

- ``pub`` : The function will be callable from outside the library
- ``extern "C"`` : This line serves two different purposes in Rust, both related to FFI. In my
  case, I use it specify that the function should be exposed with the `application binary interface
  from C`_.
- ``fn data_new()`` : This is just the usual ``fn`` keyword and the name of the function
- ``-> *mut RStruct`` : Here I specify that the function will return a mutable, raw pointer to an
  ``RStruct instance``.

The purpose of this function is to create a ``RStruct`` instance and return a pointer to it. The
``RStruct`` is created just as we would any other struct in Rust, with the exception of the
``name`` field:

.. code-block:: rust

   RStruct {
       name: CString::new("my_rstruct")
           .expect("Error: CString::new()")
           .into_raw(),
       value: Value::_Int(42),
   }

The ``CString`` is first created with the ``new()`` constructor and contains the value
``"my_rstruct"``. After unpacking the result with ``expect()``, I call the ``into_raw()`` method to
create a raw pointer to the C string whose `ownership will be passed off to the calling C
code`_. (If I had used ``as_ptr()`` instead, the pointer would have been dropped immediately after
the function call because the ``CString`` `would have been deallocated`_.) The ``value`` field is
instantiated as it would be in normal Rust.

What is perhaps new in this method is the ``Box`` type that wraps the ``RStruct`` instance.

.. code-block:: rust

   Box::into_raw(Box::new( ... ))

A ``Box`` is one of Rust's smart pointers that is used to `allocate memory for a data type on the
heap`_. When ``Box::new()`` is called it creates a pointer to the newly created ``RStruct``
instance. Normally, this pointer would be dropped and the memory automatically deallocated when the
``data_new()`` function returns. However, the ``Box::into_raw()`` function serves the same purpose
here as the corresponding function for ``CString``: it hands off ownership of the pointer to the
calling code so that the memory is not deallocated.

There is a rule-of-thumb that memory allocated by Rust should be freed by Rust. For this reason, we
provide the ``data_free()`` method that C code may use to deallocate the memory that is allocated
by ``data_new()``.

.. code-block:: rust

   #[no_mangle]
   pub extern "C" fn data_free(ptr: *mut RStruct) {
       if ptr.is_null() {
           return;
       }
       unsafe {
           Box::from_raw(ptr);
       }
   }   

This function accepts a mutable pointer to an RStruct. First, it checks whether the pointer is null
and if it is, the function returns without doing anything. Assuming that the pointer is not null,
the ``Box`` is reconstructed from it inside an ``unsafe`` block because ``from_raw()`` `is
unsafe`_. Importantly, this new Box pointer will go out of scope at the end of the function so that
it will automatically be dropped when the function returns.

Building the library is simple. I run ``cargo build --release`` to build a release version. The
library itself will be found at ``target/release/librstruct.so``. On Linux, one can verify that it
contains the ``data_new()`` and ``data_free()`` methods by displaying its symbols with the ``nm
-g`` command:


.. code-block:: console

   $ nm -g target/release/librstruct.so
   # snip
   00000000000046c0 T data_free
   00000000000044e0 T data_new
   # snip

Generating the header for the library
-------------------------------------

Now that I have a shared library, I want to access the functions that it exposes from C. To do
this, I first need a header file that I can use to import the library's declarations into the C
code. Moreover, generating the header can help in understanding how Rust translates its data types
to C.

I will use `cbindgen`_ to automatically generate the header. ``cbindgen`` is installed with the
command

.. code-block:: console

   $ cargo install cbindgen

``cbindgen`` is highly configurable, but for the project described here I only need its most basic
functionality. Assuming that I am in the root directory of my Rust project, I generate the header
``rstruct.h`` with the following

.. code-block:: console

   $ cbindgen --lang C -o rstruct.h .

After running ``cbindgen`` there is a new file called ``rstruct.h`` in the project folder. Here are
its contents:

.. code-block:: c
   :linenos:

   #include <stdarg.h>
   #include <stdbool.h>
   #include <stdint.h>
   #include <stdlib.h>

   typedef enum {
     _Int,
     _Float,
   } Value_Tag;

   typedef struct {
     int32_t _0;
   } _Int_Body;

   typedef struct {
     double _0;
   } _Float_Body;

   typedef struct {
     Value_Tag tag;
     union {
       _Int_Body _int;
       _Float_Body _float;
     };
   } Value;

   typedef struct {
     const char *name;
     Value value;
   } RStruct;

   void data_free(RStruct *ptr);

   RStruct *data_new(void);

First, you can see the ``enum`` that contains the variations of the ``Value`` data type that is
stored in the ``RStruct`` and that was defined in Rust. The name of this new type is ``Value_Tag``,
and it is used to define the current type of a value.

.. code-block:: c

   typedef struct {
     Value_Tag tag;
     union {
       _Int_Body _int;
       _Float_Body _float;
     };
   } Value;

A ``Value`` is just another struct that contains a ``Value_Tag`` field to identify which variant of
the ``enum`` it is holding and a ``union`` field that holds the actual value.

The important thing to understand here is that ``cbindgen`` effectively uses nested C data types to
represent complex Rust data structures. In particular, Rust ``enums`` are a combination of C
``structs``, ``enums``, and ``unions``.

Calling the library from C
==========================

With everything in place, it's now time to write the C program. My example C program looks like the
following:

.. code-block:: c
   :linenos:

   #include <dlfcn.h>
   #include <stdio.h>
   #include <stdlib.h>

   #include "rstruct.h"

   int main() {
     void* handle;
     RStruct* (*data_new)(void);
     void (*data_free)(RStruct*);
     char* error;
  
     printf("Loading librstruct.so...\n");
     handle = dlopen(
       "librstruct.so",
       RTLD_LAZY
     );
     if (!handle) {
       fprintf(stderr, "%s\n", dlerror());
       exit(EXIT_FAILURE);
     }
     printf("Done.\n\n");

     dlerror();

     data_new = (RStruct* (*)(void)) dlsym(handle, "data_new");
     error = dlerror();
     if (error != NULL) {
       fprintf(stderr, "%s\n", error);
       exit(EXIT_FAILURE);
     }

     dlerror();
     
     data_free = (void (*)(RStruct*)) dlsym(handle, "data_free");
     error = dlerror();
     if (error != NULL) {
       fprintf(stderr, "%s\n", error);
       exit(EXIT_FAILURE);
     }

     printf("Calling data_new() from main.c...\n");
     RStruct* data = (*data_new)();

     printf("\nBack inside main.c. Printing results...\n");
     printf("Name: %s\nValue: %d\n", data->name, data->value._int._0);

     printf("\nFreeing the RStruct data...\n");
     (*data_free)(data);

     dlclose(handle);
     return EXIT_SUCCESS;
   }

This code is based on the example in the ``dlopen()`` `man pages`_. In particular, the library file
is opened and a handle attached to it here:

.. code-block:: c

     handle = dlopen(
       "librstruct.so",
       RTLD_LAZY
     );

A function pointer to ``data_new()`` is created with ``dlsym()``, and we use the function to create
the new ``RStruct`` instance with the lines

.. code-block:: c

   data_new = (RStruct* (*)(void)) dlsym(handle, "data_new");
   // snip
   RStruct* data = (*data_new)();

Finally, the data is freed by creating another function pointer to ``data_free()`` and calling it.

.. code-block:: c

   data_free = (void (*)(RStruct*)) dlsym(handle, "data_free");
   // snip
   (*data_free)(data);

Running the program
-------------------

I wrote a small Makefile to handle compilation of the C and Rust programs while I wrote this
post. I won't include it here because it distracts from the main message about the Rust
FFI. Instead, I will describe how to compile the program from the command line.

I first placed the ``librstruct.so``, ``rstruct.h``, and ``main.c`` programs into the following
directory structure:

.. code-block:: console

   $ tree
   .
   ├── include
   │   └── rstruct.h
   ├── lib
   │   └── librstruct.so
   └── src
       └── main.c

Next, I compiled the ``main`` binary with gcc.

.. code-block:: console

   $ gcc -Wall -g -Iinclude -c -o main.o main.c
   $ gcc -Wall -g -o main main.o -ldl

(``-ldl`` is used to link against libdl for dynamically loading the library from C.) After
compilation I run the ``main`` binary. To make it work, I set the ``LD_LIBRARY_PATH`` environment
variable so that the program knows to look inside the ``lib`` directory for the ``librstruct.so``
library.

.. code-block:: console

   $ LD_LIBRARY_PATH=lib ./main
   Loading librstruct.so...
   Done.

   Calling data_new() from main.c...
   Inside data_new().

   Back inside main.c. Printing results...
   Name: my_rstruct
   Value: 42

   Freeing the RStruct data...

Nice! From the output you can see the print statements that I placed inside both the Rust and C
code to indicate where the program was as it was running. In summary, the program performs the
following sequence of events:

- The main binary is run
- The ``librstruct.so`` library is opened and pointers to the ``data_new()`` and ``data_free()``
  functions are created
- ``data_new()`` is called, creating our Rust datatype on the heap and returning a pointer to it in
  the C code
- Information about the data type is printed from C
- ``data_free()`` is called, freeing the memory from back inside Rust

Summary
=======

And that's it! I hope you enjoyed this post. It took me several days of reading and trial-and-error
to learn about this feature of Rust. The topics covered here were

- the Rust FFI and its purpose
- creating a complex data type (a Rust enum nested inside a Rust struct) and exporting it through
  the FFI
- ``Box`` and ``CString`` Rust data types
- ``cbindgen`` for automatically creating header files from Rust code
- using the Rust library from inside C

.. _`Rust Foreign Function Interface`: https://doc.rust-lang.org/nomicon/ffi.html
.. _`2018 edition guide`: https://doc.rust-lang.org/edition-guide/rust-2018/platform-and-target-support/cdylib-crates-for-c-interoperability.html
.. _`Rustonomicon`: https://doc.rust-lang.org/nomicon/other-reprs.html
.. _`raw pointer`: https://doc.rust-lang.org/std/primitive.pointer.html
.. _`part of the type name`: https://doc.rust-lang.org/beta/book/ch19-01-unsafe-rust.html#dereferencing-a-raw-pointer
.. _`the Book`: https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#calling-rust-functions-from-other-languages
.. _`application binary interface from C`: https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#using-extern-functions-to-call-external-code
.. _`would have been deallocated`: https://doc.rust-lang.org/std/ffi/struct.CString.html#method.as_ptr
.. _`ownership will be passed off to the calling C code`: https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_raw
.. _`allocate memory for a data type on the heap`: https://doc.rust-lang.org/book/ch15-01-box.html
.. _`is unsafe`: https://doc.rust-lang.org/std/boxed/struct.Box.html#method.from_raw
.. _`cbindgen`: https://github.com/eqrion/cbindgen
.. _`man pages`: https://linux.die.net/man/3/dlopen
