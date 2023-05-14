# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="aifi - OpenAPI 3.0",
    author_email="",
    url="",
    keywords=["OpenAPI", "aifi - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about &#x60;&#x60;&#x60;mermaid classDiagram class Component {     string id } class ComponentTemplate {     string id     string label } class Rack {     string id     %% the below property is an array with cardinality [0..*]     string hiddenComponents } class UiSetting {     string id     string label     boolean hidden     string dataType     string uiType     object defaultValue     object initialValue } class ComponentDefinition {     string id     string label     object apiConfiguration     string version }  class Asset {     string id     string type     string label     string description     string storageLocation     %% the below property is an array with cardinality [0..*]     string previewLocations }  class Rig {  } class Connection {     string id     string label     string description     string type     boolean required     boolean allowMultiple } class KeyValue {     string key     string value } class Error {     string message     integer code }  Rack \&quot;1\&quot; --&gt; \&quot;0..*\&quot; Component : components Rig \&quot;1\&quot; --&gt; \&quot;0..*\&quot; ComponentDefinition : componentDefinitions Rig  \&quot;1\&quot; --&gt; \&quot;0..*\&quot; KeyValue : config Rig  \&quot;1\&quot; --&gt; \&quot;0..*\&quot; KeyValue : secrets Rack \&quot;1\&quot; --&gt; \&quot;0..1\&quot;  Component: rackAsComponent Rack \&quot;1\&quot; --&gt; \&quot;0..*\&quot;  Connection: output Rig \&quot;1\&quot; --&gt; \&quot;0..*\&quot; Rack : racks ComponentDefinition \&quot;1\&quot; --&gt; \&quot;1..*\&quot; ComponentTemplate : componentTemplates ComponentDefinition \&quot;1\&quot; --&gt; \&quot;0..*\&quot; Asset : assets ComponentTemplate \&quot;1\&quot; --&gt; \&quot;1\&quot; Component: component Component \&quot;1\&quot; --&gt; \&quot;0..1\&quot;  ComponentDefinition: componentDefinition Component \&quot;1\&quot; --&gt; \&quot;0..*\&quot;  UiSetting: uiSettings Component \&quot;1\&quot; --&gt; \&quot;0..*\&quot;  Connection: input Component \&quot;1\&quot; --&gt; \&quot;0..*\&quot;  Connection: output &#x60;&#x60;&#x60;
    """
)

