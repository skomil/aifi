import json
import yaml
from jsonschema import Draft7Validator
import argparse

def get_refs(schema, refs):
    for k, v in schema.items():
        if isinstance(v, dict):
            get_refs(v, refs)
        elif k == "$ref":
            ref = v.replace("#/definitions/", "")
            refs.add(ref)

def openapitojson(startpoints, open_api_schema_file, json_schema_dir):

    # Load your OpenAPI schema (in YAML format)
    with open(open_api_schema_file, 'r') as f:
        openapi_schema = yaml.safe_load(f)

    # The components/schemas section of the OpenAPI document contains the schema definitions.
    schemas = openapi_schema['components']['schemas']

    json_schemas = {}

    for schema_name, schema_content in schemas.items():
        # Create a new JSON schema based on the OpenAPI schema.
        json_schema = {}

        # Properties, type, and description are usually the same.
        for key in ['properties', 'type', 'description']:
            if key in schema_content:
                json_schema[key] = schema_content[key]

        # Required is also usually the same, but needs to be at the top level in JSON Schema.
        if 'required' in schema_content:
            json_schema['required'] = schema_content['required']

        # For each property, if it has a "format", that usually maps to a "type" in JSON Schema.
        for property_name, property_content in schema_content.get('properties', {}).items():
            if 'format' in property_content:
                property_content['type'] = property_content['format']
                del property_content['format']

            # handle $ref, replacing '#/components/schemas/' with '#/definitions/' for JSON Schema
            if 'items' in property_content:
                if '$ref' in property_content['items']:
                    property_content['items']['$ref'] = property_content['items']['$ref'].replace('#/components/schemas/', '#/definitions/')
            if '$ref' in property_content:
                property_content['$ref'] = property_content['$ref'].replace('#/components/schemas/', '#/definitions/')

        # Add the converted schema to our collection of JSON Schemas.
        json_schemas[schema_name] = json_schema

    added_schemas = set()

    for root_object in startpoints:
        refs = set()
        get_refs(json_schemas[root_object], refs)

        # Add the root schema and any definitions it references to the root of JSON Schema.
        root_json_schema = dict(json_schemas[root_object])
        root_json_schema['definitions'] = {}
        for key in json_schemas.keys():
            if key is not root_object:
                root_json_schema['definitions'][key] = dict(json_schemas[key])

        # Write the root schema to a file.
        with open(f'{json_schema_dir}{root_object}.aifischema.json', 'w') as f:
            json.dump(root_json_schema, f, indent=4)

        # Validate the root schema
        try:
            Draft7Validator.check_schema(root_json_schema)
            print(f'Schema "{root_object}" is valid')
        except Exception as e:
            print(f'Schema "{root_object}" is invalid: {str(e)}')

    







    

args = argparse.ArgumentParser(description='Convert OpenAPI to JSON Schema')
args.add_argument('--openapi', help='OpenAPI file', default='../api.yaml') 
args.add_argument('--jsonschema', help='JSON Schema Directory', default='../')
args.add_argument('--objects', help='Root Objects', default=['Rig', 'DeviceFactory', 'Rack'])
if __name__ == '__main__':
    arguments = args.parse_args()
    openapitojson(arguments.objects, arguments.openapi, arguments.jsonschema)    
