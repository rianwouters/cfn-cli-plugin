from setuptools import setup
from setuptools.command.install import install
from os import system

class CustomInstall(install):
    def run(self):
        install.run(self)
        system("aws configure set plugins.cloudformation cloudformation")

setup(
    name='awscli-plugins',
    version='0.1',
    py_modules=[
        'cloudformation',
        'package.search_path',
        'package.local_includes'
    ],
    install_requires=[
        'awscli'
    ],
    cmdclass={
        'install': CustomInstall
    },
)