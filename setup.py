from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyrelate',
    version='1.0.4',
    author='sendwithus',
    author_email='matt@sendwithus.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/mrmch/pyrelate',
    license='LICENSE.txt',
    description='Python API client for relateiq',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 1.1.0"
    ]
)
