# coding: utf-8

"""
VariablesApi.py
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


class VariablesApi(object):
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

    def v1_public_variables_get(self, **kwargs):
        """
        Get public variables
        This endpoint retrieves an array of all public variables. Public variables are things like foods, medications, symptoms, conditions, and anything not unique to a particular user. For instance, a telephone number or name would not be a public variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_variables_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_variables_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/public/variables'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

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
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_public_variables_search_search_get(self, search, **kwargs):
        """
        Get top 5 PUBLIC variables with the most correlations
        Get top 5 PUBLIC variables with the most correlations containing the entered search characters. For example, search for 'mood' as an effect. Since 'Overall Mood' has a lot of correlations with other variables, it should be in the autocomplete list.<br>Supported filter parameters:<br><ul><li><b>category</b> - Category of Variable</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_public_variables_search_search_get(search, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search query can be some fraction of a variable name. (required)
        :param str effect_or_cause: Allows us to specify which column in the `correlations` table will be searched. Choices are effect or cause.
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'search' is set
        if search is None:
            raise ValueError("Missing the required parameter `search` when calling `v1_public_variables_search_search_get`")

        all_params = ['search', 'effect_or_cause', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_variables_search_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/public/variables/search/{search}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'search' in params:
            path_params['search'] = params['search']

        query_params = {}
        if 'effect_or_cause' in params:
            query_params['effectOrCause'] = params['effect_or_cause']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

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
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_user_variables_post(self, sharing_data, **kwargs):
        """
        Update User Settings for a Variable
        Users can change things like the display name for a variable. They can also change the parameters used in analysis of that variable such as the expected duration of action for a variable to have an effect, the estimated delay before the onset of action. In order to filter out erroneous data, they are able to set the maximum and minimum reasonable daily values for a variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_variables_post(sharing_data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserVariables sharing_data: Variable user settings data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'sharing_data' is set
        if sharing_data is None:
            raise ValueError("Missing the required parameter `sharing_data` when calling `v1_user_variables_post`")

        all_params = ['sharing_data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_user_variables_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/userVariables'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'sharing_data' in params:
            body_params = params['sharing_data']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_variable_categories_get(self, **kwargs):
        """
        Variable categories
        The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variable_categories_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[VariableCategory]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variable_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variableCategories'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

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
                                            response_type='list[VariableCategory]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_variables_get(self, **kwargs):
        """
        Get variables by the category name
        Get variables by the category name. <br>Supported filter parameters:<br><ul><li><b>name</b> - Original name of the variable (supports exact name match only)</li><li><b>lastUpdated</b> - Filter by the last time any of the properties of the variable were changed. Uses UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>source</b> - The name of the data source that created the variable (supports exact name match only). So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here</li><li><b>latestMeasurementTime</b> - Filter variables based on the last time a measurement for them was created or updated in the UTC format \"YYYY-MM-DDThh:mm:ss\"</li><li><b>numberOfMeasurements</b> - Filter variables by the total number of measurements that they have. This could be used of you want to filter or sort by popularity.</li><li><b>lastSource</b> - Limit variables to those which measurements were last submitted by a specific source. So if you have a client application and you only want variables that were last updated by your app, you can include the name of your app here. (supports exact name match only)</li></ul><br>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: User id
        :param str category: Filter data by category
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :param int sort: Sort by given field. If the field is prefixed with `-, it will sort in descending order.
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'category', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'user_id' in params:
            query_params['userId'] = params['user_id']
        if 'category' in params:
            query_params['category'] = params['category']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

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
        auth_settings = ['basicAuth', 'oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_variables_post(self, variable_name, **kwargs):
        """
        Create Variables
        Allows the client to create a new variable in the `variables` table.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_post(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VariablesNew variable_name: Original name for the variable. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_post`")

        all_params = ['variable_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'variable_name' in params:
            body_params = params['variable_name']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_variables_search_search_get(self, search, **kwargs):
        """
        Get variables by search query
        Get variables containing the search characters for which the currently logged in user has measurements. Used to provide auto-complete function in variable search boxes.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_search_search_get(search, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search query which may be an entire variable name or a fragment of one. (required)
        :param str category_name: Filter variables by category name. The variable categories include Activity, Causes of Illness, Cognitive Performance, Conditions, Environment, Foods, Location, Miscellaneous, Mood, Nutrition, Physical Activity, Physique, Sleep, Social Interactions, Symptoms, Treatments, Vital Signs, and Work.
        :param str source: Specify a data source name to only return variables from a specific data source.
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0.
        :param int offset: Now suppose you wanted to show results 11-20. You'd set the offset to 10 and the limit to 10.
        :return: list[Variable]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'search' is set
        if search is None:
            raise ValueError("Missing the required parameter `search` when calling `v1_variables_search_search_get`")

        all_params = ['search', 'category_name', 'source', 'limit', 'offset']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_search_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables/search/{search}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'search' in params:
            path_params['search'] = params['search']

        query_params = {}
        if 'category_name' in params:
            query_params['categoryName'] = params['category_name']
        if 'source' in params:
            query_params['source'] = params['source']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']

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
                                            response_type='list[Variable]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_variables_variable_name_get(self, variable_name, **kwargs):
        """
        Get info about a variable
        Get all of the settings and information about a variable by its name. If the logged in user has modified the settings for the variable, these will be provided instead of the default settings for that variable.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_variables_variable_name_get(variable_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str variable_name: Variable name (required)
        :return: Variable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_get`")

        all_params = ['variable_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_variables_variable_name_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables/{variableName}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'variable_name' in params:
            path_params['variableName'] = params['variable_name']

        query_params = {}

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
                                            response_type='Variable',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
