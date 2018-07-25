#!/usr/bin/env python
import logging
import sys

from database_summary import access
from database_summary import outport
from database_summary import tableinfo

def dump_database_info(args):
    """
    Dumps a description and an extract for the visible tables in the given database.
    """
    output_path = args[0]
    print(output_path)

    logging.info('Dumping table meta and table extracts')

    engine = access.create_engine()
    tables = tableinfo.get_table_names(engine)

    for tablename in tables:

        table_info = tableinfo.get_table_info(engine, tablename)
        outport.dump_csv(table_info, tablename+'-meta', output_path)

        index_name = tableinfo.get_index_column_name(table_info)
        if not index_name:
            logging.error("Could not determine index for table {} cannot get extract".format(tablename))
            continue

        table_extract = tableinfo.get_table_extract(engine, tablename, index_name, '1000')
        outport.dump_csv(table_extract, tablename+'-extract', output_path)

    logging.info('Finished dump')
    exit(0)


def main():
    dump_database_info(sys.argv[1:2])


if __name__ == '__main__':
    exit(main())
