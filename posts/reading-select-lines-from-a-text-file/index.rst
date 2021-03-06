.. title: Reading select lines from a text file
.. slug: reading-select-lines-from-a-text-file
.. date: 2015-03-18 08:27:50 UTC+01:00
.. tags: python, micro-manager
.. category: 
.. link: 
.. description: 
.. type: text

`I just created a Python Gist <https://gist.github.com/kmdouglass/507717d339bc82f850ce>`_ for
reading select lines from a text file into memory. I came up with this Gist when I needed to parse
the core log from our `microscope control software (Micro-Manager)
<https://www.micro-manager.org/>`_. One of our devices was continously sending its statistics to
the computer, which would then be recorded to the log. I wanted to find only lines that contained
the statistics by searching for the *STATS* identifier, which was unique to these lines.

The problem was a bit more difficult than reading just the lines containing this string because I
wanted the statistics only for times when the software was acquiring a time series of
images. Luckily, the core log also contains lines with unique strings indicating when a time series
was initiated and stopped. All lines in the log are time-stamped.

Below is the Gist I used to solve this problem. The lines that will be retained in memory will
contain the strings in the list lineFilters. I then define a function named stringIsIn that will
return a list of bool indicating whether each string is present in the line.

At the bottom of the Gist, I use a list comprehension to loop over each line in the file. The line
is appended to a growing list called outputLines if the line contains *any* of the strings I
defined. Note that it's not necessary to use a separate definition for `stringIsIn`; the list
comprehension over lineFilters could have been placed inline with the primary list comprension over
lines in the file. I do think it is more readable the way it is presented below, however.

I welcome any comments or suggestions, especially on the `Gist website
<https://gist.github.com/kmdouglass/507717d339bc82f850ce>`_ where others may be more likely to find
it.

.. code-block:: python

   filename    = 'myFile.txt'
   outputLines = []

   # Keep all lines containing ANY of the following list of strings.
   lineFilters = ['line 1',
                  'line 2',
                  'line 3']
   stringIsIn  = lambda line: [filter in line for filter in lineFilters]


   # Read only lines containing one of the strings into memory.
   with open(filename, 'r') as file:
       [outputLines.append(line) for line in file if any(stringIsIn(line))]
