#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Copyright © Appknox
#

"""
File name: setup.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-03-11
"""
__author__ = "dhilipsiva"
__status__ = "development"

"""
Installation of android adb libraries borrowed from Chromium project
"""

from setuptools import find_packages, setup


setup(
    name='xysec_adb',
    version='0.2',
    url='https://github.com/xysec/xysec_adb',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    description=(
        'A Collections android adb libraries borrowed from Chromium project'),
    license='Multiple Licenses',
    packages=find_packages(),
    include_package_data=True,
    scripts=[
        # This will contain a list of files that can be called as script
        # from command line. Ex:
        # 'path/to/my_script.py'
    ],
    entry_points={},
    extras_require={
        # Extra requiremnts. Ex:
        # "bcrypt": ["bcrypt"],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: xysec_adb',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Multiple Licenses',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
