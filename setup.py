"""
Setup script for smuggle.

Add to requirements.pip with:
-e git+https://github.com/demiurgestudios/smuggle#egg=smuggle
"""
from setuptools import setup

if __name__ == '__main__':
    setup(name='smuggle',
          version='1.0',
          packages=['smuggle'],
          package_dir={'smuggle': 'smuggle'},
          install_requires=[],
          package_data={'smuggle': ['*.txt']})
