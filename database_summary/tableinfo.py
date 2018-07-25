#!/usr/bin/env python
import logging

from database_summary import access


def get_index_column_name(table_info):
    """
    Tries to infer an appropriate column to use as an index using
    the output from a table description.

    :param table_info: a dataframe of a table description
    :return: None or a column that is a primary key
    """

    primary_keys = table_info.loc[table_info['Key'] == 'PRI']
    num_primary_keys = len(primary_keys)

    if num_primary_keys > 1:
        logging.warning("More than one primary key using the first in the description")
    elif num_primary_keys == 0:
        logging.warning("No Primary Keys detected")
        return None

    return primary_keys.index[0]


def get_table_names(engine):
    """
    Get the available table names in a database.

    :param engine: a database connection
    :return: a list of strings that are table names
    """
    logging.info('Getting tablenames')
    show_tables = 'show tables;'
    tables = access.call_sql_against_connection(engine, show_tables, index='Tables_in_fpsetl')
    return [item for item in tables.index]


def get_table_info(engine, tablename):
    """
    Get information about a table.

    :param engine: a database connection object
    :param tablename: a table name as a string
    :return: a dataframe of the description of the given table
    """
    logging.info('Getting table meta for {}'.format(tablename))
    TABLE_INFO = 'DESCRIBE {tablename};'
    return access.call_sql_against_connection(engine, TABLE_INFO.format(tablename=tablename), index='Field')


def get_table_extract(engine, tablename, index, limit):
    """
    Get rows from the database up to the given limit.

    :param engine: database connection object
    :param tablename: the name of the table to get data from
    :param index: the column to use as an index for the data
    :param limit: the number of records to return
    :return: a dataframe
    """
    logging.info('getting table extract for {}'.format(tablename))
    TABLE_EXAMPLE = 'SELECT * FROM {tablename} LIMIT {limit};'
    return access.call_sql_against_connection(engine, TABLE_EXAMPLE.format(tablename=tablename, limit=limit), index)

