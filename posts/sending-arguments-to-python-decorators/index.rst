.. title: Sending arguments to Python decorators
.. slug: sending-arguments-to-python-decorators
.. date: 2015-01-24 08:45:38 UTC+01:00
.. tags: python
.. link: 
.. description: Understanding when arguments are passed to decorated functions. 
.. type: text

`Python's decorators <http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/>`_
are tools for changing the behavior of a function without completely recoding it. When we apply a
decorator to a function, we say that the function has been decorated. Strictly speaking, when we
decorate a function, we send it to a wrapper that returns another function. It's as simple as that.

I was having trouble understanding exactly to which function, the original or the decorated one,
the arguments are sent in a Python decorated function call. I wrote the following script to better
understand this process (I use Python 3.4):

.. code-block:: python
		
   def wrapper(inFunction):
       def outFunction(**kwargs):
           print('The input arguments were:')
           for key, value in kwargs.items():
               print('%r : %r' % (key, value))

           # Return the original function
           return inFunction(**kwargs)

       return outFunction

   def add(x = 1, y = 2):
       return x + y

`wrapper(inFunction)` is a function that accepts another function as an argument. It returns a
function that simply prints the keyword arguments of `inFunction()`, and calls `inFunction()` like
normal.

To decorate the function `add(x = 1, y = 2)` so that its arguments are printed without recoding it,
we normally would place `@wrapper` before its definition. However, let's make the decorator in a
way that's closer to how `@` works under the hood:

.. code-block:: shell

   In [22]: decoratedAdd = wrapper(add)
   In [23]: decoratedAdd(x = 1, y = 24)
   The input arguments were:
   'y' : 24
   'x' : 1
   Out[23]: 25

When we call `decoratedAdd(x = 1, y = 24)`, the arguments are printed to the screen and we still
get the same functionality of `add()`. What I wanted to know was this: are the keyword arguments x
= 1, y = 24 bound in the namespace of `wrapper()` or in the namespace of `outFunction()`? *In
otherwords, does wrapper() at any point know what the arguments are that I send to the decorated
function?*

The answer, as it turns out, is no in this case. This is because the `wrapper()` function first
returns the decorated function, and then the arguments are passed into the decorated function. If
this order of operations were flipped, `wrapper()` should know that I set x to 1 and y to 24, but
really it doesn't know these details at all.

.. code-block:: shell

   In [24]: wrapper(add)(x = 1, y = 24)
   The input arguments were:
   'y' : 24
   'x' : 1
   Out[24]: 25

So, when I call `wrapper(add)(x = 1, y = 24)`, first `wrapper(add)` is called, which returns
`outFunction()`, and then these arguments are passed to `outFunction()`.

Now what happens when I call `wrapper(add(x = 1, y = 24))`? When I try this, the arguments are
first passed into add, but then `outFunction` is returned without any arguments applied to it.

This example can give us an idea about the working order of operations in Python. Here, this
example reveals that function calls in Python are left-associative.

