#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-heringer',
    version='0.1',
    description='Default Pygments theme with different colors.',
    keywords='pygments style',
    license='BSD',

    author='Matthias L�ken',

    url='https://github.com/matthiaslueken/pygments-style-heringer',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    github=pygments_style_github:GithubStyle''',

    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)