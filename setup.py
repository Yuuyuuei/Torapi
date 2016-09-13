#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow trove classifiers in previous python versions
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

from Torapi import __version__ as version

setup(
    name='Torapi',
    version=version,
    install_requires=['requests'],
    author='Eugene Tan',
    author_email='eugene@eugenetan.co.uk',
    description='Unofficial simple http://torrentapi.org/ API library',
    long_description='Unofficial simple http://torrentapi.org/ API library.',
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ]
)
