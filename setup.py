import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name="Transformer",
	version="0.0.2",
	author="David Daniel",
	author_email="David.Daniel@dealertrack.com",
	description=("Transforms provided input to an output, based on the transform."),
	license="BSD",
	keywords="transformer xslt xml xslt transform",
	packages=find_packages(),
	long_description=read('README.md'),
	entry_points={
		'console_scripts' : [
			'transformer = transformer.runner:main'
		]
	},
	install_requires=['lxml==3.2.1', 'Jinja2==2.7.1']
)
