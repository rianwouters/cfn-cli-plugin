from setuptools import setup
from setuptools.command.install import install
from subprocess import call
from os import system

class CustomInstall(install):
    def run(self):
        install.run(self)
        system("aws configure set plugins.cloudformation cloudformation")

setup(
    name='awscli-plugins',
    version='0.1',
    py_modules=[
        'cloudformation'
    ],
    install_requires=[
        'awscli',
    ],
    cmdclass={
        'install': CustomInstall
    },
)