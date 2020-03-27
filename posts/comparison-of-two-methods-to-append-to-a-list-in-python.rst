.. title: Comparison of two methods to append to a list in Python
.. slug: comparison-of-two-methods-to-append-to-a-list-in-python
.. date: 2020-03-27 18:09:00 UTC+01:00
.. tags: python
.. category: 
.. link: 
.. description: Which of two methods for appending items to a list in Python is faster?
.. type: text

.. container:: ABSTRACT

   A colleague recently told me that the ``append`` method on a Python
   list is more efficient than using the += operator but provided no
   justification. Curious, I investigated whether this was true.

String validation as an example
===============================

Consider the following function as an example. It checks whether a
string is *semantically* correct, i.e. whether it satisifies some set of
requirements that are dictated by the needs of the application. In this
example, the requirements are

1. The string cannot be longer than 10 characters
2. The string cannot contain a number

.. code:: python

   import re

   def validate(input: str) -> str:
       reasons = []

       if len(input) > 10:
           reasons += ["Input is too long"]

       if bool(re.search(r"\d", input)):
           reasons += ["Input contains a number"]

       if reasons:
            raise Exception(" | ".join(reasons))

       return input

If either of these conditions are violated, an exception is raised
containing a message. The message describes which condition(s) is(are)
violated. The ``reasons`` list contains zero, one, or two elements, and
it is built by appending to the list using the += operator. I could
have instead used the ``append`` method of ``list``.

+= vs. append
=============

To test the speed of the two methods, I use the ``timeit`` package from
the Python standard library in the program below. The test consists of
the following:

1. Create an empty list
2. Append error strings to the list one at a time

.. code:: python

   import string
   import timeit

   reasons = [
       "This is an error message",
       "This is another error message",
       "Let's add another for good measure",
   ]
   def test_plus_equals():
       result = []
       for reason in reasons:
           result += [reason]

   def test_append():
       result = []
       for reason in reasons:
           result.append(reason)

   number = 1000000
   repeat = 5
   results_plus_equals = min(
       timeit.repeat(
           "test_plus_equals()",
           number=number,
           repeat=repeat,
           setup="from __main__ import test_plus_equals"
       )
   )

   results_append = min(
       timeit.repeat(
           "test_append()",
           number=number,
           repeat=repeat,
           setup="from __main__ import test_append")
   )

   if __name__ == "__main__":
       print("1E+6 loops per test")
       print(f"+= (best of five tests):\t{results_plus_equals:0.4f} s")
       print(f"append (best of five tests):\t{results_append:0.4f} s")

Results
=======

.. code::

   1E+6 loops per test
   += (best of five tests):	0.2392 s
   append (best of five tests):	0.2241 s

In this test the ``append`` method of Python's list does appear to be
faster by a factor of 6% or 7%. ``append`` took about 0.239
microseconds per loop, whereas the += operator took 0.224 microseconds.

The advantage of the ``append`` method is probably only noticeable if
you need to append to a list many millions of times per second.

