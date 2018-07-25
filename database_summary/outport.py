#!/usr/bin/env python
import os
from os import path


def dump_csv(dataframe, filename, output_path):

    absolute_path = path.abspath(output_path)

    if not path.exists(absolute_path):
        os.mkdir(absolute_path)

    assert path.isdir(absolute_path), 'Output path must be a directory: {}'.format(absolute_path)

    filename_extension = filename + '.csv'
    output_filepath = path.join(absolute_path, filename_extension)

    dataframe.to_csv(output_filepath, encoding='utf-8')