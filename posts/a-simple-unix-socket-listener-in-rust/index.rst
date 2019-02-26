.. title: A simple UNIX socket listener in Rust
.. slug: a-simple-unix-socket-listener-in-rust
.. date: 2019-02-24 16:25:58 UTC+01:00
.. tags: rust, linux
.. category: 
.. link: 
.. description: How to read from a UNIX socket in Rust
.. type: text

I decided that I wanted to learn a new programming language in 2019. After a bit of research, I
settled upon `Rust`_ due to its speed, novel ideas about memory safety, and `focus on two areas
that I am interested in`_: embedded systems and WebAssembly. While I think that `The Book`_ is the
best place to get started learning the language, nothing is a really a substitute for writing
code.

With that in mind, I developed an idea for a starting project: a background daemon for Linux
systems like the Raspberry Pi that controls and reads data from the system's peripherals. The
design of this project is inspired by Docker: a daemon process does most of the heavy work while a
command line tool communicates with the Daemon over a Unix socket (typically a file located at
``/var/run/docker.sock``). The purpose of this post is to demonstrate the most basic realization of
this: reading text from a UNIX socket in Rust.

To begin, I created a new Rust project with ``cargo``.

.. code-block:: shell

   $ cargo new rust-uds
   $ cd rust-uds

Next, I opened the file that cargo automatically generated in ``src/main.rs``, removed the
auto-generated content, and added the following code, which is largely taken from the `example`_
provided in the Rust documentation:

.. code-block:: rust
   :linenos:
      
   use std::io::Read;
   use std::os::unix::net::{UnixStream,UnixListener};
   use std::thread;

   fn handle_client(mut stream: UnixStream) {
       let mut response = String::new();

       stream.read_to_string(&mut response).unwrap();
       println!("{}", response);
   }

   fn main() {
       let listener = UnixListener::bind("/tmp/rust-uds.sock").unwrap();

       for stream in listener.incoming() {
          match stream {
               Ok(stream) => {
                   thread::spawn(move || handle_client(stream));
               }
               Err(err) => {
                   println!("Error: {}", err);
                   break;
               }
           }
       }
   }


Explanation
===========

The first three lines import the necessary modules for this code example.

.. code-block:: rust

   use std::io::Read;
   use std::os::unix::net::{UnixStream,UnixListener};
   use std::thread;

``Read`` is a trait that must be imported into the current scope to use the `read_to_string()`
method. ``UnixStream`` and ``UnixListener`` are structs that provide the functionality for handling
the UNIX socket, and the ``std::thread`` module is used to spawn threads.

The next set of lines defines a function named ``handle_client()`` that is called whenever new data
arrives in the stream. The explanation for this is best left until after the ``main()`` function.

The first line in the ``main()`` function creates the UnixListener struct and binds it to the
``listener`` variable.

.. code-block:: rust

   let listener = UnixListener::bind("/tmp/rust-uds.sock").unwrap();

The ``bind()`` function takes a string argument that is a path to the socket file and ``unwrap()``
moves the value out of the Option that is returned by ``bind()``. (This is a pattern that is
`discouraged`_ in Rust but is OK for quick prototypes because it simplifies the error handling.)

After creating the listener, ``listener.incoming()`` returns an iterator over the incoming
connections to the socket. The connections are looped over in an infinite for loop; I believe that
this is more-or-less the same as a generator in Python which never raises a ``StopIteration``
exception.

Next, the ``Result`` of the incoming streams is matched; if there is an error, it is printed and
the loop it exited:

.. code-block:: rust

   Err(err) => {
       println!("Error: {}", err);
       break;
   }
   
However, if the ``Result`` of the connection is ``Ok``, then a new thread is spawned to handle the
new stream:

.. code-block:: rust

   Ok(stream) => {
       thread::spawn(move || handle_client(stream));
   }

I had to add the ``move`` keyword to the argument of ``thread.spawn()`` to make the compiler
happy. The reason is that the argument to the client handler is mutable, which I think means that
it needs to take ownership of the stream. (See the documentation `here`_.)

Finally, the client handler is called for each connection.

.. code-block:: rust

   fn handle_client(mut stream: UnixStream) {
       let mut response = String::new();

       stream.read_to_string(&mut response).unwrap();
       println!("{}", response);
   }

The handler in this case is fairly straight-forward. The response is stored in a mutable string
which we extract from the stream and printed to terminal.

.. _`Rust`: https://www.rust-lang.org/
.. _`focus on two areas that I am interested in`: https://blog.rust-lang.org/2018/03/12/roadmap.html#four-target-domains
.. _`The Book`: https://doc.rust-lang.org/book/
.. _`example`: https://doc.rust-lang.org/std/os/unix/net/struct.UnixListener.html#examples
.. _`discouraged`: https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap
.. _`here`: https://doc.rust-lang.org/book/ch16-01-threads.html#using-move-closures-with-threads
