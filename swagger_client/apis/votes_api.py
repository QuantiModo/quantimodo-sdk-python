# coding: utf-8

"""
VotesApi.py
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

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class VotesApi(object):
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

    def v1_votes_post(self, cause, effect, correlation, **kwargs):
        """
        Post or update vote
        This is to enable users to indicate their opinion on the plausibility of a causal relationship between a treatment and outcome. QuantiModo incorporates crowd-sourced plausibility estimations into their algorithm. This is done allowing user to indicate their view of the plausibility of each relationship with thumbs up/down buttons placed next to each prediction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_votes_post(cause, effect, correlation, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cause: Cause variable name (required)
        :param str effect: Effect variable name (required)
        :param float correlation: Correlation value (required)
        :param bool vote: Vote: 0 (for implausible) or 1 (for plausible)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'cause' is set
        if cause is None:
            raise ValueError("Missing the required parameter `cause` when calling `v1_votes_post`")
        # verify the required parameter 'effect' is set
        if effect is None:
            raise ValueError("Missing the required parameter `effect` when calling `v1_votes_post`")
        # verify the required parameter 'correlation' is set
        if correlation is None:
            raise ValueError("Missing the required parameter `correlation` when calling `v1_votes_post`")

        all_params = ['cause', 'effect', 'correlation', 'vote']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_votes_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/votes'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}
        if 'cause' in params:
            query_params['cause'] = params['cause']
        if 'effect' in params:
            query_params['effect'] = params['effect']
        if 'correlation' in params:
            query_params['correlation'] = params['correlation']
        if 'vote' in params:
            query_params['vote'] = params['vote']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='CommonResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_votes_delete_post(self, cause, effect, **kwargs):
        """
        Delete vote
        Delete previously posted vote

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_votes_delete_post(cause, effect, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cause: Cause variable name (required)
        :param str effect: Effect variable name (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'cause' is set
        if cause is None:
            raise ValueError("Missing the required parameter `cause` when calling `v1_votes_delete_post`")
        # verify the required parameter 'effect' is set
        if effect is None:
            raise ValueError("Missing the required parameter `effect` when calling `v1_votes_delete_post`")

        all_params = ['cause', 'effect']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_votes_delete_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/votes/delete'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}
        if 'cause' in params:
            query_params['cause'] = params['cause']
        if 'effect' in params:
            query_params['effect'] = params['effect']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='CommonResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
