#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from setuptools import setup, find_packages


# Variables ===================================================================
changelog = open('CHANGES.rst').read()
long_description = "\n\n".join([
    open('README.rst').read(),
    changelog
])


# Functions ===================================================================
def allSame(s):
    return not filter(lambda x: x != s[0], s)


def hasDigit(s):
    return any(map(lambda x: x.isdigit(), s))


def getVersion(data):
    data = data.splitlines()
    return filter(
        lambda (x, y):
            len(x) == len(y) and allSame(y) and hasDigit(x) and "." in x,
        zip(data, data[1:])
    )[0][0]


# Actual setup definition =====================================================
setup(
    name='napoleon2html',
    version=getVersion(changelog),
    description='Functions to translate sphinx to HTML.',
    long_description=long_description,
    url='https://github.com/Bystroushaak/napoleon2html',

    author='Bystroushaak',
    author_email='bystrousak@kitakitsune.org',

    classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ],
    license='MIT',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=True,

    install_requires=open("requirements.txt").read().splitlines(),

    extras_require={
        "docs": [
            "sphinx",
            "sphinxcontrib-napoleon",
        ]
    },
)
