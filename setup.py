"""Compare Setup

This module contains the setuptools.setup() definition for the Compare program.
Usage
    ./install
"""
from pathlib import Path, PurePath
from setuptools import setup, find_packages

root=Path(__file__).resolve().parent
requirements_txt=Path(PurePath(root, 'requirements.txt'))

def read_requirements_file(fd):
    res=[]
    if Path(fd).is_file():
        with open(fd, 'r') as reader:
            res +=[lin.strip('\n')
                    for lin in reader.readlines() if '#' not in lin]
    return res

with open('README.md', 'r') as fh:
    long_description=fh.read()

requirements=read_requirements_file(requirements_txt)

setup(
    name='Compare',
    version='1.0.0',
    author='Emille Giddings',
    author_email='emilledigital@gmail.com',
    description='<enter description here>',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    install_requires=requirements,
    packages=find_packages(),
    package_data={'': ['', '']},
    entry_points={
        'console_scripts': [
            'compare=compare.__main__:main',
            'run-microservice=run_microservice:main',
        ]
    },
    tests_require=[''],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    setup_requires=[
    'setuptools>=42',
    'wheel',
    'setuptools_scm>=3.4'
    ],
)