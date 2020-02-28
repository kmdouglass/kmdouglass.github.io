.. title: Out of the Tar Pit: a Summary
.. slug: summary-out-of-the-tar-pit
.. date: 2020-02-28 23:40:18 UTC+01:00
.. tags: literature summary
.. category: computer science
.. link: 
.. description: A summary of the paper "Out of the Tar Pit"
.. type: text

`Out of the Tar Pit`_ is a 2006 paper by Ben Moseley and Peter Marks about the causes and effects
of complexity in software systems. The thesis of the paper is stated already in the second sentence
of the paper:

  The biggest problem in the development and maintenance of large-scale software systems is
  complexity — large systems are hard to understand.

As implied by the authors, complexity is a property of a software system that represents the degree
of difficulty that is experienced when trying to understand the system. State—in particular mutable
state—is the primary cause of complexity. Additional causes are code volume and control flow, but
these are of secondary importance.

Complexity
==========

Of the four properties described by Brooks in the paper entitled `No Silver Bullet`_ that make
building software hard (complexity, conformity, changeability, invisibility), the authors state
that complexity is the only meaningful one:

  Complexity is the root cause of the vast majority of problems with software today. Unreliability,
  late delivery, lack of security — often even poor performance in large-scale systems can all be
  seen as deriving ultimately from unmanageable complexity.

By complexity, the authors mean "that which makes large systems *hard to understand*," not the
field of computer science that is concerned with the resources that are consumed by an algorithm.

Approaches to Understanding
===========================

To better establish their definition of complexity, the authors explore the ways in which
developers attempt to understand a system. There are two main ways:

1. **Testing** This is a way to understand the system from the outside.
2. **Informal Reasoning** This is a way to understand the system from the inside.

  Of the two, informal reasoning is the most important by far. This is because — as we shall see
  below — there are inherent limits to what can be achieved by testing, and because informal
  reasoning (by virtue of being an inherent part of the development process) is always used.  The
  other justification is that improvements in informal reasoning will lead to less errors being
  created whilst all that improvements in testing can do is to lead to more errors being detected.

The primary problem with testing is that a test will only tell you about the behavior of a system
subject to the particular range of inputs used by the test. A test will tell you absolutely nothing
about the system's behavior under a different set of inputs. In large systems, the set of all
possible inputs is too large to fully explore with testing.

  Have you performed the right tests? The only certain answer you will ever get to this question is
  an answer in the negative — when the system breaks.

Informal reasoning, on the other hand, is what is used when a developer builds a mental model about
how the system works while looking at the code. Because it is the most important way to understand
a system, simplicity is a vital characteristic of well-functioning, large-scale systems.

Causes of Complexity
====================

State
-----

The presence of state (particularly mutable state) makes programs difficult to understand. The
authors offer the following example to explain the problems of state:

  Anyone who has ever telephoned a support desk for a software system and been told to “try it
  again”, or “reload the document”, or “restart the program”, or “reboot your computer” or
  “re-install the program” or even “re-install the operating system and then the program” has
  direct experience of the problems that state causes for writing reliable, understandable
  software.

State makes testing difficult by making flakiness more likely. (Flakiness describes a set of tests
that randomly fail for seemingly no reason.) This fact, combined with the large number of inputs to
a program, combine together *horribly* (emphasis the authors).

In addition, state complicates informal reasoning by hindering the developer from understanding the
system "from the inside." It contaminates a system in the sense that even mostly stateless systems
become difficult to understand when coupled to components with mutable state.

Control
-------

The authors claim that the next most important barrier to understanding is control.

  Control is basically about the order in which things happen. The problem with control is that
  very often we do not want to have to be concerned with this.

Complexity caused by control very much depends on the choice of language; some languages make
control flow explicit, whereas other, more declarative languages, make control flow
implicit. Having to explicitly deal with control creates complexity.

The same is true of concurrency. Explicit concurrency in particular makes both testing and informal
reasoning about programs hard.

Code volume
-----------

Increasing the amount of code does increase complexity, but effective management of state and
control marginalizes its impact.

There are indeed other causes of complexity than the three listed above, but they all reduce to
three basic principles:

1. Complexity breeds complexity
2. Simplicity is *hard*
3. Power corrupts

The last principle states that mistakes and poor decisions *will be made* when a language allows
it. For this reason, restrictive, declarative languages and tools should be preferred.

Classical approaches to managing complexity
===========================================

To better understand the ways in which programmers manage complexity, the authors explore three
major styles of programming:

1. Imperative (more precisely, object-oriented)
2. Functional
3. Logic

Object-orientation
------------------

Object-oriented programming (OOP) is one of the most dominant styles of programming today for
computers that are based on the von Neumann architecture and is presumably inspired largely by its
state-based form of computation.

OOP enforces integrity constraints on data by combining an object's state with a set of procedures
to access and modify it. This characteristic is known as *encapsulation*. Problems may arise when
multiple procedures contend for access to the same state.

OOP also views objects as being uniquely identifiable, regardless of the object's attributes. In
other words, two objects with the exact same set of attributes and values are condsidered
distinct. This property is known as *intensional identity* and contrasts with *extensional
identity* in which things are considered the same if their attributes are the same.

For these two reasons, OOP is not suitable for avoiding the problems of complexity:

  The bottom line is that all forms of OOP rely on state (contained within objects) and in general
  all behaviour is affected by this state. As a result of this, OOP suffers directly from the
  problems associated with state described above, and as such we believe that it does not provide
  an adequate foundation for avoiding complexity.

Functional programming
----------------------

Modern functional programming (FP) languages can be classified as pure (e.g. Haskell) and impure
(e.g. the ML family of languages).

  The primary strength of functional programming is that by avoiding state (and side-effects) the
  entire system gains the property of *referential transparency* - which implies that when supplied
  with a given set of arguments a function will always return exactly the same result (speaking
  loosely we could say that it will always behave in the same way)...

  It is this cast iron guarantee of *referential transparency* that obliterates one of the two
  crucial weaknesses of testing as discussed above. As a result, even though the other weakness of
  testing remains (testing for one set of inputs says nothing at all about behaviour with another
  set of inputs), testing does become far more effective if a system has been developed in a
  functional style.

Informal reasoning is also more effective in the functional approach to programming. By enforcing
*referential transparency*, mutable state is generally avoided. However, in spite of its
properties, nothing in FP can prevent somenone from effectively simulating multiple state, so some
care must still be taken.

The authors concede that by sacrificing state in FP, one does lose a degree of modularity.

  Working within a stateful framework it is possible to add state to any component without
  adjusting the components which invoke it. Working within a functional framework the same effect
  can only be achieved by adjusting every single component that invokes it to carry the additional
  information around.

However,

  The trade-off is between complexity (with the ability to take a shortcut when making some
  specific types of change) and simplicity (with huge improvements in both testing and
  reasoning). As with the discipline of (static) typing, it is trading a one-off up-front cost for
  continuing future gains and safety (“one-off” because each piece of code is written once but is
  read, reasoned about and tested on a continuing basis).

FP remains relatively unpopular despite its advantages. The authors state that the reason is that
problems arise when programmers attempt to use it in problems that require mutable state.

Logic programming
-----------------

Logic programming is like FP in the sense that it is declarative: it emphasizes what needs to be
done, not how it is done. The primary example of a logic programming language is Prolog.

  Pure logic programming is the approach of doing nothing more than making statements about the
  problem (and desired solutions). This is done by stating a set of axioms which describe the
  problem and the attributes required of something for it to be considered a solution. The ideal of
  logic programming is that there should be an infrastructure which can take the raw axioms and use
  them to find or check solutions. All solutions are formal logical consequences of the axioms
  supplied, and “running” the system is equivalent to the construction of a formal proof of each
  solution.

Pure logic programming does not suffer from the same problems of state and control as OOP. However,
it appears that real logic programming languages need to make some pragmatic tradeoffs in their
implementations which introducs small amounts of state and control elements.

Accidents and Essence
=====================

The authors define two different types of complexity:

- **Essential complexity** is inherent in, and the essence of, the problem as seen by the user.
- **Accidental complexity** is all the rest - complexity with which the development team would not
  have to deal with in the real world.

It is important to understand the degree of strictness in the definition of essential
complexity. Only complexity related to the problem domain of the user falls into this
category. Everything related to the implementation details - bytes, transistors, operating systems,
programming languages, etc. - is accidental complexity.

  We hence see essential complexity as "the complexity with which the team will have to be
  concerned, even in the ideal world"... Note that the "have to" part of this observation is
  critical — if there is any possible way that the team could produce a system that the users will
  consider correct without having to be concerned with a given type of complexity then that
  complexity is not essential.

The authors disagree with Brooks's assertion that most complexity in software is essential.

  Complexity itself is not an inherent (or essential) property of software (it is perfectly
  possible to write software which is simple and yet is still software), and further, much
  complexity that we do see in existing software is not essential (to the problem).

Recommended general approach
============================

The remaining sections of the paper present the authors' idea on a model system that minimizes the
effects of complexity. First, they present the solution in the ideal world, and then adjust this
solution accordingly to handle real world constraints.

Ideal world
-----------

The implementation of a complexity-minimizing system in the ideal world is not concerned with
performance, and the language and infrastructure provides all the support necessary to build the
system.

The purpose of designing the system is to translate users' informal requirements into formal
requirements.

.. math::

   \text{Informal requirements} \rightarrow \text{Formal requirements}

(Note that I believe that, today, this mapping is most often done as part of the Agile workflow,
not through a formal analysis method.) In the ideal world, this translation must not introduce any
accidental complexity, and, as a result, should not include any details about execution
what-so-ever.

  The sole concern when producing the formal requirements must be to ensure that there is no
  relevant ambiguity in the informal requirements (i.e. that it has no omissions).

Once the design process has finished, it should suffice to simply execute the system in the ideal
world.

Such a system as described above obtains its data either as inputs or by deriving it from
inputs. All data derived from the user requirements is essential, but not all such data corresponds
to *essential state*. The reason is that some derived data need not be stored but, rather,
calculated only as needed.

Only essential input data corresponds to essential state. All other data is part of accidental
state, including:

- derived, immutable, essential data
- derived, mutable, essential data
- and derived accidental data.

Control in the ideal world is entirely accidental; it is not something that programmer's should be
concerned with (in the ideal world!) because it does not pertain to the users' problem.

Required Accidental Complexity
------------------------------

Once we move into the real world, we will find that we must allow for some accidental
complexity. The reasons for justifying it are

- Performance
- Ease of expression

Given that we must allow for some accidental complexity, the authors suggest the following strategy
to address it:

- Avoid
- Separate

The overriding aim must be to avoid accidental complexity and, when it is necessary, separate it
from the rest of the system to the greatest degree possible.

Functional relational programming
=================================

The second part of the paper concerns itself with exploring a real-world implementation of a
complexity-minimizing system known as *functional relational programming*, or FRP. It is based on
two major paradigms:

- the relational data model for handling state
- pure functional programming for handling logic

Throughout these final sections, the role of the relational model was the primary topic, whereas
the role of functional programming within the system was given relatively little importance. I
found a few points interesting here:

1. The authors focus primarily on the pure form of the relational model, citing `a work of Codd's`_
   that criticizes "impure" but pragmatic implementations, such as SQL. However, and as far as I
   can tell, there are extremely few real-world implementations of a pure relational database. (I
   only managed to find one, `RelDB`_, from `a page explaining why and how`_ SQL does not strictly
   follow the relational model.)
2. In spite of the paper's insistence on the elimination of mutable state, it seems like the
   authors ignore the point that their implementation of essential state using the relational model
   is mutable. I know of no way that FRP can update the relational variables in the system's
   essential state without mutating them.

The following quotes indicate that the authors seem to understand that their system is based on
mutable state, which is why I am puzzled that it is part of their proposed solution.

  Specifically, all input must be converted into relational assignments (which replace the old
  relvar values in the essential state with new ones), and all output (and side-effects) must be
  driven from changes to the values of relvars (primarily derived relvars). - Section 9.1.4

  Finally, the ability to access arbitrary historical relvar values would obviously be a useful
  extension in some scenarios. - Section 9.1.5

I was actually a bit relieved when a colleague pointed out to me that Rich Hickey expresses similar
criticism about FRP in his talk `Deconstructing the Database`_ because it gave me some confidence
that my suspicions may be correct.

Summary
=======

"Out of the Tar Pit" has significantly changed the way I think about solving problems with software
engineering. In particular, it has made me reevaluate the signifance of domain specific languages
(DSLs), especially those that constrain the freedom of the programmer to work only within the
problem's immediate domain. I am much more suspect of the tendency of programmers to focus on the
flow of control in a program, and I now go to great lengths to avoid mutable state in my own work.

I invested the most thought in the final sections of the paper, only to conclude that their
content, in my opinion, is somewhat incomplete. Though the relational model is indeed powerful and
elegant, it has very few pure, real-world implementations and seems to admit mutable state. This
last bit I find difficult to reconcile with the main thesis of the paper, which is that mutable
state is the primary cause of complexity in systems.

I described "Out of the Tar Pit" to my former manager as one of those papers where if you read it,
you can't help but agree with it's message because it puts into words what you already know by
heart. He replied that this is true only if you've worked in programming for long enough to suffer
from the effects of unmanageable complexity. Otherwise, you have no idea what the authors are
talking about.

.. _Out of the Tar Pit: http://curtclifton.net/papers/MoseleyMarks06a.pdf
.. _No Silver Bullet: https://en.wikipedia.org/wiki/No_Silver_Bullet
.. _a work of Codd's: https://dl.acm.org/doi/10.5555/77708.C1065772
.. _RelDB: https://reldb.org/c/
.. _a page explaining why and how: https://www.sisense.com/blog/your-database-isnt-really-relational/
.. _Deconstructing the Database: https://www.youtube.com/watch?v=Cym4TZwTCNU
