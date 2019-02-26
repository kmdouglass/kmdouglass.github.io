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
this: reading text from a UNIX socket in Rust. And to emphasize that the UNIX socket is used for
communication between two separate processes, we will send messages from Bash to Rust.

Keep in mind that this is my first-ever Rust program, so it may not be completely idiomatic
Rust. The following was compiled with rustc 1.32.0 (9fda7c223 2019-01-16).

To begin, I created a new Rust project with ``cargo``.

.. code-block:: shell

   $ cargo new rust-uds
   $ cd rust-uds

Next, I opened the file that cargo automatically generated in ``src/main.rs``, removed the
auto-generated content, and added the following code, which is largely based on the `example`_
provided in the Rust documentation but with a few key differences:

.. code-block:: rust
   :linenos:
      
   use std::io::{BufRead, BufReader};
   use std::os::unix::net::{UnixStream,UnixListener};
   use std::thread;

   fn handle_client(stream: UnixStream) {    
       let stream = BufReader::new(stream);
       for line in stream.lines() {
           println!("{}", line.unwrap());
       }
   }

   fn main() {
       let listener = UnixListener::bind("/tmp/rust-uds.sock").unwrap();

       for stream in listener.incoming() {
           match stream {
               Ok(stream) => {
                   thread::spawn(|| handle_client(stream));
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

   use std::io::{BufRead, BufReader};
   use std::os::unix::net::{UnixStream,UnixListener};
   use std::thread;

``BufRead`` is a trait that enables extra ways of reading data sources; in this case, it has an
internal buffer for reading the socket line-by-line. ``BufReader`` is a struct that actually
implements the functionality in ``BufRead``. ``UnixStream`` and ``UnixListener`` are structs that
provide the functionality for handling the UNIX socket, and the ``std::thread`` module is used to
spawn threads.

The next set of lines defines a function named ``handle_client()`` that is called whenever new data
arrives in the stream. The explanation for this is best left until after the ``main()`` function.

The first line in the ``main()`` function creates the UnixListener struct and binds it to the
``listener`` variable.

.. code-block:: rust

   let listener = UnixListener::bind("/tmp/rust-uds.sock").unwrap();

The ``bind()`` function takes a string argument that is a path to the socket file and ``unwrap()``
moves the value out of the Result that is returned by ``bind()``. (This is a pattern that is
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
       thread::spawn(|| handle_client(stream));
   }

Finally, the client handler is called for each connection.

.. code-block:: rust

   fn handle_client(mut stream: UnixStream) {
       let stream = BufReader::new(stream);
       for line in stream.lines() {
           println!("{}", line.unwrap());
       }
   }

The handler in this case is fairly straight-forward. It shadows the original ``stream`` variable by
binding it to a version of itself that has been converted to a ``BufReader``. Finally, it loops
over the ``lines()`` iterator, which blocks until a new line appears in the stream.

Sending messages
================

As an example, let's send messages to the Rust program via Bash using `the OpenBSD version of
netcat`_. (The OpenBSD version seems to be the default on Ubuntu-based systems.) This should
underscore the fact that the UNIX socket is really being used to communicate between two different
processes.

First, compile and run the Rust program to start the socket listener:

.. code-block::

   $ cargo run --release
      Compiling rust-uds v0.1.0 (/home/kmd/src/rust-uds)
       Finished release [optimized] target(s) in 1.59s
        Running `target/release/rust-uds`

Open up a new terminal. You should see the socket file /tmp/rust-uds.sock:

.. code-block::

   $ ls /tmp | grep rust
   rust-uds.sock

Now let's send messages to the rust program. Use the following netcat command to open a connection
to the socket.

.. code-block::

   $ nc -U /tmp/rust-uds.sock

The ``-U`` is necessary to indicate to netcat that this is a UNIX stream socket. Now, start typing
text into the same window. Every time you press ENTER, you should see the same text appear in the
terminal window in which the Rust program is running. Press CTRL-C to exit the Rust socket
listener. If you re-run the program, delete the old socket first: ``rm /tmp/rust-uds.sock``

Summary
=======

- Use a ``UnixListener`` struct to create a UNIX socket and listen to it for connections.
- For each new connection, spawn a new thread and read the stream with a ``BufReader``.
- Print each new line in the stream by iterating over the ``lines()`` iterator of the
  ``BufReader``.
- Send commands to your Rust program from bash with ``nc -U "$PATH_TO_SOCKET"``.

.. _`Rust`: https://www.rust-lang.org/
.. _`focus on two areas that I am interested in`: https://blog.rust-lang.org/2018/03/12/roadmap.html#four-target-domains
.. _`The Book`: https://doc.rust-lang.org/book/
.. _`example`: https://doc.rust-lang.org/std/os/unix/net/struct.UnixListener.html#examples
.. _`discouraged`: https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap
.. _`here`: https://doc.rust-lang.org/book/ch16-01-threads.html#using-move-closures-with-threads
.. _`the OpenBSD version of netcat`: http://man.openbsd.org/nc
