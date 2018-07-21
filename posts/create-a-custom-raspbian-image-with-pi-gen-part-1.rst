.. title: Create a custom Raspbian image with pi-gen: part 1
.. slug: create-a-custom-raspbian-image-with-pi-gen-part-1
.. date: 2018-07-21 12:31:28 UTC+02:00
.. tags: raspbian, raspberry pi, devops
.. category: raspberry pi
.. link: 
.. description: Part 1 of a tutorial on creating custom Raspbian images with pi-gen.
.. type: text
.. status: published

.. role:: shell(code)
   :language: shell
   
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
`pi-gen`_, a useful collection of Shell scripts and a Docker container
for creating custom Raspbian images. In this post, I will summarize
the steps that I take in using pi-gen to create my own, personalized
Raspbian image.

*After I wrote this post, I found a set of posts at* `Learn Think
Solve Create`_ *that describe many of the tasks I explain here. Be
sure to check them out for another take on modifying Raspbian images.*

Clone the pi-gen repository
===========================

This is as easy as cloning the git repository.

.. code-block:: shell
   
   git clone git@github.com:RPi-Distro/pi-gen.git

Alternatively, you can use the https address instead of ssh, which is
https://github.com/RPi-Distro/pi-gen.git.

From now on, all directories in this post will be relative to the root
pi-gen directory.

Build the official Raspbian images
==================================

By default, the pi-gen repository will build the official Raspbian
images. Doing this once before making any modifications is probably a
good idea; if you can't build the official images, how will you be
able to build a custom image?

There are two main scripts that you can use to do this: **build.sh**
and **build-docker.sh**. build.sh requires you to install the packages
that are listed in the repository's README.md file, whereas
build-docker.sh requires only that you have Docker already installed
on your computer. I'm going to be using the Docker-based build script
for the rest of this post. If you don't have Docker installed on your
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

If we don't want to run previously built stages, we can simply place a
file inside the corresponding folder named SKIP. For example, if our
build fails at stage2, we can place SKIP files inside the stage0 and
stage1 folders, then rerun the build-docker.sh script with
CONTINUE=1.

Unfortunately, I have sometimes noticed that I have to also rebuild
the stage *prior* to the one where the build failed. In the worst
case, I had to rebuild all the stages because the fixes I applied to a
file in stage2 were not accounted for when I tried to skip building
stages 0 and 1. YMMV with this; I have no idea how well the SKIP
mechanism works for the normal build.sh script.
   
After a successful build, we can find our custom images located inside
the **deploy** folder of the pi-gen directory. These may then be
written onto a SD card and used as a standard Raspbian image.

We can ensure that the build container is preserved even after successful
builds using

.. code-block:: shell

   PRESERVE_CONTAINER=1 ./build-docker.sh

Custom Raspbian images
======================

Now that we've got the default build working, let's start by
customizing the build process. For this post, I have the following
goals:

- Build only the *lite* version of the Raspbian images
- Add a custom user account and delete the default *pi* account
- Set the Pi's locale information

In a follow-up post, I will discuss the following:

- Setup the WiFi for a home network
- Setup ssh so that we can log on to the Pi remotely on its first
  startup

Building just Raspbian Lite
---------------------------

Raspbian Lite is a `minimal Raspbian image`_ without the X windows
server and speciality modules that would otherwise make Raspbian more
user friendly. It's an ideal starting point for projects that are
highly specialized, require only a few packages, and do not require a
GUI.

pi-gen creates Raspbian images in sequential steps called stages. At
the time of this writing, there were five stages, with stages 2, 4,
and 5 producing images of the operating system. Building everything
from stage 0 up to and including stage 2 produces a Raspbian Lite
image. We can speed up the build process and save harddrive space by
disabling all the later stages.

To disable the build for a particular a stage, we add an empty file
called **SKIP** inside the corresponding stage folder of the pi-gen
root directory, just as we did above when skipping previously built
stages. We also disable the explicit creation of images by adding an
empty file called **SKIP_IMAGES** to stages 4 and 5. (We don't need to
add a SKIP_IMAGES file to the stage3 folder because no image is
produced at this stage.)

.. code-block:: shell

   touch ./stage3/SKIP ./stage4/SKIP ./stage5/SKIP
   touch ./stage4/SKIP_IMAGES ./stage5/SKIP_IMAGES

Now, when we run build-docker.sh, pi-gen will only build and produce
one image for Raspbian Lite in the deploy directory.

 
Add a custom user account
-------------------------

The default user in Raspbian is called **pi**. This account is created
in stage1 in the the script **stage1/01-sys-tweaks/00-run.sh**. This
account is not very secure because it and its password, *raspberry*,
are the well-known defaults in Raspbian. Let's go ahead and change
them.

The relevant lines in the script look like this:

.. code-block:: shell

   on_chroot << EOF
   if ! id -u pi >/dev/null 2>&1; then
	adduser --disabled-password --gecos "" pi
   fi
   echo "pi:raspberry" | chpasswd
   echo "root:root" | chpasswd
   EOF

The user pi is created with the line
:shell:`adduser --disabled-password --gecos "" pi` if it doesn't
already exist. According to the `adduser man pages`_
The --disabled-password flag prevents the program passwd from setting
the account's password when adduser is run, but remote logins without
password authentication to the pi account are still allowed. the
:shell:`--gecos ""` flag simply adds an empty string to the
/etc/passwd file for the pi account.

After the user is created, *raspberry* is set as pi's password and
*root* is set as the root password in the lines :shell:`echo
"pi:raspberry" | chpasswd` and :shell:`echo "root:root" | chpasswd`.

Let's start by modifying the pi account. For the sake of this example,
let's change its name to alphapi. For the password, we will generate a
**temporary, random** password and write it to a file in the deploy
directory. We'll do the same for root. The modifications look like the
following:

.. code-block:: shell

   user_passwd=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-8})
   root_passwd=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-8})

   # Write passwords to a file.
   cat <<EOF > /pi-gen/deploy/users
   ${user_passwd}
   ${root_passwd}
   EOF

   on_chroot << EOF
   if ! id -u alphapi >/dev/null 2>&1; then
	adduser --disabled-password --gecos "" alphapi
   fi
   echo "alphapi:${user_passwd}" | chpasswd
   echo "root:${root_passwd}" | chpasswd
   EOF

The first two lines create random alphanumeric passwords for the users
alphapi and root. They should be changed immediately when the image is
first run.

.. code-block:: shell

   user_passwd=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-8})
   root_passwd=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-8})		

This way of password generation works by reading random bytes from
/dev/urandom and redirecting them to the standard input of the tr
command, which filters the input so only alphanumeric characters
remain. Next, the output is piped to the head command, which outputs
only the first eight alphanumeric characters produced in this fashion.

The passwords are then written to a file named **users** inside the
deploy directory where the outputs will eventually be placed.

.. code-block:: shell

   # Write passwords to a file.
   cat <<EOF > /pi-gen/deploy/users
   ${user_passwd}
   ${root_passwd}
   EOF

The remaining parts of the script are more-or-less the same as before,
except I changed pi to alphapi and used variable substitution for the
passwords.

Running ./build-docker.sh at this point will raise an error in stage02
because it's at this stage where the user pi is added to the various
groups on the system. We therefore need to open
**stage2/01-sys-tweaks/01-run.sh** and modify the following lines,
replacing pi with alphapi.

.. code-block:: shell

   for GRP in adm dialout cdrom audio users sudo video games plugdev input gpio spi i2c netdev; do
       adduser alphapi $GRP
   done

Set the locale information
--------------------------

The locale information used by your operating system may be modified
as follows. Open **stage0/01-locale/00-debconf**. I personally changed
every occurence of en_GB.UTF-8 to en_US.UTF-8, but you can set your
locale accordingly.

.. code-block:: shell

   # Locales to be generated:
   # Choices: All locales, aa_DJ ISO-8859-1, aa_DJ.UTF-8 UTF-8, ...
   locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8
   # Default locale for the system environment:
   # Choices: None, C.UTF-8, en_US.UTF-8
   locales locales/default_environment_locale	select	en_US.UTF-8

Next, we open **stage2/01-sys-tweaks/00-debconf**. I currently live in
Europe, so I made the following changes::

  tzdata	tzdata/Areas	select	Europe

I also made the following changes to switch from the default British
English to American English:

.. code-block:: shell

   keyboard-configuration keyboard-configuration/xkb-keymap select us
   keyboard-configuration keyboard-configuration/fvariant  select  English (US) - English (US\, international with dead keys)

Note that the comment in 00-debconf above the
keyboard-configuration/xkb-keymap line erroneously states that
American English is an option, but it's not. You need to change it
from "gb" to "us" if you want the American layout.

Using the custom image
======================

With all these changes, we can build our new image by running
:shell:`./build-docker.sh` and, if successful, find a .zip file inside
the deploy directory with the image name and date.

To use this image, we unzip the file to extract the .img file inside
it. Next, we need to copy it onto a SD card that will plug into the
pi. I have a SD card reader/writer on my laptop for which I check for
its Linux device name by running :shell:`lsblk` before and after
plugging in the card. (The device that appears in the output of lsblk
after plugging it in is its name, which is **/dev/mmcblk0** on my
laptop). Once I get its device name, I use the Linux :shell:`dd`
command to copy the contents of the image onto the card. (Be sure to
change /dev/mccblk0 to match the name that your system gives to your
SD card device.)

.. code-block:: shell

   sudo dd if=2018-07-21-my_name-lite.img of=/dev/mmcblk0 bs=4096; sync

**Please be EXTREMELY careful that you get the device name right.**
It's not very difficult to write the contents of the image file over
your root partition or other important data.

After writing the image, we can plug the SD card into our pi, boot it
up, and try logging in as alphapi with the random password that was
created in the users file. **Be sure at this point to change your
user's and root's password**. We can also verify that the keyboard was
set to US English by typing Shift-3 and observing whether we get a
hashtag (#) symbol and not the symbol for the British pound currency.

In a follow-up post, I will describe how to setup the network and SSH
so I can continue to setup my Raspberry Pi without ever needing a
terminal.
   
.. _cross-compile a large C++ and Python library: link://slug/how-i-built-a-cross-compilation-workflow-for-the-raspberry-pi
.. _Raspbian: https://www.raspberrypi.org/downloads/raspbian/
.. _pi-gen: https://github.com/RPi-Distro/pi-gen
.. _Learn Think Solve Create: https://learnthinksolvecreate.wordpress.com/category/raspberry-pi/pi-gen/
.. _follow the instructions here: https://docs.docker.com/install/
.. _minimal Raspbian image: https://raspberrypi.stackexchange.com/questions/39932/differences-between-raspbian-jessie-and-raspbian-jessie-lite#39933
.. _adduser man pages: http://manpages.ubuntu.com/manpages/trusty/man8/adduser.8.html
