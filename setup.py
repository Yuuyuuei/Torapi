#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

from Torapi import __version__, __author__, __email__

license_text = open('LICENSE').read()
long_description = open('README.md').read()

setup(
    name='Torapi',
    version=__version__,
	url = 'https://github.com/Yuuyuuei/Torapi',
    install_requires=['requests'],
    author=__author__,
    author_email=__email__,
    description='Unofficial simple http://torrentapi.org/ API library',
    long_description=long_description,
    license=license_text,
	packages=['Torapi'],
    data_files=[('Torapi', ['LICENSE', 'README.md'])],
    classifiers=[
        'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ]
)
