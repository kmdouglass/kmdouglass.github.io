.. title: Create a custom Raspbian image with pi-gen
.. slug: create-a-custom-raspbian-image-with-pi-gen
.. date: 2018-07-14 19:15:28 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Docker has been an amazing tool for improving my development
efficiency on the Raspberry Pi. For example, I recently used it to
`cross-compile a large C++ and Python library`_ for the Pi's ARM
architecture on my x86_64 laptop. However, in that post I took it for
granted that I had already set up my Raspberry Pi with user accounts,
packages, ssh keys, etc. Performing these steps manually on a fresh
install of the Pi's `Raspbian`_ operating system can become tedious,
especially because ssh needs to be manually enabled before doing any
remote work.

Fortunately, the Raspberry Pi developers have provided us with
`pi-gen`_, useful collection of Shell scripts and a Docker container
for creating custom Raspbian images. In this post, I will summarize
the steps that I take in using pi-gen to create my own, personalized
Raspbian image.

Clone the pi-gen repository
===========================

This is as easy as cloning the git repository.

.. code-block:: shell
   
   git clone git@github.com:RPi-Distro/pi-gen.git

Alternatively, you can use the https address instead of ssh, which is
https://github.com/RPi-Distro/pi-gen.git.

Build the official Raspbian images
==================================

By default, the pi-gen repository will build the official Raspbian
images. Doing this once before making any modifications is probably a
good idea; if you can't build the official images, how will you be
able to build a custom image?

There are two main scripts that you can use to do this: **build.sh**
and **build-docker.sh**. **build.sh** requires you to install the
packages that are listed in the repository's README.md file, whereas
**build-docker.sh** requires that you have Docker already installed on
your computer. I'm going to be using the Docker-based build script for
the rest of this post. If you don't have Docker installed on your
system, you can `follow the instructions here`_ for the community
edition.

Name your image
---------------

First we need to give a name to our image, even if we use the default
build. To do this, we assign a name to a variable called **IMG_NAME**
inside a file called **config** that is located inside the root pi-gen
folder.

.. code-block:: shell
   
   echo "IMG_NAME=my_name" > config

Build the default image
-----------------------

Once we've named our image, we can go ahead and run the build script.

.. code-block:: shell
   
   ./build-docker.sh

Be prepared to wait a while when running this script; the full build
took well over half an hour on my laptop and with the Docker volume
located on a SSD. It also consumed several GB of space on the SSD.

Resuming a failed build
+++++++++++++++++++++++

The first time I used pi-gen the build failed twice. Once, it hung
without doing anything for several minutes, so I canceled it with a
**Ctrl-C** command. The other time I encountered a hash error when
installing a Debian package.

We can resume a failed build from the point of failure by assigning
the value 1 to the CONTINUE variable when calling build-docker.sh
again.

.. code-block:: shell
   
   CONTINUE=1 ./build-docker.sh

After a successful build, we can find our custom images located inside
the **deploy** folder of the pi-gen directory. These may then be
written onto a SD card and used as a standard Raspbian image.

Custom Raspbian images
======================

Now that we've got the default build working, let's start by
customizing the build process. For this post, I have the following
goals:

- Build only the *lite* version of the Raspbian images
- Add a custom user account and delete the default *pi* account
- Setup the WiFi for a home network
- Setup ssh so that we can log on to the Pi remotely on its first
  startup

   
.. _cross-compile a large C++ and Python library: link://slug/how-i-built-a-cross-compilation-workflow-for-the-raspberry-pi
.. _Raspbian: https://www.raspberrypi.org/downloads/raspbian/
.. _pi-gen: https://github.com/RPi-Distro/pi-gen
.. _follow the instructions here: https://docs.docker.com/install/
