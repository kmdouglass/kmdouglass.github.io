.. title: The basics of virtualenv
.. slug: the-basics-of-virtualenv
.. date: 2015-02-10 07:47:50 UTC+01:00
.. tags: python
.. category: 
.. link: 
.. description: These are the aboslute basics you need to get virtualenv working. 
.. type: text

I use Python 3.4 in most of my data analyses and in some simulations. I like a lot of its features,
like its implementation of generators, maps, and filters. However, much of the software on my
Debian Wheezy system depends on Python 2.7 to run, such as `Mendeley
<http://www.mendeley.com/>`_. (It used to run just fine with Python 3.4, until I ran an automatic
update and that was the end of that.)

To run some Python 2.7 programs, I used to do the following:

.. code-block:: shell

   sudo rm /usr/bin/python 
   sudo ln -s /usr/bin/python2.7 /usr/bin/python 

I know. Ouch. Every single time I needed to run a program that depended on python2.7, I would
delete the symlink in /usr/bin, make a new link to python2.7, and then run my program. When I
needed to give various programs convenient access to python3.4, I would delete the symlink and
create a new one to the newer version.

This was dumb, because there is a convenient Python-based tool that can fix the problem of needing
multiple versions of Python (and libraries!) on the same system. The solution to this problem is
called `virtualenv <https://virtualenv.pypa.io/en/latest/>`_.

There are a lot of descriptions about what virtualenv is on the internet, so I won't bother going
into details here. Instead, I will focus on just the very basics of its setup and use so that I can
have a handy future reference for when I forget how something works and so that others can profit
from what I have learned. Most everything I've done came from `python-guide.org
<http://docs.python-guide.org/en/latest/>`_, so I'm more-or-less putting `what they have already
said <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ into my own words.

To start, I already have Python 2.7 and 3.4 installed on my system. In principle, you do not need
them installed at the system level, but I already have done this so I will start from there. I
first installed pip for Python 2.7 since I only had pip3 on my system to start. I did this because
I want to keep Python 2.7 as my system's default Python environment.

.. code-block:: shell

   sudo apt-get update
   sudo apt-get install python-pip

Once installed, I used it to install virtualenv and `virtualenvwrapper
<https://virtualenvwrapper.readthedocs.org/en/latest>`_. The latter provides some nice features for
working with virtualenv.

.. code-block:: shell

   sudo pip install virtualenv
   sudo pip install virtualenvwrapper

Now, virtualenvwrapper requires an environment variable to tell it where to store the folders for
each virtual environment. This environment variable is called WORKON_HOME. First, I created the
folder it will point to:

.. code-block:: shell

   mkdir ~/Envs

Next, I edited my ~/.bashrc and added the following line:

.. code-block:: shell

   export WORKON_HOME=~/Envs

All of my virtual environment files (except for the Python intepreters) will be stored in this
folder. Finally, I restarted my terminal window so that the environment variable was assigned. You
can check this by typing =echo $WORKON_HOME= in your new terminal window. If it returns the path to
your new environments folder, then you should be fine.

Next, I ran the virtualwrapper setup script. Note that I did not need sudo (in fact, sudo could not
find a command called `source`) and that no output is returned when the script is run.

.. code-block:: shell

   source /usr/local/bin/virtualenvwrapper.sh

Now virtualenvwrapper should be installed, so let's make a virtual environment. We can do this
using the `mkvirtualenv` command, followed by a name for the environment. I will use the name venv
in this example, like Kenneth Reitz did in his guide that I linked above.

.. code-block:: shell
   
   mkvirtualenv venv

To start the new virtual environment, type `workon venv` and note that change in the prompt,
indicating which environment you are in. You now have a fresh Python environment to which you can
add any library you wish. To leave the environment, type `deactivate` into your terminal.

One simple test that you can do to see whether your Python environment really is clean is to run
the Python interpreter from inside your environment and try importing a module that you know is in
your system-wide site packages but not in your virtual environment. For example, inside venv I type
=python= at the terminal prompt and tried importing numpy, which I had not yet installed in venv:

.. code-block:: python

   import numpy

This returned an `ImportError: No module named numpy`. Since I do have numpy installed on my system
but not in this environment, it tells me that the environment is likely clean.

To install new libraries, simply use pip or install them to the folder that was created for this
environment in ~/Env. To delete a virtual environment entirely, use `rmvirtual env`.

Now, how can I specify that I want the virtual environment to use the python3.4 interpreter in a
virtual environment named python3-general? Doing so would solve my original problem. Simply
make a new virtual environment like so:

.. code-block:: python

   mkvirtualenv -p /usr/bin/python3.4 python3-general

Voilà. C'est tout. I hope this helps you get up and running with this great tool!
