#!/usr/bin/python
import argparse
import logging
import os
import sys
from transformer import xformer


def transform(input_file_path, transformer_file_path, transform_type, separator, row_pause, row, output):
    
    # verify inputs exist
    if not os.path.exists(input_file_path):
        raise IOError("%s does not exist." % input_file_path)

    if not os.path.exists(transformer_file_path):
        raise IOError("%s does not exist." % transformer_file_path)

    if row:
        row = int(row)
        if row < 1:
            raise ValueError("Invalid row number provided. Must be greater than 0.")

    if output:

        if not row and transform_type in ('simple', 'jinja', ):
            raise ValueError("Cannot output to file if a row is not specified.")

        if os.path.exists(output):
            os.remove(output)

    # transform
    if transform_type == 'xslt':
        xformed = xformer.xslt_transformer(input_file_path, transformer_file_path)
        if output:
            with open(output, 'wb') as outfile:
                outfile.write(xformed)
        else:
            sys.stdout.write(xformed)
    elif transform_type == 'jinja':
        xformer.jinja_transform(input_file_path, transformer_file_path, separator=separator,
                                row_pause=row_pause, process_row=row, output=output)
    elif transform_type == 'simple':
        xformer.simple_transformer(input_file_path, transformer_file_path, separator=separator,
                                   row_pause=row_pause, process_row=row, output=output)



def main():
    parser = argparse.ArgumentParser(description="Transforms provided input to standard output, based on the transform.")
    parser.add_argument('-i', '--input', help='Path to Input File', action='store', required=True)
    parser.add_argument('-t', '--transformer', help='Path to Transform File', action='store', required=True)
    parser.add_argument('-x', '--transformer_type', help='Transformer Type', choices=['simple', 'jinja', 'xslt'])
    parser.add_argument('-s', '--separator', help='Row Separator for standard output. Not applicable for xslt.', default='')
    parser.add_argument('--prefix', help='String to place at begining of stdout.', default='')
    parser.add_argument('--suffix', help='String to place at end of stdout.', default='')
    parser.add_argument('--pause', help='Use flag to pause after each row.', action='store_true')
    parser.add_argument('--row', help='Enter row number in CSV file to process')
    parser.add_argument('--output-filepath', help='Enter path to save file to. Does not output to STDOUT if given. Not available if rows not specified')
    args = parser.parse_args()

    try:
        sys.stdout.write('%s\n' % args.prefix)
        transform(args.input, args.transformer, args.transformer_type, args.separator, args.pause,
                  args.row, args.output_filepath)
        sys.stdout.write('%s\n' % args.suffix)
    except Exception, e:
        logging.exception("Error occurred while running code.")

if __name__ == "__main__":
    main()
