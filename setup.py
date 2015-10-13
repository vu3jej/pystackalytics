#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

package = 'pystackalytics'

requirements = [
    'requests',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pystackalytics',
    version=get_version(package),
    description="Python wrapper for Mirantis Stackalytics API.",
    long_description=readme + '\n\n' + history,
    author="Jithesh E J",
    author_email='mail@jithesh.net',
    url='https://github.com/vu3jej/pystackalytics',
    packages=[
        'pystackalytics',
    ],
    package_dir={'pystackalytics':
                 'pystackalytics'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pystackalytics',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
