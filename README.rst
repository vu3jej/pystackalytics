===============================
pystackalytics
===============================

.. image:: https://img.shields.io/travis/vu3jej/pystackalytics.svg
        :target: https://travis-ci.org/vu3jej/pystackalytics

.. image:: https://img.shields.io/pypi/v/pystackalytics.svg
        :target: https://pypi.python.org/pypi/pystackalytics


Python wrapper for Mirantis Stackalytics API.

* Free software: The MIT License
* Documentation: https://pystackalytics.readthedocs.org.

Usage
-----

.. code:: python

        from pystackalytics.pystackalytics import Stackalytics
        api = Stackalytics()
        api.companies(release='kilo').stats[1].name
        # u'Mirantis'

Features
--------

* TODO
