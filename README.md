Transformer
===========

A simple utility that transforms provided input to standard output, based on the transform.

ToDo
----

1. Provide Jinja Support

Requires
--------

1. lxml == 3.2.1

Installation
------------

Checkout and run setup.py

    python setup.py install

Usage
-----

If you need help at any moment, enter the following. This documentation assumes that you're
using the examples in the examples file.

    transformer --help

You need 2 files:

- Input File
- Transform File

Depending on what transform you use, you will need to provide different input
files and transforms you use. Like most programs, this application is stupid,
and it requires you to be explicit with what you give it. Please pay attention
to details.

You are required to pass 3 flags to transformer to work:

- **-i / --input** - Path to Input File
- **-t / --transformer** - Path to Transform File
- **-x / --transformer_type** - Transformer Type

The following are optional flags:

- **-s / --separator** - Row Separator for standard output. Not applicable for xslt.
- **--prefix** - String to place at begining of print out
- **--suffix** - String to place at end of stdout.

You can use these to understand what's going on below.

### Simple Transform

To use the Simple Transformer, do the following.

    transformer -i examples/people.csv -t examples/people_transformer.json -x simple

This will return a JSON file in the command line with the data you provided in people.csv,
with the transform found in people_transform.json.

To output in XML, write your own or use the XML transformer file found in examples:

    transformer -i examples/people.csv -t examples/people_transformer.xml -x simple

### XSLT Transform

To use the XSLT Transformer, do the following

    transformer -i examples/people.xml -t examples/people_transformer.xslt -x xslt

Simple Transformer
------------------

The Simple Transform doesn't have any intelligence and is not smart, so do not
expect it to do loops and like Jinja or Django Templating Language does. I
hope to add support for Jinja in the near future.

### Input File

    id,name,age,height,weight
    1,Alice,20,62,120.6
    2,Freddie,21,74,190.6
    3,Bob,17,68,120.0

### Transform File and Output (XML)

If you want your transformation to yield a XML, create the following XML Transform File (people_transform.xml):

    <person>
        <id>$id</id>
        <name>$name</name>
        <age>$age</age>
        <height>$height</height>
        <weight>$weight</weight>
    </person>

And run:

    transformer -i examples/people.csv -t examples/people_transformer.xml --prefix '<?xml version="1.0" encoding="UTF-8"?>' -x simple
    
To get: 

    <?xml version="1.0" encoding="UTF-8"?>
    <people>
        <person>
            <id>1</id>
            <name>Alice</name>
            <age>20</age>
            <height>62</height>
            <weight>120.6</weight>
        </person>
        <person>
            <id>2</id>
            <name>Freddie</name>
            <age>21</age>
            <height>74</height>
            <weight>190.6</weight>
        </person>
        <person>
            <id>3</id>
            <name>Bob</name>
            <age>17</age>
            <height>68</height>
            <weight>120.0</weight>
        </person>
    </people>
    
**NOTE:** You'll need to format yourself

### Transform File and Output (JSON)
If you want your transformation to yield a JSON, create the following JSON Transform File (people_transform.json):

    {
        id : "$id",
        name : "$name",
        age : "$age",
        height : "$height",
        weight : "$weight"
    }

And run:

    transformer -i examples/people.csv -t examples/people_transformer.json --prefix [ --suffix ] --separator , -x simple
    
To get: 

    [
        {
            id : "1",
            name : "Alice",
            age : "20",
            height : "62",
            weight : "120.6"
        },
        {
            id : "2",
            name : "Freddie",
            age : "21",
            height : "74",
            weight : "190.6"
        },
        {
            id : "3",
            name : "Bob",
            age : "17",
            height : "68",
            weight : "120.0"
        },
    ]
    
**NOTE:** You'll need to format yourself.

### Transform File and Output (SQL)
If you want your transformation to yield a JSON, create the following JSON Transform File (people_transform.json):

    INSERT INTO table (id, name, age, height, weight) VALUES ($id, "$name", "$age", "$height", "$weight")



And run:

    transformer -i examples/people.csv -t examples/people_transformer.sql --separator \; -x simple
    
To get: 

    INSERT INTO table (id, name, age, height, weight) VALUES (1, "Alice", "20", "62", "120.6");
    INSERT INTO table (id, name, age, height, weight) VALUES (2, "Freddie", "21", "74", "190.6");
    INSERT INTO table (id, name, age, height, weight) VALUES (3, "Bob", "17", "68", "120.0");
    
**NOTE:** You'll need to format yourself.

XSLT Transformer
----------------

Suppose you have an input XML file (tools.xml):

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <tool>
      <field id="prodName">
        <value>HAMMER HG2606</value>
      </field>
      <field id="prodNo">
        <value>32456240</value>
      </field>
      <field id="price">
        <value>$30.00</value>
      </field>
    </tool>

And the following is your XSLT file (tools.xslt):

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
      <html>
      <body>
      <form method="post" action="edittool.asp">
      <h2>Tool Information (edit):</h2>
      <table border="0">
        <xsl:for-each select="tool/field">
        <tr>
          <td><xsl:value-of select="@id"/></td>
          <td>
          <input type="text">
          <xsl:attribute name="id">
            <xsl:value-of select="@id" />
          </xsl:attribute>
          <xsl:attribute name="name">
            <xsl:value-of select="@id" />
          </xsl:attribute>
          <xsl:attribute name="value">
            <xsl:value-of select="value" />
          </xsl:attribute>
          </input>
          </td>
        </tr>
        </xsl:for-each>
      </table>
      <br />
      <input type="submit" id="btn_sub" name="btn_sub" value="Submit" />
      <input type="reset" id="btn_res" name="btn_res" value="Reset" />
      </form>
      </body>
      </html>
    </xsl:template>
    
    </xsl:stylesheet>

You want to run the transform with the following command:

    transformer -i examples/tools.xml -t examples/tools.xslt -x xslt
    
And you'll get the following output:

    <html>
      <body>
        <form method="post" action="edittool.asp">
          <h2>Tool Information (edit):</h2>
          <table border="0">
            <tr>
              <td>prodName</td>
              <td>
                <input type="text" id="prodName" name="prodName" value="HAMMER HG2606"/>
              </td>
            </tr>
            <tr>
              <td>prodNo</td>
              <td>
                <input type="text" id="prodNo" name="prodNo" value="32456240"/>
              </td>
            </tr>
            <tr>
              <td>price</td>
              <td>
                <input type="text" id="price" name="price" value="$30.00"/>
              </td>
            </tr>
          </table>
          <br/>
          <input type="submit" id="btn_sub" name="btn_sub" value="Submit"/>
          <input type="reset" id="btn_res" name="btn_res" value="Reset"/>
        </form>
      </body>
    </html>


