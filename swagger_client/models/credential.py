# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Credential(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Credential - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'int',
            'connector_id': 'int',
            'attr_key': 'str',
            'attr_value': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime'
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'connector_id': 'connector_id',
            'attr_key': 'attr_key',
            'attr_value': 'attr_value',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._user_id = None
        self._connector_id = None
        self._attr_key = None
        self._attr_value = None
        self._created_at = None
        self._updated_at = None

    @property
    def user_id(self):
        """
        Gets the user_id of this Credential.
        ID of user that owns this credential

        :return: The user_id of this Credential.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Credential.
        ID of user that owns this credential

        :param user_id: The user_id of this Credential.
        :type: int
        """
        self._user_id = user_id

    @property
    def connector_id(self):
        """
        Gets the connector_id of this Credential.
        The id for the connector data source from which the credential was obtained

        :return: The connector_id of this Credential.
        :rtype: int
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this Credential.
        The id for the connector data source from which the credential was obtained

        :param connector_id: The connector_id of this Credential.
        :type: int
        """
        self._connector_id = connector_id

    @property
    def attr_key(self):
        """
        Gets the attr_key of this Credential.
        Attribute name such as token, userid, username, or password

        :return: The attr_key of this Credential.
        :rtype: str
        """
        return self._attr_key

    @attr_key.setter
    def attr_key(self, attr_key):
        """
        Sets the attr_key of this Credential.
        Attribute name such as token, userid, username, or password

        :param attr_key: The attr_key of this Credential.
        :type: str
        """
        self._attr_key = attr_key

    @property
    def attr_value(self):
        """
        Gets the attr_value of this Credential.
        Encrypted value for the attribute specified

        :return: The attr_value of this Credential.
        :rtype: str
        """
        return self._attr_value

    @attr_value.setter
    def attr_value(self, attr_value):
        """
        Sets the attr_value of this Credential.
        Encrypted value for the attribute specified

        :param attr_value: The attr_value of this Credential.
        :type: str
        """
        self._attr_value = attr_value

    @property
    def created_at(self):
        """
        Gets the created_at of this Credential.
        When the record was first created. Use ISO 8601 datetime format

        :return: The created_at of this Credential.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Credential.
        When the record was first created. Use ISO 8601 datetime format

        :param created_at: The created_at of this Credential.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Credential.
        When the record in the database was last updated. Use ISO 8601 datetime format

        :return: The updated_at of this Credential.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Credential.
        When the record in the database was last updated. Use ISO 8601 datetime format

        :param updated_at: The updated_at of this Credential.
        :type: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

