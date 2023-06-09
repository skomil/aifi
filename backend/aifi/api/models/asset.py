# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from aifi.api.models.base_model_ import Model
from aifi.api import util


class Asset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=None, label=None, description=None, storage_location=None, preview_locations=None):  # noqa: E501
        """Asset - a model defined in OpenAPI

        :param id: The id of this Asset.  # noqa: E501
        :type id: str
        :param type: The type of this Asset.  # noqa: E501
        :type type: str
        :param label: The label of this Asset.  # noqa: E501
        :type label: str
        :param description: The description of this Asset.  # noqa: E501
        :type description: str
        :param storage_location: The storage_location of this Asset.  # noqa: E501
        :type storage_location: str
        :param preview_locations: The preview_locations of this Asset.  # noqa: E501
        :type preview_locations: List[str]
        """
        self.openapi_types = {
            'id': str,
            'type': str,
            'label': str,
            'description': str,
            'storage_location': str,
            'preview_locations': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'label': 'label',
            'description': 'description',
            'storage_location': 'storageLocation',
            'preview_locations': 'previewLocations'
        }

        self._id = id
        self._type = type
        self._label = label
        self._description = description
        self._storage_location = storage_location
        self._preview_locations = preview_locations

    @classmethod
    def from_dict(cls, dikt) -> 'Asset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Asset of this Asset.  # noqa: E501
        :rtype: Asset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Asset.


        :return: The id of this Asset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Asset.


        :param id: The id of this Asset.
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Asset.


        :return: The type of this Asset.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Asset.


        :param type: The type of this Asset.
        :type type: str
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this Asset.


        :return: The label of this Asset.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Asset.


        :param label: The label of this Asset.
        :type label: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this Asset.


        :return: The description of this Asset.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Asset.


        :param description: The description of this Asset.
        :type description: str
        """

        self._description = description

    @property
    def storage_location(self):
        """Gets the storage_location of this Asset.


        :return: The storage_location of this Asset.
        :rtype: str
        """
        return self._storage_location

    @storage_location.setter
    def storage_location(self, storage_location):
        """Sets the storage_location of this Asset.


        :param storage_location: The storage_location of this Asset.
        :type storage_location: str
        """

        self._storage_location = storage_location

    @property
    def preview_locations(self):
        """Gets the preview_locations of this Asset.


        :return: The preview_locations of this Asset.
        :rtype: List[str]
        """
        return self._preview_locations

    @preview_locations.setter
    def preview_locations(self, preview_locations):
        """Sets the preview_locations of this Asset.


        :param preview_locations: The preview_locations of this Asset.
        :type preview_locations: List[str]
        """

        self._preview_locations = preview_locations
