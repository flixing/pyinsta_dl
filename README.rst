pyinsta_dl
===================

.. image:: https://travis-ci.org/natanocr/pyinsta_dl.svg?branch=master
    :alt: travis-cli tests status for pyinsta_dl
    :target: https://travis-ci.org/natanocr/pyinsta_dl

.. image:: https://coveralls.io/repos/github/natanocr/pyinsta_dl/badge.svg
    :alt: coveralls tests status for pyinsta_dl
    :target: https://coveralls.io/github/natanocr/pyinsta_dl

.. image:: https://landscape.io/github/natanocr/pyinsta_dl/master/landscape.svg?style=flat
   :target: https://landscape.io/github/natanocr/pyinsta_dl/master
   :alt: Code Health

.. image:: http://badge.kloud51.com/pypi/v/pyinsta_dl.svg
    :alt: Version of pyinsta_dl
    :target: https://pypi.python.org/pypi/pyinsta_dl/

.. image:: http://badge.kloud51.com/pypi/d/pyinsta_dl.svg
    :alt: Downloads of pyinsta_dl
    :target: https://pypi.python.org/pypi/pyinsta_dl/

.. image:: http://badge.kloud51.com/pypi/l/pyinsta_dl.svg
    :alt: License of pyinsta_dl
    :target: https://pypi.python.org/pypi/pyinsta_dl/

.. image:: http://badge.kloud51.com/pypi/f/pyinsta_dl.svg
    :alt: Format of pyinsta_dl
    :target: https://pypi.python.org/pypi/pyinsta_dl/

.. image:: http://badge.kloud51.com/pypi/py_versions/pyinsta_dl.svg
    :alt: Python version of pyinsta_dl
    :target: https://pypi.python.org/pypi/pyinsta_dl/

.. image:: http://badge.kloud51.com/pypi/e/pyinsta_dl.svg
    :alt: Eggs pyinsta_dl
    :target: https://pypi.python.org/pypi/pyinsta_dl/


Python implementation for download images and videos from Instagram

PhantomJs is requeride
--------

>>> sudo curl --output /usr/local/phantomjs/phantomjs https://s3.amazonaws.com/circle-downloads/phantomjs-2.1.1 && chmod +x /usr/local/phantomjs/phantomjs


Usage for Single media
-------

>>> import pyinsta_dl
>>> url = pyinsta_dl.get('https://www.instagram.com/p/BIIKGvsAzAn')
>>> print(url)

Usage for All media
-------

>>> import pyinsta_dl
>>> urls_list = pyinsta_dl.get_all('https://www.instagram.com/milreceitas/')
>>> print(urls_list)

Install
-------

**pyinsta_dl** is also available at pypi:

http://pypi.python.org/pypi/pyinsta_dl

::

    $ pip install pyinsta_dl

And done ;)

For devs:
--------

>>> git clone https://github.com/natanocr/pyinsta_dl.git
>>> cd pyinsta_dl
>>> pip install -r requeriments.txt

Tests
-------

>>> python setup.py test

----

========== ======
Source      https://github.com/natanocr/pyinsta_dl
Issues      https://github.com/natanocr/pyinsta_dl/issues
PyPi        http://pypi.python.org/pypi/pyinsta_dl
Author      Natan Oliveira
License     MIT
========== ======
