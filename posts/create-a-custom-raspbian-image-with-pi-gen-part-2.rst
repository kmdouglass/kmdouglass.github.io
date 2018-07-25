.. title: Create a custom Raspbian image with pi-gen: part 2
.. slug: create-a-custom-raspbian-image-with-pi-gen-part-2
.. date: 2018-07-24 18:25:26 UTC+02:00
.. tags: raspbian, raspberry pi, devops
.. category: raspberry pi
.. link: 
.. description: Part 1 of a tutorial on creating custom Raspbian images with pi-gen.
.. type: text
.. status: published

.. role:: shell(code)
   :language: shell

In my `previous post`_, I discussed how to setup user accounts and
locales in a custom Raspbian image using pi-gen. In this follow-up
post, I will discuss the main problems that I want to solve:
automatically configuring the wireless network and ssh on a new
Raspberry Pi without a terminal attached directly to the Pi.

Set up the wireless network
===========================

The WPA supplicant
------------------

The Pi's wireless credentials are configured in stage 2 in the file
**stage2/02-net-tweaks/files/wpa_supplicant.conf**. Here's how it
looks by default::

  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

According to the blogs `Learn Think Solve Create`_ and the `Raspberry
Spy`_, the first thing we should do is add our country code to the top
of this file with the line `country=CH`. (Use your own country code
for this.) Next, we want to enter the details for our wireless
network, which includes its name and the password. For security
reasons that I hope are obvious, we should not store the password in
this file. Instead, we create a hash of the password and put that
inside the file. The command to create the password hash is

.. code-block:: shell

    wpa_passphrase ESSID PASSWORD > psk

where ESSID is our wireless network's name. Note that I also used a
space before the :shell:`wpa_passphrase` command to prevent the
password being written to my .bash_history file. Now, we copy and
paste the contents of the file **psk** into the wpa_supplicant.conf
and remove the comment that contains the actual password::

  country=CH
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  network={
	  ssid=YOUR_ESSID_HERE
       	  psk=YOUR_PSK_HASH_HERE
  }

Configure the wireless network interfaces
-----------------------------------------

After having configured the supplicant, we next move on to configuring
the network interfaces used by Raspbian. The appropriate file is found
in **stage1/02-net-tweaks/files/interfaces**. In my post `Connecting a
Raspberry Pi to a Home Linux Network`_ I described how to set up the
network interfaces by editing **/etc/network/interfaces**. Much of the
information presented in that post has now been superseded in Raspbian
by the DHCP daemon. For now, we will use the interfaces file to
instruct our Pi to use DHCP and will use **/etc/dhcpcd.conf** at a
later time to set up a static IP address when provisioning the Pi.

We first need to make a few changes to make the interfaces file aware
of the credentials in the wpa supplicant configuration file. According
to the blog `kerneldriver`_, we need modify the
/etc/networe/interfaces file as such::

  auto lo

  iface lo inet loopback
  iface eth0 inet dhcp

  auto wlan0
  iface wlan0 inet manual
       wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
  iface default inet dhcp

In the first modification, I specify that I want the wirless interface
**wlan0** started automatically with `auto wlan0`. Next, I specify
that the wlan0 interface should use the `manual inet address family`_
with the line `iface wlan0 inet manual`.

According to the man pages, "[the manual] method may be used to define
interfaces for which no configuration is done by default." After this
we use the `wpa-roam` command to specify the location of the
wpa_supplicant.conf file that we previously modified. The wireless
ESSID and password are therefore not defined in interfaces, but rather
reference them inside wpa_supplicant.conf.

In case you noticed that wpa-roam doesn't appear as an option in
documentation on the interfaces file and were wondering why, it's
because other programs like wpasupplicant may provide additional
options to the interfaces file. A similar command is `wpa-conf`, but I
do not quite yet understand the difference between these two commands.

Following the wpa-roam command, we configure the default options for
all networks in our wpa_supplicant.conf file with the line `iface
default inet dhcp`. At this point, we save the setup of the static IP
address for a later time.

For more information, see `the interfaces man page for Debian
Stretch`_.

Change the hostname
-------------------

Our Pi's hostname may be changed from the default (raspberrypi) by
modifying the line in **stage1/02-net-tweaks/files/hostname**. See
`RFC 1178`_ for tips on choosing a hostname.

In addition to modifying the hostname file, we need to update
**stage1/02-net-tweaks/00-patches/01-hosts.diff** and change
raspberrypi to the new hostname::

  Index: jessie-stage1/rootfs/etc/hosts
  ===================================================================
  --- jessie-stage1.orig/rootfs/etc/hosts
  +++ jessie-stage1/rootfs/etc/hosts
  @@ -3,3 +3,4 @@
   ff02::1		  ip6-allnodes
   ff02::2		  ip6-allrouters
   
  +127.0.1.1	  NEW_HOSTNAME_HERE

Set the DNS servers
-------------------

DNS servers are configured in
**export-image/02-network/files/resolv.conf**. By default, mine was
already configured to use one of Google's DNS servers (8.8.8.8). I
added a secondary Google DNS address as well::

  nameserver 8.8.8.8
  nameserver 8.8.4.4

Enable SSH
==========

Enabling SSH is simple. Open **stage2/01-sys-tweaks/01-run.sh** and
change the line :shell:`systemctl disable ssh` to :shell:`systemctl
enable ssh`.

(I later learned that we can also enable ssh on a headless pi by
adding an empty file named **ssh** to the boot partition of a standard
Raspbian image. See here for more details:
https://www.raspberrypi.org/documentation/remote-access/ssh/)

Configuring SSH keys (or not)
-----------------------------

I decided after writing much of this tutorial that pi-gen was not
necessarily the best tool for adding my public SSH keys. So long as I
have network access and SSH enabled, I can easily add my keys using
:shell:`ssh-copy-id`. Furthermore, after following this tutorial,
there still remains a lot of setup and customization steps. These can
more easily be performed manually or by server automation tools like
`Fabric`_ or `Ansible`_.

Therefore, I think that at this point we can stop with our
customization of the image with pi-gen and move to a different
tool. We have a basic Raspbian image that is already configured for
our home network and that serves as a starting point for more complete
customization.

Conclusion
==========

This tutorial and my `previous post`_ demonstrated how to create a
custom Raspbian image that is pre-configured for

- our home wireless network
- our locale information
- ssh

Of course, we can do much, much more with pi-gen, but other tools
exist for the purpose of configuring a server. These tutorials at
least allow you to setup a new Raspberry Pi without having to manually
configure its most basic functionality. Happy Pi'ing!

.. _previous post: link://slug/create-a-custom-raspbian-image-with-pi-gen-part-1
.. _Learn Think Solve Create: https://learnthinksolvecreate.wordpress.com/2017/07/25/pi-gen-setting-default-wifi-settings/
.. _Raspberry Spy: https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/
.. _Connecting a Raspberry Pi to a Home Linux Network: link://slug/connecting-a-raspberry-pi-to-a-home-linux-network
.. _kerneldriver: https://kerneldriver.wordpress.com/2012/10/21/configuring-wpa2-using-wpa_supplicant-on-the-raspberry-pi/
.. _manual inet address family: https://manpages.debian.org/stretch/ifupdown/interfaces.5.en.html#The_manual_Method
.. _the interfaces man page for Debian Stretch: https://manpages.debian.org/stretch/ifupdown/interfaces.5.en.html
.. _RFC 1178: https://tools.ietf.org/html/rfc1178
.. _Fabric: http://www.fabfile.org/
.. _Ansible: https://www.ansible.com/
