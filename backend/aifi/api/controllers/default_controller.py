import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from aifi.api.models.error import Error  # noqa: E501
from aifi.api.models.rack import Rack  # noqa: E501
from aifi.api.models.rig import Rig  # noqa: E501
from aifi.api import util


def create_rack(rack):  # noqa: E501
    """Create a new rack

     # noqa: E501

    :param rack: The rack to create
    :type rack: dict | bytes

    :rtype: Union[Rack, Tuple[Rack, int], Tuple[Rack, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        rack = Rack.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_rack_by_id(rack_id):  # noqa: E501
    """Delete a specific rack

     # noqa: E501

    :param rack_id: The ID of the rack to delete
    :type rack_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_rack_by_id(rack_id):  # noqa: E501
    """Retrieve a specific rack

     # noqa: E501

    :param rack_id: The ID of the rack to retrieve
    :type rack_id: str

    :rtype: Union[Rack, Tuple[Rack, int], Tuple[Rack, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_racks():  # noqa: E501
    """Retrieve a list of racks

     # noqa: E501


    :rtype: Union[List[Rack], Tuple[List[Rack], int], Tuple[List[Rack], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_rig():  # noqa: E501
    """Retrieve the rig

     # noqa: E501


    :rtype: Union[Rig, Tuple[Rig, int], Tuple[Rig, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_rack_by_id(rack_id, rack):  # noqa: E501
    """Update a specific rack

     # noqa: E501

    :param rack_id: The ID of the rack to update
    :type rack_id: str
    :param rack: The updated rack data
    :type rack: dict | bytes

    :rtype: Union[Rack, Tuple[Rack, int], Tuple[Rack, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        rack = Rack.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
