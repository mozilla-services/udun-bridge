import platform
import codecs
import os
from setuptools import setup, find_packages
from udun import __version__

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


REQUIREMENTS = [
    'redis',
    'konfig',
    'requests'
]


ENTRY_POINTS = {
    'console_scripts': [
        'udun = udun:main'
    ]
}


setup(name='udun',
      version=__version__,
      description='Kinto-to-Balrog',
      long_description=README,
      license='Apache License (2.0)',
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "License :: OSI Approved :: Apache Software License"
      ],
      keywords="web services",
      author='Mozilla Services',
      author_email='services-dev@mozilla.com',
      url='https://github.com/mozilla-services/udun-bridge',
      packages=find_packages(),
      zip_safe=False,
      install_requires=REQUIREMENTS,
      entry_points=ENTRY_POINTS)
