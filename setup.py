#!/usr/bin/env python

from distutils.core import setup

setup(
    name='database_summary',
    version='0.1.0.rc0',
    description='Database Inquiry',
    author='Sarah Lynch',
    author_email='sarahlynch@fastmail.com',
    packages=['database_summary'],
    install_requires=[
        'pandas',
        'psycopg2-binary',
        'mysqlclient',
        'sqlalchemy'
    ],
    entry_points = {
        'console_scripts': [
            'summarise=database_summary.main:main'
        ]
    },
)