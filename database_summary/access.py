#!/usr/bin/env python
import os

import pandas
import sqlalchemy
import logging

from . import EnvironmentVariables, DEBUG, DBToolException

def create_engine():
    """
    Creates a connection to the database using the environment variable

    :return: Instantiated connection object to query against
    """

    connection_url = os.environ.get(EnvironmentVariables.database_url)
    logging.info('Connecting to database using environment variable')

    if not connection_url:
        error_format_string = '"{}" environment variable unset'
        logging.critical(error_format_string.format(EnvironmentVariables.database_url))
        raise DBToolException('Environment variables were not set correctly')

    return sqlalchemy.create_engine(connection_url, echo=DEBUG)


def call_sql_against_connection(engine, formatted_query, index=None):
    """
    Given a database connection calls an SQL query and returns a dataframe

    :param engine: Connection object to query against
    :param formatted_query: the SQL query to be called
    :param index: the column to use as an index in the dataframe
    :return: a dataframe of the result of the SQL query given
    """

    logging.debug("Calling query: {}".format(formatted_query))
    index = index if index else 'id'

    try:
        return pandas.read_sql_query(sql=formatted_query, con=engine, index_col=index)
    except sqlalchemy.exc.SQLAlchemyError as e:
        raise DBToolException(str(e))
