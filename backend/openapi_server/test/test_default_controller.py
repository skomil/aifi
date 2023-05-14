# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.rack import Rack  # noqa: E501
from openapi_server.models.rig import Rig  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_rack(self):
        """Test case for create_rack

        Create a new rack
        """
        rack = {"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"components":[{"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"input":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"uiSettings":[{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"},{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"}],"id":"id","componentDefinition":{"apiConfiguration":"{}","assets":[{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"},{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"}],"componentTemplates":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"id":"id","label":"label","version":"version"}},{"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"input":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"uiSettings":[{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"},{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"}],"id":"id","componentDefinition":{"apiConfiguration":"{}","assets":[{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"},{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"}],"componentTemplates":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"id":"id","label":"label","version":"version"}}],"hiddenComponents":["hiddenComponents","hiddenComponents"],"id":"id","rackAsComponent":{"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"input":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"uiSettings":[{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"},{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"}],"id":"id","componentDefinition":{"apiConfiguration":"{}","assets":[{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"},{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"}],"componentTemplates":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"id":"id","label":"label","version":"version"}}}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/racks',
            method='POST',
            headers=headers,
            data=json.dumps(rack),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_rack_by_id(self):
        """Test case for delete_rack_by_id

        Delete a specific rack
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/racks/{rack_id}'.format(rack_id='rack_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rack_by_id(self):
        """Test case for get_rack_by_id

        Retrieve a specific rack
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/racks/{rack_id}'.format(rack_id='rack_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_racks(self):
        """Test case for get_racks

        Retrieve a list of racks
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/racks',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rig(self):
        """Test case for get_rig

        Retrieve the rig
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rig',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_rack_by_id(self):
        """Test case for update_rack_by_id

        Update a specific rack
        """
        rack = {"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"components":[{"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"input":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"uiSettings":[{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"},{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"}],"id":"id","componentDefinition":{"apiConfiguration":"{}","assets":[{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"},{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"}],"componentTemplates":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"id":"id","label":"label","version":"version"}},{"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"input":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"uiSettings":[{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"},{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"}],"id":"id","componentDefinition":{"apiConfiguration":"{}","assets":[{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"},{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"}],"componentTemplates":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"id":"id","label":"label","version":"version"}}],"hiddenComponents":["hiddenComponents","hiddenComponents"],"id":"id","rackAsComponent":{"output":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"input":[{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True},{"allowMultiple":True,"description":"description","id":"id","label":"label","type":"type","required":True}],"uiSettings":[{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"},{"hidden":True,"defaultValue":"{}","dataType":"dataType","uiType":"uiType","id":"id","label":"label","initialValue":"{}"}],"id":"id","componentDefinition":{"apiConfiguration":"{}","assets":[{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"},{"description":"description","storageLocation":"storageLocation","id":"id","label":"label","previewLocations":["previewLocations","previewLocations"],"type":"type"}],"componentTemplates":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"id":"id","label":"label","version":"version"}}}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/racks/{rack_id}'.format(rack_id='rack_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(rack),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
