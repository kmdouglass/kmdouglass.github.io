.. title: Thoughts from the Swiss Photonics Machine Learning Workshop
.. slug: thoughts-from-the-swiss-photonics-machine-learning-workshop
.. date: 2016-02-04 18:31:32 UTC+01:00
.. tags: machine learning, photonics, Switzerland
.. category: 
.. link: 
.. description: My thoughts from today's Machine Learning Workshop.
.. type: text

Today I attended a `machine learning workshop hosted by Swiss Photonics
<http://www.swissphotonics.net/workshops/workshop-datenbank?2886>`_. The workshop was a small,
day-long series of talks by industry experts in Neuchâtel, Switzerland, not far from Lausanne. I
went to the workshop because a) I don't know much about machine learning and want to know more,
and b) I wanted to connect with people within the Swiss Photonics circle. Most of the talks
concerned deep learning for solving problems in industrial machine vision applications, such as
quality control for the watch-making industry.

Here are the main things I learned, which may or not be correct. I welcome any opinions or
corrections in the comments:

+ The term "learning" is used to mean "teaching a computer to recognize and classify patterns in
  data", such as finding people in images.
+ Learning involves finding patterns in data. Once patterns are idenfitied, a set of them can be
  combined to form a model. A model makes predictions about what future data may look like. This
  means that a model may be used to see whether new data meets our expectations. An example would
  be using pictures of products from a production line and searching for defects, i.e. those
  products that don't fit our classification of "good" products.
+ Learning applications require lots of training data to implement. This is where the primary cost
  of applying learning algorithms comes from.
+ There are three categories of learning: supervised, reinforced, and unsupervised.
+ The value in neural networks is their ability to make decisions in a way that is similar to
  humans. Other classification and decision algorithms work using strict programmatic rules and
  look for user-specified features. Neural networks do not require domain knowledge to establish
  features for a classifier. Their generality is their strength.
+ `Deep learning <https://en.wikipedia.org/wiki/Deep_learning>`_ just refers to really big neural
  networks. Neural networks are not new; recent hardware advances like GPU-based computation and
  the availability of large datasets are what has enabled Deep learning.

I did not hear much discussion about the tradeoffs and downsides to using neural networks or deep
learning, other than that they require large amounts of training data. Notable talks were given by
Reto Wyss of `ViDi <http://www.vidi-systems.com/company/about-us.html>`_ and Virginie Moser of
`http://www.csem.ch/site/ <CSEM>`_. Wyss very eloquently explained why deep learning is useful for
classification. Moser presented an extremely small and light-weight embedded machine vision system
for traffic light control.
