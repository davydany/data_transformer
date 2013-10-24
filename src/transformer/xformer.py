import csv
import sys
import lxml.etree as ET


def xslt_transformer(input_file_path, transformer_file_path):
    """
    Transforms a input XML file `input_file_path`
    using the XSLT `transformer_file_path`.
    """
    # perform transformation
    dom = ET.parse(input_file_path)
    xslt = ET.parse(transformer_file_path)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    return ET.tostring(newdom, pretty_print=True)


def simple_transformer(csv_input_file_path, transformer_file_path, separator):
    """
    Transforms a CSV file `csv_input_file_path` using the Transformation file in
    `transformer_file_path`.
    """

    # read contents of the transformer
    transformer_contents = ""
    with open(transformer_file_path, 'r') as transformer_file:
        transformer_contents = transformer_file.read()
    if len(transformer_contents) == 0:
        raise ValueError("Transformer is empty.")

    # parse the csv file each row at at time
    with open(csv_input_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        row_count = 0
        fieldnames = []

        for row in reader:
            output_template = transformer_contents.strip()
            row_count += 1

            # retrieve field names during first pass
            if row_count == 1:
                fieldnames = row
                continue

            for i, value in enumerate(row):
                output_template = output_template.replace("$%s" % fieldnames[i], value)

            sys.stdout.write(output_template)
            sys.stdout.write(separator)






