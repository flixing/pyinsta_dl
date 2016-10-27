# -*- coding: utf-8 -*-
from setuptools import setup
import io
import os
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()

setup(name='pyinsta_dl',
      version='0.0.1',
      description='Python implementation for download images and videos from Instagram',
      url='https://github.com/natanocr/pyinsta_dl',
      author='Natan Oliveira',
      author_email='natanoliveiracruz@gmail.com',
      keywords='instagram download media image video',
      long_description=read('README.md'),
      license='MIT',
      packages=['pyinsta_dl'],
      install_requires=[
            'bs4',
      ],
      zip_safe=False)