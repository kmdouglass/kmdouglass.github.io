.. title: Variable locations in Rust during copy and move
.. slug: variable-locations-in-rust-during-copy-and-move
.. date: 2019-11-24 10:46:20 UTC+01:00
.. tags: rust
.. category: 
.. link: 
.. description: An exploration of memory layout during copy and move operations in Rust
.. type: text

`Ownership`_ is a well-known concept in Rust and is a major reason for the language's memory
safety. Consider the following example of ownership from `The Rust Programming Language`_:

.. code-block:: rust
   :linenos:

   let s1 = String::from("hello");
   let s2 = s1;

   println!("{}, world!", s1);

Compiling this code will produce an error because the ``String`` value that is bound to the
variable ``s1`` is moved to ``s2``. After a move, you may no longer use the value bound to
``s1``. (You may, as we will see, re-use its memory by binding a new value of the same type to it.)

``String`` is a container type, which means that it contains both metadata on the stack and a
pointer to data on the heap. Simple types such as ``i32``, on the other hand, are normally stored
entirely on the stack. Types such as these implement the `Copy`_ trait. This means that variable
reassignment does not produce a compile-time error like it does in the example above:

.. code-block:: rust
   :linenos:

   let x = 42;
   let y = x;

   // The value bound to x is Copy, so no error will be raised.
   println!("{}", x);

``String`` is not ``Copy`` because it contains a pointer to data on the heap. When a variable that
is bound to a ``String`` is dropped, its data is automatically freed from the heap. If a ``String``
were ``Copy``, the compiler would have to determine whether the heap data is still pointed to by
another variable to avoid a `double free error`_.

Memory layout in copies and moves
=================================

What's happening inside a program's memory during copies and moves? Consider first a move:

.. code-block:: rust
   :linenos:

   let mut x = String::from("foo");
   println!("Memory address of x: {:p}", &x);

   // Move occurs here
   let y = x;
   println!("Memory address of y: {:p}", &y);

   // Printing the memory address of x is an error because its value was moved.
   // println!("Memory address of x: {:p}", &x)

   // Assign new string to x
   x = String::from("bar");
   println!("Memory address of x: {:p}", &x);

In the above code snippet, addresses of variables are printed by using the pointer formatter
``:p``. I create a ``String`` value and bind it to the variable ``x``. Then, the value is moved to
the variable ``y`` which prevents me from using ``x`` again in the ``println!`` macro.

However, I can assign a new ``String`` value to ``x`` by reusing its memory on the stack. This does
not change its memory address as seen in the output below:

.. code-block:: console
   :linenos:

   Memory address of x: 0x7ffded2aa3d0
   Memory address of y: 0x7ffded2aa3f0
   Memory address of x: 0x7ffded2aa3d0  # Memory address of x is unchanged after reassignment

A copy is similar. In the snippet below, an integer that is originally bound to ``x`` is copied to
``y``, which means that I can still refer to ``x`` in the ``println!`` macro.

.. code-block:: rust
   :linenos:

   let mut x = 42;
   println!("Memory address of x: {:p}", &x);

   // Move occurs here
   let y = x;
   println!("Memory address of y: {:p}", &y);

   // Printing the memory address of x is not an error because its value was copied.
   println!("Memory address of x: {:p}", &x);

   // Assign new integer to x
   x = 0;
   println!("Memory address of x: {:p}", &x);

Both the copy operation and value reassignment do not change the memory locations of ``x`` as seen
in the program's output:

.. code-block:: console
   :linenos:

   Memory address of x: 0x7ffee579d544
   Memory address of y: 0x7ffee579d548
   Memory address of x: 0x7ffee579d544  # Memory address of x is unchanged after copy
   Memory address of x: 0x7ffee579d544  # Memory address of x is unchanged after reassignment

Summary
=======

Move semantics on container types are one of the reasons for Rust's memory safety. Nothing
mysterious is happening in memory when a value is moved from one location to another. The original
stack memory still exists; its use is simply disallowed by the compiler until a new value is
assigned to it.

The complete program from this post may be found here:
https://gist.github.com/kmdouglass/e596d0934e15f6b3a96c1eca6f6cd999
   
.. _`Ownership`: https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html
.. _`The Rust Programming Language`: https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#memory-and-allocation
.. _`Copy`: https://doc.rust-lang.org/std/marker/trait.Copy.html
.. _`double free error`: https://stackoverflow.com/questions/21057393/what-does-double-free-mean
