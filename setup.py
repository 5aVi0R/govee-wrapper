from setuptools import setup

setup (
    name='govee-wrapper',
    url='https://github.com/5aVi0R/govee-wrapper',
    author='5aVi0R',
    author_email='N/A',
    packages=['govee-wrapper'],
    install_requires=['requests','json'],
    version='1.0',
    license='Apache License 2.0',
    description='A python wrapper for the official Govee api',
    long_description=open('README.md').read()
)