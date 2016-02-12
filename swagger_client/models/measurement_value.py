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


class MeasurementValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MeasurementValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_time': 'str',
            'value': 'float',
            'note': 'str'
        }

        self.attribute_map = {
            'start_time': 'start_time',
            'value': 'value',
            'note': 'note'
        }

        self._start_time = None
        self._value = None
        self._note = None

    @property
    def start_time(self):
        """
        Gets the start_time of this MeasurementValue.
        When the measurement event occurred . Use ISO 8601 datetime format

        :return: The start_time of this MeasurementValue.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this MeasurementValue.
        When the measurement event occurred . Use ISO 8601 datetime format

        :param start_time: The start_time of this MeasurementValue.
        :type: str
        """
        self._start_time = start_time

    @property
    def value(self):
        """
        Gets the value of this MeasurementValue.
        Value for the measurement

        :return: The value of this MeasurementValue.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MeasurementValue.
        Value for the measurement

        :param value: The value of this MeasurementValue.
        :type: float
        """
        self._value = value

    @property
    def note(self):
        """
        Gets the note of this MeasurementValue.
        An optional note the user may include with their measurement

        :return: The note of this MeasurementValue.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this MeasurementValue.
        An optional note the user may include with their measurement

        :param note: The note of this MeasurementValue.
        :type: str
        """
        self._note = note

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

