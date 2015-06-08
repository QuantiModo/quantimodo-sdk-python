#!/usr/bin/env python
# coding: utf-8

"""
MeasurementsApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..util import remove_none

from ..swagger import ApiClient

class MeasurementsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client
    
    def measurement_sources_get(self, **kwargs):
        """
        Get measurement sources
        Returns a list of all the apps from which measurement data is obtained.

        
        :return: None
        """
        
        all_params = []

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method measurement_sources_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/measurementSources'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict())
        query_params = remove_none(dict())
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        
    def measurement_sources_post(self, name, **kwargs):
        """
        Add a data source
        Add a life-tracking app or device to the QuantiModo list of data sources.

        :param list[MeasurementSource] name: An array of names of data sources you want to add. (required)
        
        :return: None
        """
        
        # verify the required parameter 'name' is set
        if name is None:
            raise ValueError("Missing the required parameter `name` when calling `measurement_sources_post`")
        
        all_params = ['name']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method measurement_sources_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/measurementSources'.replace('{format}', 'json')
        method = 'POST'

        path_params = remove_none(dict())
        query_params = remove_none(dict())
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = params.get('name')

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        
    def measurements_get(self, variable_name, **kwargs):
        """
        Get measurements for this user
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten.

        :param str variable_name: Name of the variable you want measurements for (required)
        :param str unit: The unit your want the measurements in 
        :param str start_time: The lower limit of measurements returned (Epoch) 
        :param str end_time: The upper limit of measurements returned (Epoch) 
        :param int grouping_width: The time (in seconds) over which measurements are grouped together 
        :param str grouping_timezone: The time (in seconds) over which measurements are grouped together 
        
        :return: None
        """
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `measurements_get`")
        
        all_params = ['variable_name', 'unit', 'start_time', 'end_time', 'grouping_width', 'grouping_timezone']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method measurements_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/measurements'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict())
        query_params = remove_none(dict(variableName=params.get('variable_name'), unit=params.get('unit'), startTime=params.get('start_time'), endTime=params.get('end_time'), groupingWidth=params.get('grouping_width'), groupingTimezone=params.get('grouping_timezone')))
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        
    def measurements_v2_post(self, measurements, **kwargs):
        """
        Post a new set of measurements to the database
        You can submit multiple measurements in a \"measurements\" sub-array.  If the variable these measurements correspond to does not already exist in the database, it will be automatically added.  The request body should look something like [{\"measurements\":[{\"timestamp\":1406419860,\"value\":\"1\",\"note\":\"I am a note about back pain.\"},{\"timestamp\":1406519865,\"value\":\"3\",\"note\":\"I am another note about back pain.\"}],\"name\":\"Back Pain\",\"source\":\"QuantiModo\",\"category\":\"Symptoms\",\"combinationOperation\":\"MEAN\",\"unit\":\"/5\"}]

        :param list[Measurement] measurements: An array of measurements you want to insert. (required)
        
        :return: None
        """
        
        # verify the required parameter 'measurements' is set
        if measurements is None:
            raise ValueError("Missing the required parameter `measurements` when calling `measurements_v2_post`")
        
        all_params = ['measurements']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method measurements_v2_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/measurements/v2'.replace('{format}', 'json')
        method = 'POST'

        path_params = remove_none(dict())
        query_params = remove_none(dict())
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = params.get('measurements')

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        
    def measurements_range_get(self, **kwargs):
        """
        Get measurements range for this user
        Get Unix time-stamp (epoch time) of the user's first and last measurements taken.

        :param str sources: Enter source name to limit to specific source (varchar) 
        :param int user: If not specified, uses currently logged in user (bigint) 
        
        :return: None
        """
        
        all_params = ['sources', 'user']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method measurements_range_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/measurementsRange'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict())
        query_params = remove_none(dict(sources=params.get('sources'), user=params.get('user')))
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        








