Transformer
===========
![alt tag](https://raw.github.com/davydany/DataTransformer/master/transformer.jpg)


A simple utility that transforms provided input to standard output, based on the transform.

Requires
--------

1. lxml == 3.2.1
2. Jinja2 == 2.7.1

Installation
------------

Checkout and run setup.py

    python setup.py install

Features
--------

DataTransformer transforms your data using the transform file you provide it. It supports 3
formats. They are:

- Simple Transformer
- Jinja2 Template Language
- XSLT Transform

**Which one should you use?**

Well that depends on what you want to do. If you're comfortable with representing your input 
with XML and transforming with XSLT, you should use XSLT transforms. Most people are not, so
that's why you can use the Simple Transform and Jinja2 Template Language. Jinja2 is just as
powerful (if not more powerful) than XSLT. However, with great power comes great need to 
understand what you're doing. You will need to read Jinja2's documentation before 
fully utilizing transformer. The simplest solution, therefore, is to use the Simple Transformer
but it is not very smart. You cannot use if/then conditions, add/subtract numbers or check if a 
number is odd or even. Therefore, you are limited with just string replace. If this is what you
want, feel free to use the Simple transformer.

However, I urge you to look at the Usage and the examples below before making your decision.

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
- **--row** - Enter the row number you want to process. Row number must be greater than 1, where 1 represents header.

You can use these to understand what's going on below.

### Simple Transform

To use the Simple Transformer, do the following.

    transformer -i examples/people.csv -t examples/people_transformer.json -x simple

This will return a JSON file in the command line with the data you provided in people.csv,
with the transform found in people_transform.json.

To output in XML, write your own or use the XML transformer file found in examples:

    transformer -i examples/people.csv -t examples/people_transformer.xml -x simple

### Jinja2 Transformer

To use the Jinja2 Transformer, do the following.

    transformer -i examples/people.csv -t examples/people_transformer.jinja -x jinja

This will return XML file that was formatted using the Jinja templating language.

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

Jinja2 Transformer
------------------

Suppose you have a CSV file (people.csv)

    id,name,age,height,weight
    1,Alice,20,62,120.6
    2,Freddie,21,74,190.6
    3,Bob,17,68,120.0

And we have the following Jinja2 formatted file:


    {% if id|float % 2 == 0 %}
    <people>
        <id>{{ id|float + 3 }}</id>
        <name>{{ name|upper }}</id>
        <age>{{ age| float }}</age>
        <height>{{ height|float / 12 }}</height>
        <weight>{{ weight }}</weight>
    </people>
    {% endif %}


We will run the following command:

    transformer -i examples/people.csv -t examples/people_transformer.jinja -x jinja

Which will yield:


    <people>
        <id>5.0</id>
        <name>FREDDIE</id>
        <age>21.0</age>
        <height>6.16666666667</height>
        <weight>190.6</weight>
    </people>


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


