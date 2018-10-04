from setuptools import setup

setup(
    name='awscli-plugins',
    version='0.1',
    py_modules=[
        'cloudformation'
    ],
    install_requires=[
        'awscli',
    ],
)