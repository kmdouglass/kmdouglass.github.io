.. title: Beware the paraxial approximation in microscopy
.. slug: beware-the-paraxial-approximation-in-microscopy
.. date: 2015-09-09 19:40:00 UTC+02:00
.. tags: optics, microscopy
.. category: 
.. link: 
.. description: The paraxial approximation can cause conceptual problems when modeling microscopes.
.. type: text


I have had a difficult time resolving what originally seemed to be an inconsistency between a 2004
research article about estimating microscope pupil functions and the body of knowledge concerning
the theory of aberrations in optical systems.

In the article by Hanser, et al.[1], the authors utilize an imaging model for calculating the
amplitude point-spread function of an optical system that incorporates defocus as an exponential
term inside the Fourier transform integral:

.. math::

   \text{PSF}_{\text{A}} \left( x, y, z \right) = \iint_{pupil} P \left( k_x, k_y \right) e^{i k_z z} e^{i \left( k_{x}x + k_{y}y \right)} dk_x dk_y

where :math:`k_z = \sqrt{\left( 2 \pi n / \lambda \right)^2 - \left( k_x^2 + k_y^2 \right)}`. (I
changed the notation of some variables used in the text because the authors confusingly use
:math:`k` to represent spatial frequency in units of /cycles per distance/ instead of the much more
common *radians per distance*.) In the image plane at :math:`z = 0`, there is no defocus and we get
the amplitude point spread function (PSF) as the Fourier transform of the pupil function :math:`P
\left( k_x, k_y \right)` just like we would expect (see Goodman[2], Chapter 6, pp. 129-131).

The problem arises when I try to verify this model when :math:`z` is not equal to zero by computing
the defocused PSF using the wavefront error for defocus. From the scalar diffraction theory of
aberrations, the defocused PSF is the Fourier transform of the pupil function multiplied by a phase
factor whose phase angle is proportional to the wavefront error :math:`W \left( k_x, k_y \right)`

.. math::

   \text{PSF}_{\text{A}} \left( x, y, z \right) = \iint_{pupil} P \left( k_x, k_y \right) e^{i k W \left( k_x, k_y \right)} e^{i \left( k_{x}x + k_{y}y \right)} dk_x dk_y

Any textbook discussing Seidel aberrations will tell you that the defocused wavefront error
:math:`W` is quadratic in the pupil plane coordinates, i.e. :math:`W \sim k_x^2 + k_y^2`. Goodman
even states this with little justification later in Chapter 6 on p. 149 when discussing defocus
[2]. So how can I reconcile the first equation in which the defocus goes as the square root of a
constant minus the squared pupil coordinates with the second equation that is quadratic in pupil
coordinates?

The answer, as you might have guessed from the title of this post, is that /the Seidel polynomial
term for defocus is a result of applying the paraxial approximation when computing the wavefront
error/. You can see this by calculating the phase of a spherical wave in the pupil plane that is
centered on the axis in the image plane; Goodman states it is quadratic without justification, but
this is only true near the axis. Mahajan offers a geometrical interpretation of :math:`W`
on p. 148, where he notes that the path length difference for defocus "is approximately equal to
the difference of `sags <http://liutaiomottola.com/formulae/sag.htm>`_ of the reference sphere and
the wavefront.[3]" He then goes on to derive the same expression for :math:`W` that Goodman gets;
he states the approximation that he uses, whereas Goodman implicitly assumes a quadratic phase
front in the pupil. Hanser et al., on the other hand, are essentially propagating the plane wave
angular spectrum from the image plane to nearby planes to model defocus. I think that this should
be rigorously correct since no approximation is applied. For me, it is unfortunate that this was
not made clear in their paper because I spent quite a bit of time trying to reconcile the two
results.

The lesson of this story is to be sure you know about the approximations that go into a "standard"
result found in textbooks. I falsely assumed that the Seidel aberrations were exact and that
Hanser, et al. were suspect when in fact it was the other way around. Because the paraxial
approximation is so widespread in optics theory, it can often lie hidden behind an equation and its
effects can easily be taken for granted. This is a problem for the large NA systems used in
microscopy where the results of the paraxial approximation are not often valid.

Footnotes
=========

1. http://onlinelibrary.wiley.com/doi/10.1111/j.0022-2720.2004.01393.x/abstract;jsessionid=946CF30FA7FA65F1DB4C638D0C4DF00F.f02t04
2. https://books.google.ch/books/about/Introduction_to_Fourier_optics.html?id=ow5xs_Rtt9AC&redir_esc=y
3. https://books.google.ch/books/about/Optical_Imaging_and_Aberrations_Ray_geom.html?id=I_1AAQAAIAAJ&redir_esc=y

