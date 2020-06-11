import os
from importlib.machinery import SourceFileLoader
from setuptools import setup, find_packages

version = SourceFileLoader(
    'agentos.version', os.path.join('agentos', 'version.py')).load_module().VERSION

setup(
    name='agentos',
    author='Andy Konwinski',
    version=version,
    packages=find_packages(),
    install_requires=[
        'click>=7.0',
        'mlflow',
        'gym',
    ],
    entry_points='''
        [console_scripts]
        agentos=agentos.cli:agentos_cmd
    ''',
    license='Apache License 2.0',
)
