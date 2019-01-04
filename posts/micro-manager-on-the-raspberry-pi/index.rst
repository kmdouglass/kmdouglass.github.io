.. title: Micro-Manager on the Raspberry Pi
.. slug: micro-manager-on-the-raspberry-pi
.. date: 2017-02-10 19:31:57 UTC+01:00
.. tags: micro-manager, raspberry pi, microscopy, open source
.. category: embedded microscopy
.. link: 
.. description: How I compiled Micro-Manager 2.0 on the Raspberry Pi
.. type: text

`Micro-Manager`_ is an open source platform for controlling microscope
hardware, automating image acquisition, and tracking metadata about
how images are acquired. In biomedical imaging research, it serves as
an incredibly important tool because it is free and open source, which
means that scientists can benefit from the contributions of others to
the software without paying costly licensing fees.

I recently managed to compile Micro-Manager version 2.0 on the
Raspberry Pi. I did this for a small hobby project I am working on to
build a cheap yet effective tool for `at-home microscope projects and
hacking`_. Though I am not yet convinced that Micro-Manager will be
the best tool for this particular job given it's relatively heavy
footprint on the Pi's slower hardware, I thought that I would post my
notes so that others could benefit from my experience.

.. _Micro-Manager: https://micro-manager.org/
.. _at-home microscope projects and hacking: https://hackaday.io/project/19677-basic-lensless-imaging-for-low-cost-microscopy

Software versions
=================

I am working with a Raspberry Pi 3 Model B::

  pi@raspberrypi:~ $ uname -a & gcc -dumpversion & make -v & ldd --version
  Linux raspberrypi 4.4.38-v7+ #938 SMP Thu Dec 15 15:22:21 GMT 2016 armv7l GNU/Linux

  pi@raspberrypi:~ $ gcc -dumpversion
  4.9.2

  pi@raspberrypi:~ $ make -v
  GNU Make 4.0

  pi@raspberrypi:~ $ ldd --version
  ldd (Debian GLIBC 2.19-18+deb8u7) 2.19

Setup a network share for 3rd party libraries
=============================================

We need to compile Micro-Manager because binares for the Pi's ARM
processor are not distributed by the Micro-Manager team (probably
because too few people have ever wanted them). To compile
Micro-Manager, we need to checkout a rather large set of 3rd party
libraries. When I last checked, these libraries occupied 6.7 GB of
space on my laptop, a size which can be prohibitive when using the
Micro-SD cards that provide storage for the Pi.

To circumvent this problem, I checked out the **3rdpartypublic** SVN
repository onto my laptop and created a network share from this
directory. Then, I mounted the share on my Pi in the directory just
above that containing the Micro-Manager source code.

To get started, first have a look at my post on connecting a Pi to a
Linux home network for ideas if you haven't already connected the Pi
to your other machines at home:
http://kmdouglass.github.io/posts/connecting-a-raspberry-pi-to-a-home-linux-network.html

Once the Pi and the laptop are on the same network, checkout the SVN
3rdpartypublic repository onto your laptop or home server. You may
need to do this a few times until completion because the downloads can
timeout after a few minutes::

  svn checkout https://valelab4.ucsf.edu/svn/3rdpartypublic/

Next, we need to setup the network share. If your laptop or server is
running Windows, then you will probably need to setup `Samba`_ on the
Pi to share files between them. I however am running a Linux home
network, so I decided to use `NFS`_ (Network File Sharing) to share
the directory between my laptop--which runs Debian Linux--and the
Pi. I installed NFS on my laptop with::
  
  sudo apt-get install nfs-kernel-server nfs-common

Once installed, I added the following line to the newly created
/etc/exports file::

  /home/kmdouglass/src/micro-manager/3rdpartypublic 192.168.0.2/24(ro)

The first part is the directory to share, i.e. where the
3rdpartypublic directory is stored on my laptop. The second part
contains the static IP address of the Pi on my home network. The /24
was REQUIRED for my client (the Pi) to mount the share. /24 simply
denotes a network mask of 255.255.255.0; if you have a different mask
on your network, then you can find a good discussion on this topic
here: https://arstechnica.com/civis/viewtopic.php?t=751834 Finally,
(...)  specifies shared options and **ro** means read only.

After editing the file, export the folder and restart the NFS server::
  
  sudo exportfs -arv
  sudo /etc/init.d/nfs-kernel-server restart

On the client (the Pi), the NFS client software was already
installed. However, I had to restart the rpcbind service before I
could mount the share::

  sudo /etc/init.d/rpcbind restart

Finally, I added a line to the **/etc/fstab** file on the Pi to make
mounting the 3rdpartypublic share easier::

  192.168.0.102:/home/kmdouglass/src/micro-manager/3rdpartypublic /home/pi/src/micro-manager/3rdpartypublic nfs user,noauto 0 0

The first part indicates the IP of the laptop and the share to
mount. The second part, **/home/pi/src/micro-manager/3rdpartypublic**
is the directory on the Pi where the share will be mounted. I placed
this one directory above where the MM source code is,
(**/home/pi/src/micro-manager/micro-manager** on my machine). **nfs**
indicates the type of share to mount, and **user,noauto** permits any
user to mount the share (not just root), though this share will not be
automatically mounted when the Pi starts. The final two zeros are
explained in the fstab comments but aren't really important for us. To
mount the share, type the following on the Pi::

  sudo mount /home/pi/src/micro-manager/3rdpartypublic

In case you're interested in learning more about the intricacies of
Linux home networking, I found the following sources of information to
be incredibly helpful.

1. https://www.howtoforge.com/install_nfs_server_and_client_on_debian_wheezy
2. https://www.youtube.com/watch?v=luqq8DUqqCw
3. http://nfs.sourceforge.net/nfs-howto/ar01s03.html#config_server_setup
4. http://www.tecmint.com/how-to-setup-nfs-server-in-linux/

.. _Samba: https://www.samba.org/samba/what_is_samba.html
.. _NFS: https://en.wikipedia.org/wiki/Network_File_System

Building MM
===========

Once I was able to mount the share containing 3rd party libraries, I
installed the following packages on the Pi and checked out the
Micro-Manager source code::

  sudo apt-get install autoconf automake libtool pkg-config swig ant libboost-dev libboost-all-dev
  cd ~/src/micro-manager
  git clone https://github.com/micro-manager/micro-manager.git
  cd micro-manager
  git checkout mm2

The last command switches to the mm2 branch where the Micro-Manager
2.0 source code is found. Note that it may not be necessary to install
all of the boost libraries with :code:`sudo apt-get install
libboost-all-dev`, but I did this anyway because I encountered
multiple errors due to missing boost library files the first few times
I tried compiling.

The next step follows the normal Micro-Manager build routine using
make, with the exception of the configuration step. From inside the
Micro-Manager source code directory on the Pi, run the following
commands one at a time::

  ./autogen.sh
  PYTHON=/usr/bin/python3 ./configure --prefix=/opt/micro-manager --with-ij-jar=/usr/share/java/ij.jar --with-python=/usr/include/python3.4 --with-boost-libdir=/usr/lib/arm-linux-gnueabihf --with-boost=/usr/include/boost
  make fetchdeps
  make
  sudo make install

In the configuration step, I set the Python interpreter to Python 3
because I greatly prefer it over Python 2. This is done by setting the
**PYTHON** environment variable before running
configure. **--prefix=/opt/micro-manager/** indicates the preferred
installation directory of
Micro-Manager. **--with-ij-jar=/usr/share/java/ij.jar** is the path to
the ImageJ Java library, though I am uncertain whether this was
necessary. (I installed ImageJ with a :code:`sudo apt-get install
imagej` a while ago.) **--with-python=/usr/include/python3.4** should
point to the directory containing the **Python.h** header file for the
version of Python you are compiling against. **with-boost-libdir**
should point to the directory containing the boost libraries (.so
files). This was critical for getting MM2 to build. If you are unsure
where they are located, you can search for them with :code:`sudo find
/ -name "libboost*"`. Finally, the last option, **with-boost**, may or
may not be necessary. I set it to the directory containing the boost
headers but never checked to see whether MM compiles without it.

If all goes well, Micro-Manager will compile and install without
problems. Compilation time on my Pi took around one hour.

Set the maximum amount of direct memory
+++++++++++++++++++++++++++++++++++++++

In the next step, we need to make a minor edit to the Micro-Manager
Linux start script. Edit the script
(/opt/micro-manager/bin/micromanager) to reduce the maximum direct
memory to something reasonable::

  /usr/lib/jvm/jdk-8-oracle-arm32-vfp-hflt/bin/java -Xmx1024M \
    -XX:MaxDirectMemorySize=1000G \
     -classpath "$CLASSPATH" \
     -Dmmcorej.library.loading.stderr.log=yes \
     -Dmmcorej.library.path="/opt/micro-manager/lib/micro-manager" \
     -Dorg.micromanager.plugin.path="/opt/micro-manager/share/micro-manager/mmplugins" \

Change 1000G to 512M or 256M; otherwise the Pi will complain that the
MaxDirectMemorySize of 1000G is too large. You can start Micro-Manager
by running this modified script.

What's next?
============

Though Micro-Manager compiles and runs on the Pi, I have not yet
tested it thoroughly acquisitions. I am currently waiting on a camera
board to arrive in the mail, and when it does, I will attempt to
interface with it through Micro-Manager. Though I could write my own
Python library, Micro-Manager is appealing because it can save a lot
of time by providing a ready-made means to annotate, process, and
store imaging data.

Running Micro-Manager on the Pi also raises the possibility of a fully
open, embedded biomedical imaging platform, though I am uncertain at
the moment whether the hardware on the Pi is up to the task. If you
manage to do anything cool with Micro-Manager and the Raspberry Pi,
please let me know in the comments!
