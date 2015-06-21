# coding=utf-8
"""
"""
from distutils.core import setup

version = '0.1'

setup(
  name = 'django-staticfiles-webpack',
  packages = ['webpack'],
  version = version,
  description = 'Support for loading Webpack hashed files in Django templates via the static files app.',
  author = 'Rocco Schulz',
  author_email = 'rocco@is-gr8.com',
  url = 'https://github.com/schocco/django-staticfiles-webpack',
  download_url = 'https://github.com/schocco/django-staticfiles-webpack/webpack/tarball/{}'.format(version),
  keywords = ['django', 'webpack', 'assets', 'build', 'static'],
  classifiers = [
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Framework :: Django',
    'Environment :: Web Environment',
    'License :: OSI Approved :: MIT License',
  ],
)