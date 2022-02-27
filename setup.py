import os
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
   name='raspberrydisplay',
   version='0.6',
   description='A simple module for displaying RaspberryPi 4 info onto OLED display',
   author='RushKappa',
   author_email='bartoszzylwis@gmail.com',
   package_data={'raspberrydisplay':['config.ini']},
   install_requires=required,
   packages=find_packages(),
   
)
