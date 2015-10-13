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
        
All methods support common set of parameters that allow to filter resulting data.

.. csv-table::
    :header: "Parameter", "Description"
    :widths: 20, 50

    "release", "Name of OpenStack release or ‘all’, by default current release"
    "project_type", "Type of project, by default ‘openstack’"
    "module", "Name of module (repository name)"
    "company", "Company name"
    "user_id", "Launchpad id of user or email if no Launchpad id is mapped."
    "metric", "Metric: e.g. ‘commits’, ‘loc’, ‘marks’, ‘emails’"
    "start_date", "When the period starts"
    "end_date", "When the period ends"

Features
--------

* TODO
