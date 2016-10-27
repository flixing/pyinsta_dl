# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='pyinsta_dl',
      py_modules=['pyinsta_dl'],
      version='0.0.7',
      description='Python implementation for download images and videos from Instagram',
      url='https://github.com/natanocr/pyinsta_dl',
      author='Natan Oliveira',
      author_email='natanoliveiracruz@gmail.com',
      keywords='instagram download media image video',
      long_description=open('README.rst').read(),
      license='MIT',
      platforms='OS Independent',
      packages=['pyinsta_dl'],
      install_requires=[
          'bs4',
      ],
      test_suite='test',
      zip_safe=False)
