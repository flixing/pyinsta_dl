# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='pyinsta_dl',
      version='0.0.1',
      description='Python implementation for download media (images and videos) from Instagram',
      url='https://github.com/natanocr/pyinsta_dl',
      author='Natan Oliveira',
      author_email='natanoliveiracruz@gmail.com',
      keywords='instagram download media image video',
      license='MIT',
      packages=['pyinsta_dl'],
      install_requires=[
            'bs4',
      ],
      zip_safe=False)