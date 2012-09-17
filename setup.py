# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name             = 'tornado-backdoor',
    version          = '0.1.0',
    url              = 'https://github.com/saghul/tornado-backdoor',
    author           = 'Saúl Ibarra Corretgé',
    author_email     = 'saghul@gmail.com',
    description      = 'Interactive interpreter over TCP for Tornado',
    long_description = open('README.rst', 'r').read(),
    packages         = ['tornado_backdoor'],
    classifiers      = [
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.0",
          "Programming Language :: Python :: 3.1",
          "Programming Language :: Python :: 3.2"
    ]
)

