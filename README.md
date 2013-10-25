Transformer
===========

A simple utility that transforms provided input to standard output, based on the transform.

Requires
--------

1. lxml == 3.2.1

Installation
------------

Checkout and run setup.py

> python setup.py build
> python setup.py install

Usage
-----

If you need help at any moment, enter the following. This documentation assumes that you're
using the examples in the examples file.

> transformer --help

You need 2 files:

- Input File
- Transform File

Depending on what transform you use, you will need to provide different input
files and transforms you use. Like most programs, this application is stupid,
and it requires you to be explicit with what you give it. Please pay attention
to details.

You are required to pass 3 flags to transformer to work:




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

Simple Transformer
------------------

The Simple Transform doesn't have any intelligence and is not smart, so do not
expect it to do loops and like Jinja or Django Templating Language does. I
hope to add support for Jinja in the near future.

To use
