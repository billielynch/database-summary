#!/usr/bin/env python
import logging


DEBUG = False
logging.basicConfig(
    level='DEBUG' if DEBUG else 'INFO',
    format='%(levelname)-10s %(message)s'
)

class EnvironmentVariables(object):
    database_url='DATABASE_URL'


class DBToolException(Exception):
    pass
