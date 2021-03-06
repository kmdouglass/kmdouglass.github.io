.. title: Measurements as processes
.. slug: measurements
.. date: 12-19-2014
.. tags: sensing, super-resolution
.. link:
.. description: Measurements can be thought of as transformations from a structure to a dataset
.. type: text

I work in microscopy, which is one form of optical sensing. In the sensing field, we are often
concerned with making measurements on some structure so as to learn what it is. Often, I think the
word measurement refers to the dataset that's produced.

I think it can be more effective to think of a measurement as a process that transforms the
structure into the dataset. Why is this so? Well, to understand what the original structure was, we
have to look at our data and make an inference. If we understand the steps in the process that took
the original structure and turned it into data, we can apply the inverse of those steps in reverse
order to get the original structure.

Of course, our dataset may only capture some limited aspects of the original structure, so we may
only be able to make probabilistic statements about what the original structure was.

Take, for example, super-resolution microscopy experiments (SR). In SR, some feature of a cell is
labeled with a discrete number of fluorescent molecules, then these molecules are localized to a
high precision. The centroids of all the molecules are then convolved with a Gaussian function (or
something similar) with a width equal to the localization precision to produce a rendered,
super-resolved image of the structure. The measurement process can be thought of like this:

1. Attach fluorescent molecules to every macromolecule (or randomly to a subset of macromolecules)
   in the structure of interest.
2. For every molecule that emits photons during the time of acqusition by one camera frame, record
   its true coordinate positions and the number of detected photons. This can create multiple
   localizations that correspond to the same molecule in multiple camera frames.
3. Remove molecules from the lis that emitted less than some threshold number of photons. These
   correspond to molecules with a signal-to-noise ratio that is too low to be detected.
4. Randomly bump the molecule positions according to a Gaussian distribution with width equal to
   the localization precision in each direction.

This process results in a list of molecule positions that originally were located on the structure
of interest, but were eventually displaced randomly and filtered out due to various sources of
noise. To understand what the original structure was, we have to "undo" each of these steps to the
best of our abilities.

I think it's interesting to note that everytime a random change to the original molecule positions
occurred, we lose some information about the structure.
