import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

setup(
    name='pyramid_jwt',
    version='0.1.0',
    author='Euclides dos Reis Silva Junior',
    author_email='roinuj21@hotmail.com',
    keywords="jwt pyramid token security signing",
    packages=['pyramid_jwt'],
    url='http://github.com/euclides-jr/pyramid_jwt',
    license="MIT",
    description='jwt authentication policy',
    long_description=long_description,
    install_requires=[
        "pyramid",
        "PyJWT",
    ],
)
