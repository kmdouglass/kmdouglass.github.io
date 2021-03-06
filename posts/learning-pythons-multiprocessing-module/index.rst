.. title: Learning Python's Multiprocessing Module
.. slug: learning-pythons-multiprocessing-module
.. date: 2014-12-29 18:42:23 UTC+01:00
.. tags: python, computing
.. link: 
.. description: Python's multiprocessing module can be used for parameter sweeps.
.. type: text

I've been doing a bit of programming work lately that would greatly benefit from a speed boost
using parallel/concurrent processing tools. Essentially, I'm doing a `parameter sweep
<http://www.mathworks.com/help/simulink/examples/parallel-simulations-using-parfor-parameter-sweep-in-normal-mode.html>`_
where the values for two different simulation parameters are input into the simulation and allowed
to run with the results being recorded to disk at the end. The point is to find out how the
simulation results vary with the parameter values.

In my current code, a new simulation is initialized with each pair of parameter values inside one
iteration of a for loop; each iteration of the loop is independent of the others. Spreading these
iterations over the 12 cores on my workstation should result in about a 12x decrease in the amount
of time the simulation takes to run.

I've had good success using the `parfor` loop construct in Matlab in the past, but my simulation
was written in Python and I want to learn more about Python's multiprocessing tools, so this post
will explore that module in the context of performing parameter sweeps.

Profile the code first to identify bottlenecks
==============================================

First, I profiled my code to identify where any slowdowns might be occurring in the serial
program. I used a great tutorial at the `Zapier Engineering
<https://zapier.com/engineering/profiling-python-boss/>`_ blog to write a decorator for profiling
the main instance method of my class that was doing most of the work. Surprisingly, I found that a
few numpy methods were taking the most time, namely `norm()` and `cross()`. To address this, I
directly imported the Fortran BLAS `nrm2()` function using scipy's `get_blas_funcs()` function and
hard-coded the cross product in pure Python inside the method; these two steps alone resulted in a
4x decrease in simulation time. I suspect the reason for this was because the overhead of calling
functions on small arrays outweighs the increase in speed using Numpy's optimized C code. I was
normalizing single vectors and taking cross products between two vectors at a time many times
during each loop iteration.

A brief glance at Python's multiprocessing module
=================================================

`PyMOTW <http://pymotw.com/2/multiprocessing/basics.html>`_ has a good, minimal description of the
main aspects of the multiprocessing module. They state that the simplest way to create tasks on
different cores of a machine is to create new `Process` objects with target functions. Each object
is then set to execute by calling its `start()` method.

The basic example from their site looks like this:

.. code-block:: python

   import multiprocessing

   def worker():
       """worker function"""
       print 'Worker'
       return

   if __name__ == '__main__':
       jobs = []
       for i in range(5):
           p = multiprocessing.Process(target=worker)
           jobs.append(p)
           p.start()

In this example, it's important to create the Process instances inside the

.. code-block:: python

   if __name__ == '__main__':

section of the script because child processes import the script where the target function is
contained. Placing the object instantiation in this section prevents an infinite, recursive string
of such instantiations. A workaround to this is to define the function in a different script and
import it into the namespace.

To send arguments to the function (`worker()` in the example above), we can use the `args` keyword
in the Process object instantiation like

.. code-block:: python

   p = multiprocessing.Process(target=worker, args=(i,))

A very important thing to note is that the arguments must be objects that can be pickled using
Python's pickle module. If an argument is a class instance, this means that every attritube of that
class must be pickleable.

An important class in the multiprocessing module is a `Pool`. A `Pool
<https://docs.python.org/3.4/library/multiprocessing.html#multiprocessing.pool.Pool>`_ object
controls a pool of worker processes. Jobs can be submitted to the Pool, which then sends the jobs
to the individual workers.

The `Pool.map()` achieves the same functionality as Matlab's `parfor` construct. This method
essentially applies a function to each element in an iterable and returns the results. For example,
if I wanted to square each number in a list of integers between 0 and 9 and perform the square
operation on multiple processors, I would write a function for squaring an argument, and supply
this function and the list of integers to `Pool.map()`. The code looks like this:

.. code-block:: python
		
   import multiprocessing

   def funSquare(num):
       return num ** 2

   if __name__ == '__main__':
       pool = multiprocessing.Pool()
       results = pool.map(funSquare, range(10))
       print(results)

Design the solution to the problem
==================================

In my parameter sweep, I have two classes: one is an object that I'm simulating and the other acts
as a controller that sends parameters to the structure and collects the results of the
simulation. Everything was written in a serial fashion and I want to change it so the bulk of the
work is performed in parallel.

After the bottlenecks were identified in the serial code, I began thinking about how the the
problem of parameter sweeps could be addressed using the multiprocessing module.

The solution requirements I identified for my parameter sweep are as follows:

1. Accept two values (one for each parameter) from the range of values to test as inputs to the
   simulation.
2. For each pair of values, run the simulation as an independent process.
3. Return the results of the simulation as as a list or Numpy array.

I often choose to return the results as Numpy arrays since I can easily pickle them when saving to
a disk. This may change depending on your specific problem.

Implementation of the solution
==============================

I'll now give a simplified example of how this solution to the parameter sweep can be implemented
using Python's multiprocessing module. I won't use objects like in my real code, but will first
demonstrate an example where `Pool.map()` is applied to a list of numbers.

.. code-block:: python

   import multiprocessing

   def runSimulation(params):
       """This is the main processing function. It will contain whatever
       code should be run on multiple processors.
    
       """
       param1, param2 = params
       # Example computation
       processedData = []
       for ctr in range(1000000):
           processedData.append(param1 * ctr - param2 ** 2)

       return processedData

   if __name__ == '__main__':
       # Define the parameters to test
       param1 = range(100)
       param2 = range(2, 202, 2)

       # Zip the parameters because pool.map() takes only one iterable
       params = zip(param1, param2)
    
       pool = multiprocessing.Pool()
       results = pool.map(runSimulation, params)

This is a rather silly example of a simulation, but I think it illustrates the point nicely. In the
`__main__` portion of the code, I first define two lists for each parameter value that I want to
'simulate.' These parameters are zipped together in this example because `Pool.map()` takes only
one iterable as its argument. The pool is opened using with `multiprocessing.Pool()`.

Most of the work is performed in the function `runSimulation(params)`. It takes a tuple of two
parameters which are unpacked. Then, these parameters are used in the for loop to build a list of
simulated values which is eventually returned.

Returning to the `__main__` section, each simulation is run on a different core of my machine using
the `Pool.map()` function. This applies the function called `runSimulation()` to the values in the
*params* iterable. In other words, it calls the code described in `runSimulation()` with a
different pair of values in params.

All the results are eventually returned in a list in the same order as the parameter iterable. This
means that the first element in the `results` list corresponds to parameters of 0 and 2 in this
example.

Iterables over arbitrary objects
================================

In my real simulation code, I use a class to encapsulate a number of structural parameters and
methods for simulating a polymer model. So long as instances of this class can be `pickled
<https://docs.python.org/3/library/pickle.html>`_, I can use them as the iterable in `Pool.map()`,
not just lists of floating point numbers.

.. code-block:: python
		
   import multiprocessing

   class simObject():
       def __init__(self, params):
           self.param1, self.param2 = params

   def runSimulation(objInstance):
       """This is the main processing function. It will contain whatever
       code should be run on multiple processors.
    
       """
       param1, param2 = objInstance.param1, objInstance.param2
       # Example computation
       processedData = []
       for ctr in range(1000000):
           processedData.append(param1 * ctr - param2 ** 2)

       return processedData

   if __name__ == '__main__':
       # Define the parameters to test
       param1 = range(100)
       param2 = range(2, 202, 2)

       objList = []
       # Create a list of objects to feed into pool.map()
       for p1, p2 in zip(param1, param2):
           objList.append(simObject((p1, p2)))

       pool = multiprocessing.Pool()
       results = pool.map(runSimulation, objList)

Again, this is a silly example, but it demonstrates that lists of objects can be used in the
parameter sweep, allowing for easy parallelization of object-oriented code.

Instead of `runSimulation()`, you may want to apply an instance method to a list in `pool.map()`. A
naïve way to do this is to replace *runSimulation* with with the method name but this too causes
problems. I won't go into the details here, but one solution is to use an instance's `__call__()`
method and pass the object instance into the pool. More details can be found `here
<http://stackoverflow.com/questions/1816958/cant-pickle-type-instancemethod-when-using-pythons-multiprocessing-pool-ma>`_.

Comparing computation times
===========================

The following code makes a rough comparison between computation time for the parallel and serial
versions of `map()`:

.. code-block:: python

   import multiprocessing
   import time

   def runSimulation(params):
       """This is the main processing function. It will contain whatever
       code should be run on multiple processors.
    
       """
       param1, param2 = params
       # Example computation
       processedData = []
       for ctr in range(1000000):
           processedData.append(param1 * ctr - param2 ** 2)

       return processedData

   if __name__ == '__main__':
       # Define the parameters to test
       param1 = range(100)
       param2 = range(2, 202, 2)

       params = zip(param1, param2)

       pool = multiprocessing.Pool()

       # Parallel map
       tic = time.time()
       results = pool.map(runSimulation, params)
       toc = time.time()

       # Serial map
       tic2 = time.time()
       results = map(runSimulation, params)
       toc2 = time.time()

       print('Parallel processing time: %r\nSerial processing time: %r'
             % (toc - tic, toc2 - tic2))

On my machine, `pool.map()` ran in 9.6 seconds, but the serial version took 163.3 seconds. My
laptop has 8 cores, so I would have expected the speedup to be a factor of 8, not a factor
of 16. I'm not sure why it's 16, but I suspect part of the reason is that measuring system time
using the `time.time()` function is not wholly accurate.

Important points
================

I can verify that all the cores are being utilized on my machine while the code is running by using
the `htop <http://hisham.hm/htop/>`_ console program. In some cases, Python modules like Numpy,
scipy, etc. may limit processes in Python to running on only one core on Linux machines, which
defeats the purpose of writing concurrent code in this case. (See for example `this discussion
<http://stackoverflow.com/questions/15639779/what-determines-whether-different-python-processes-are-assigned-to-the-same-or-d/15641148#15641148>`_.)
To fix this, we can import Python's *os* module to reset the task affinity in our code:

.. code-block:: python

   os.system("taskset -p 0xff %d" % os.getpid())

Conclusions
===========

I think that Matlab's `parfor` construct is easier to use because one doesn't have to consider the
nuances of writing concurrent code. So long as each loop iteration is independent of the others,
you simply write a `parfor` instead of `for` and you're set.

In Python, you have to prevent infinite, recursive function calls by placing your code in the
`__main__` section of your script or by placing the function in a different script and importing
it. You also have to be sure that Numpy and other Python modules that use BLAS haven't reset the
core affinity. What you gain over Matlab's implementation is the power of using Python as a general
programming language with a lot of tools for scientific computing. This and the multiprocessing
module is free; you have to have an institute license or pay for Matlab's `Parallel Computing
Toolbox <http://www.mathworks.com/products/parallel-computing/>`_.
