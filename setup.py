#!/usr/bin/env python

from setuptools import setup

setup(name='genius_trending.py',
        version='1.0.0.2',
        description='Unofficial Python API for accessing Genius top 10 trending songs',
        author='Kenny Rozario',
        author_email='kmrozario98@gmail.com',
        url='https://www.github.com/kennyrozario/genius-trending',
        py_modules=['genius_trending'],
        license='MIT License',
        install_requires=['beautifulsoup4 >= 4.6.0', 'requests >= 2.18.4']
        )
