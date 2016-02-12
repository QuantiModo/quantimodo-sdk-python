# coding: utf-8

"""
UserVariableRelationshipApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserVariableRelationshipApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def user_variable_relationships_get(self, **kwargs):
        """
        Get all UserVariableRelationships
        Get all UserVariableRelationships

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_variable_relationships_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int id: id
        :param str confidence_level: Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors
        :param float confidence_score: A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors
        :param str direction: Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values.
        :param int duration_of_action: Estimated number of seconds following the onset delay in which a stimulus produces a perceivable effect
        :param str error_message: error_message
        :param int onset_delay: Estimated number of seconds that pass before a stimulus produces a perceivable effect
        :param int outcome_variable_id: Variable ID for the outcome variable
        :param int predictor_variable_id: Variable ID for the predictor variable
        :param int predictor_unit_id: ID for default unit of the predictor variable
        :param float sinn_rank: A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting.
        :param str strength_level: Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores.
        :param float strength_score: A value represented to the size of the effect which the predictor appears to have on the outcome.
        :param int user_id: user_id
        :param str vote: vote
        :param float value_predicting_high_outcome: Value for the predictor variable (in it's default unit) which typically precedes an above average outcome value
        :param float value_predicting_low_outcome: Value for the predictor variable (in it's default unit) which typically precedes a below average outcome value
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'id', 'confidence_level', 'confidence_score', 'direction', 'duration_of_action', 'error_message', 'onset_delay', 'outcome_variable_id', 'predictor_variable_id', 'predictor_unit_id', 'sinn_rank', 'strength_level', 'strength_score', 'user_id', 'vote', 'value_predicting_high_outcome', 'value_predicting_low_outcome', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_variable_relationships_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/userVariableRelationships'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'confidence_level' in params:
            query_params['confidence_level'] = params['confidence_level']
        if 'confidence_score' in params:
            query_params['confidence_score'] = params['confidence_score']
        if 'direction' in params:
            query_params['direction'] = params['direction']
        if 'duration_of_action' in params:
            query_params['duration_of_action'] = params['duration_of_action']
        if 'error_message' in params:
            query_params['error_message'] = params['error_message']
        if 'onset_delay' in params:
            query_params['onset_delay'] = params['onset_delay']
        if 'outcome_variable_id' in params:
            query_params['outcome_variable_id'] = params['outcome_variable_id']
        if 'predictor_variable_id' in params:
            query_params['predictor_variable_id'] = params['predictor_variable_id']
        if 'predictor_unit_id' in params:
            query_params['predictor_unit_id'] = params['predictor_unit_id']
        if 'sinn_rank' in params:
            query_params['sinn_rank'] = params['sinn_rank']
        if 'strength_level' in params:
            query_params['strength_level'] = params['strength_level']
        if 'strength_score' in params:
            query_params['strength_score'] = params['strength_score']
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']
        if 'vote' in params:
            query_params['vote'] = params['vote']
        if 'value_predicting_high_outcome' in params:
            query_params['value_predicting_high_outcome'] = params['value_predicting_high_outcome']
        if 'value_predicting_low_outcome' in params:
            query_params['value_predicting_low_outcome'] = params['value_predicting_low_outcome']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2008',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_variable_relationships_post(self, **kwargs):
        """
        Store UserVariableRelationship
        Store UserVariableRelationship

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_variable_relationships_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param UserVariableRelationship body: UserVariableRelationship that should be stored
        :return: InlineResponse20029
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_variable_relationships_post" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/userVariableRelationships'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse20029',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_variable_relationships_id_get(self, id, **kwargs):
        """
        Get UserVariableRelationship
        Get UserVariableRelationship

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_variable_relationships_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of UserVariableRelationship (required)
        :param str access_token: User's OAuth2 access token
        :return: InlineResponse20029
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'access_token']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_variable_relationships_id_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_variable_relationships_id_get`")

        resource_path = '/userVariableRelationships/{id}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse20029',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_variable_relationships_id_put(self, id, **kwargs):
        """
        Update UserVariableRelationship
        Update UserVariableRelationship

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_variable_relationships_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of UserVariableRelationship (required)
        :param str access_token: User's OAuth2 access token
        :param UserVariableRelationship body: UserVariableRelationship that should be updated
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'access_token', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_variable_relationships_id_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_variable_relationships_id_put`")

        resource_path = '/userVariableRelationships/{id}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_variable_relationships_id_delete(self, id, **kwargs):
        """
        Delete UserVariableRelationship
        Delete UserVariableRelationship

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_variable_relationships_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of UserVariableRelationship (required)
        :param str access_token: User's OAuth2 access token
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'access_token']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_variable_relationships_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_variable_relationships_id_delete`")

        resource_path = '/userVariableRelationships/{id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
