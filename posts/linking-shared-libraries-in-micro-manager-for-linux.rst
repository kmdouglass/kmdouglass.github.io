.. title: Linking shared libraries in Micro-Manager for Linux
.. slug: linking-shared-libraries-in-micro-manager-for-linux
.. date: 2019-01-19 12:00:37 UTC+01:00
.. tags: micro-manager
.. category: embedded microscopy
.. link: 
.. description: Here I describe how to link shared libraries in Micro-Manager device adapters.
.. type: text

Lately I have been working on a new `Video4Linux2 device adapter`_ for `Micro-Manager`_. I
encountered the following error after adding some functionality that introduced two `Boost
libraries`_ as new dependencies in my project.

.. code-block:: shell

   Traceback (most recent call last):
     File "RPiV4L2.py", line 17, in <module>
       mmc.loadDevice("camera", "RPiV4L2", "RPiV4L2")
     File "/home/micro-manager/app/lib/micro-manager/MMCorePy.py", line 3515, in loadDevice
       return _MMCorePy.CMMCore_loadDevice(self, label, moduleName, deviceName)
   MMCorePy.CMMError: Failed to load device "RPiV4L2" from adapter module "RPiV4L2" [ Failed to load device adapter "RPiV4L2" [ Failed to load module "/home/micro-manager/app/lib/micro-manager/libmmgr_dal_RPiV4L2.so.0" [ /home/micro-manager/app/lib/micro-manager/libmmgr_dal_RPiV4L2.so.0: undefined symbol: _ZN5boost10filesystem6detail13dir_itr_closeERPvS3_ ] ] ]

I received this error when I tried to load the device in a Python script. At first I was puzzled
because the code compiled without problems, but I soon found that the solution was simple.

The key part of the message is ``undefined symbol:
_ZN5boost10filesystem6detail13dir_itr_closeERPvS3_``. To troubleshoot this, I first demangled the
symbol name by entering it at https://demangler.com/. I discovered that the symbol was referring to
the function ``boost::filesystem::detail::dir_itr_close(void*&, void*&)``. I had added both the
Boost filesystem and Boost regex libraries to this device adapter as dependencies, so it was not
surprising that either of their names appeared in the error message.

Next, I used the `ldd`_ program to check which libraries my device adapter were linked
against. (libmmgr_dal_RPiV4l2.so.0 is the name of the device adapter library file).

.. code-block:: shell

   $ ldd libmmgr_dal_RPiV4L2.so.0 
        linux-vdso.so.1 (0x7ec21000)
        libdl.so.2 => /lib/arm-linux-gnueabihf/libdl.so.2 (0x76e9c000)
        libstdc++.so.6 => /usr/lib/arm-linux-gnueabihf/libstdc++.so.6 (0x76d54000)
        libm.so.6 => /lib/arm-linux-gnueabihf/libm.so.6 (0x76cdc000)
        libc.so.6 => /lib/arm-linux-gnueabihf/libc.so.6 (0x76bee000)
        libgcc_s.so.1 => /lib/arm-linux-gnueabihf/libgcc_s.so.1 (0x76bc1000)
        libicudata.so.57 => /usr/lib/arm-linux-gnueabihf/libicudata.so.57 (0x75334000)
        libicui18n.so.57 => /usr/lib/arm-linux-gnueabihf/libicui18n.so.57 (0x75187000)
        libicuuc.so.57 => /usr/lib/arm-linux-gnueabihf/libicuuc.so.57 (0x7505e000)
        librt.so.1 => /lib/arm-linux-gnueabihf/librt.so.1 (0x75048000)
        libpthread.so.0 => /lib/arm-linux-gnueabihf/libpthread.so.0 (0x75024000)
        /lib/ld-linux-armhf.so.3 (0x76fb4000)

Neither libboost_filesystem nor libboost_regex are listed, so I knew that they were not linked with
the device adapter.

There is a Makefile.am included in the directory of every device adapter in the Micro-Manager
project. This file is used by Autotools define how the device adapter should be compiled and
linked. Here is what my Makefile.am looked like:

.. code-block:: Makefile
   :linenos:

   AM_CXXFLAGS = $(MMDEVAPI_CXXFLAGS)
   deviceadapter_LTLIBRARIES = libmmgr_dal_RPiV4L2.la
   libmmgr_dal_RPiV4L2_la_SOURCES = RPiV4L2.cpp RPiV4L2.h refactor.h ../../MMDevice/MMDevice.h ../../MMDevice/DeviceBase.h
   libmmgr_dal_RPiV4L2_la_LIBADD = $(MMDEVAPI_LIBADD)
   libmmgr_dal_RPiV4L2_la_LDFLAGS = $(MMDEVAPI_LDFLAGS)

After experimenting a bit, I discovered that I could instruct the linker to link against shared
libraries by adding them to the ``libmmgr_dal_RPiV4L2_la_LDFLAGS`` variable with the ``-l``
flag. The resulting line now looks like:

.. code-block:: Makefile

   libmmgr_dal_RPiV4L2_la_LDFLAGS = $(MMDEVAPI_LDFLAGS) -lboost_regex -lboost_filesystem

Finally, running ``ldd`` on the rebuilt device adapter now shows these two libraries:

.. code-block:: shell

   $ ldd libmmgr_dal_RPiV4L2.so.0 
        linux-vdso.so.1 (0x7ed74000)
        libboost_regex.so.1.62.0 => /usr/lib/arm-linux-gnueabihf/libboost_regex.so.1.62.0 (0x76e3c000)
        libboost_filesystem.so.1.62.0 => /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so.1.62.0 (0x76e1b000)
	...
   
.. _`Video4Linux2 device adapter`: https://github.com/kmdouglass/RPi-DeviceAdapters
.. _`Micro-Manager`: https://micro-manager.org/
.. _`Boost libraries`: https://www.boost.org/
.. _`ldd`: http://man7.org/linux/man-pages/man1/ldd.1.html
