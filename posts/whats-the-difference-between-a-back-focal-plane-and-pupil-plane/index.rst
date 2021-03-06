.. title: What's the difference between a back focal plane and pupil plane?
.. slug: whats-the-difference-between-a-back-focal-plane-and-pupil-plane
.. date: 2015-08-26 08:49:13 UTC+02:00
.. tags: optics
.. category: 
.. link: 
.. description: Exploring the difference between two important planes that help to characterize a microscope.
.. type: text

Yesterday in the lab I asked one of my colleagues whether she knew
what the pupil plane of a microscope objective was. Her answer was
no. I then unknowingly proceeded to give her a description which I now
realize was false. I said that the pupil plane is the plane near the
backside of the objective where the light intensity is proportional to
the Fourier transform of the image. Later that evening, I realized
that this explanation was, in fact, wrong. I had described to her what
is the /back focal plane/ for an infinity-corrected objective.

Don't worry, I will correct myself when I see her later
today. However, this experience does raise one important question that
I have never seriously considered in optics: what is the meaningful
difference between the pupil plane of an optical system and its back
focal plane?

First, I should point out that there is no difference between a /back/
focal plane and one of the two focal planes of an objective; these are
merely semantics that reflect the fact that we think of the sample as
being in front of the objective. The back focal plane is therefore the
focal plane of the objective located on the side opposite the
sample. Now, everyone who has taken a Fourier optics class has
probably learned the following mantra:

  **The focal plane of a lens contains the Fourier transform of the
  object.**

Of course, this statement is usually what we remember, but in fact it
should look more like this:

  **The focal plane of a lens contains the Fourier transform of the
  object, except for every other detail we ignore in the math.**

While it's true that the light intensity here reflects the sample's two-dimensional Fourier
transform, the general case often contains additional phase factors and expressions to account for
the pupil size and apodization (see `Goodman`_, section 5.2). Regardless, it is in the back focal
plane where the light intensity cpontains information on the angular spectrum that makes up the
object.

In contrast, the pupil plane contains either the image of the objective's aperture stop or the
physical stop itself, depending on what sets the limit on the numerical aperture of the objective
in the infinity space (again, see `Goodman`_, appendix B). Moreover, the pupil plane is also used
as the reference plane for quantifying the objective's aberrations. This is because, for a
diffraction-limited system, the wavefront in the (exit) pupil plane will be a spherical wave
converging towards the image of a point source and truncated by the aperture stop `Goodman`_ again
discusses this in section 6.1). Deviations from the spherical reference wave serve as the means to
quantify the aberrations in a system.

From an experimental point of view, the back focal plane is interesting because it is used in
Fourier microscopy, for which many setups have been devised to image it (see Figure 1 in `this
excellent arXiv submission`_.) What I really am wondering now is how one would go about imaging the
pupil plane as a means of exploring an objective's aberrations, and whether this is at all
feasible.

.. _Goodman: https://books.google.ch/books?id=ow5xs_Rtt9AC&printsec=frontcover&dq=goodman+fourier+optics&hl=en&sa=X&ved=0CB0Q6AEwAGoVChMI-5vjt5jGxwIVCMUUCh37ogzP#v=onepage&q=goodman%20fourier%20optics&f=false
.. _this excellent arXiv submission: http://arxiv.org/abs/1507.04037
