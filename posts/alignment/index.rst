.. title: The art of alignment
.. slug: alignment
.. date: 01-27-2014
.. tags: optics 
.. link:
.. description: What's general about aligning optical systems?
.. type: text

I've been working on realigning one of our STORM microscopy setups and moving the other over the
past couple weeks. As a result, I've been doing a lot more alignment lately than I normally do,
which has got me thinking about alignment in general.

I've worked in optics labs for nearly ten years now, but I was never systematically taught how to
do alignments. Eventually, I just figured it out from asking and watching lots of others do
it. This part of experimental optics seems to be something that's passed down and shared across
generations of PhD students and post-docs, like some sort of cultural heritage preserved by spoken
word.

Unfortunately, this fact means that written tutorials or alternative resources on alignment are
scarce. This in turn leads to frustration for new students who can't easily find someone to show
them how to align a system. I was lucky in my training because both my undergraduate and graduate
programs were in centers dedicated to the study of optics and optical engineering. Resources were
plentiful. But for a biologist working with a custom microscope using multiple laser lines, finding
someone who is competent in optics to help realign their system can be highly unlikely.

So how can people who don't have a background in optics be trained in alignment? I'm certain that
written tutorials are *not* the best tool, since aligning an optics setup is a very hands-on
job. But, a tutorial that makes explicit the principles of alignment might make a good starting
point for others.

What are these principles? Below is my rough, initial list that applies to aligning lasner
beams. Aligning incoherent systems is another beast altogether.

1. The angle of the beam propagation is just as important as the position of the beam in a plane
   perpendicular to the table. In other words, just because a beam is going through a stopped-down
   iris doesn't mean it's traveling where you think it is.
2. You need to measure the beam position in two planes to determine its angle of propagation.
3. Use "layers of abstraction" to divide sections of the setup into independent units.
4. Use paired mirrors to get enough degrees of freedom to establish these abstraction layers.
5. Design feedback mechanisms into the system. In other words, keep some irises or alignment marks
   on the walls in place to aid in future realignments.
