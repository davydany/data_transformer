Transformer
===========

A simple utility that transforms provided input to standard output, based on the transform.

Installation
------------

TODO

Examples
--------

If you need help at any moment, enter the following. This documentation assumes that you're
using the examples in the examples file.

> transformer --help

### Simple Transform

To use the Simple Transformer, do the following.

> transformer -i examples/people.csv -t examples/people_transformer.json -x simple

This will return a JSON file in the command line with the data you provided in people.csv,
with the transform found in people_transform.json.

To output in XML, write your own or use the XML transformer file found in examples:

> transformer -i examples/people.csv -t examples/people_transformer.xml -x simple

### XSLT Transform

To use the XSLT Transformer, do the following

> transformer -i examples/people.xml -t examples/people_transformer.xslt -x xslt

