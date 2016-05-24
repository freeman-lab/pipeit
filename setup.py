#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='pipeit',
    version=version,
    description='tiny package for making pipelines in python',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/freeman-lab/pipeit',
    packages=['pipeit'],
    install_requires=required,
    long_description='See ' + 'https://github.com/freeman-lab/pipeit',
    license='MIT'
)
