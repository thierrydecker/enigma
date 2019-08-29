# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license_document = f.read()

setup(
        name='enigma',
        version='0.1.0',
        description='Enigma implementation',
        long_description=readme,
        author='Thierry DECKER',
        author_email='mail@thierry-decker.com',
        url='https://github.com/thierrydecker/enigma',
        license=license_document,
        packages=find_packages(exclude=('tests', 'docs'))
)
