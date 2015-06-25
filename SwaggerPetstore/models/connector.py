#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class Connector(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'display_name': 'str',
            'image': 'str',
            'get_it_url': 'str',
            'connected': 'str',
            'connect_instructions': 'str',
            'last_update': 'int',
            'latest_data': 'int',
            'no_data_yet': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'image': 'image',
            'get_it_url': 'getItUrl',
            'connected': 'connected',
            'connect_instructions': 'connectInstructions',
            'last_update': 'lastUpdate',
            'latest_data': 'latestData',
            'no_data_yet': 'noDataYet'
        }
        
        # Connector ID number
        self.id = None  # int
        
        # Connector lowercase system name
        self.name = None  # str
        
        # Connector pretty display name
        self.display_name = None  # str
        
        # URL to the image of the connector logo
        self.image = None  # str
        
        # URL to a site where one can get this device or application
        self.get_it_url = None  # str
        
        # True if the authenticated user has this connector enabled
        self.connected = None  # str
        
        # URL and parameters used when connecting to a service
        self.connect_instructions = None  # str
        
        # Epoch timestamp of last sync
        self.last_update = None  # int
        
        # Number of measurements obtained during latest update
        self.latest_data = None  # int
        
        # True if user has no measurements for this connector
        self.no_data_yet = None  # bool
        

    def __repr__(self):
        properties = []
        for p in self.__dict__:
            if p != 'swaggerTypes' and p != 'attributeMap':
                properties.append('{prop}={val!r}'.format(prop=p, val=self.__dict__[p]))

        return '<{name} {props}>'.format(name=__name__, props=' '.join(properties))


