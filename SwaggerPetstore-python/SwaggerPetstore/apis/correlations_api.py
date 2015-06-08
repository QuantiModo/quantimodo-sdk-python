#!/usr/bin/env python
# coding: utf-8

"""
CorrelationsApi.py
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

class CorrelationsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client
    
    def correlations_get(self, **kwargs):
        """
        Get correlations
        Get correlations

        :param str effect: ORIGINAL variable name of the effect variable for which the user desires correlations 
        :param str cause: ORIGINAL variable name of the cause variable for which the user desires correlations 
        
        :return: list[Correlation]
        """
        
        all_params = ['effect', 'cause']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method correlations_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/correlations'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict())
        query_params = remove_none(dict(effect=params.get('effect'), cause=params.get('cause')))
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
                                            response='list[Correlation]')
        
        return response
        
    def public_correlations_search_search_get(self, search, effect_or_cause, **kwargs):
        """
        Get average correlations for variables containing search term
        Returns the average correlations from all users for all public variables that contain the characters in the search query. Returns average of all users public variable correlations with a specified cause or effect.

        :param str search: Name of the variable that you want to know the causes or effects of. (required)
        :param str effect_or_cause: Specifies whether to return the effects or causes of the searched variable. (required)
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'search' is set
        if search is None:
            raise ValueError("Missing the required parameter `search` when calling `public_correlations_search_search_get`")
        
        # verify the required parameter 'effect_or_cause' is set
        if effect_or_cause is None:
            raise ValueError("Missing the required parameter `effect_or_cause` when calling `public_correlations_search_search_get`")
        
        all_params = ['search', 'effect_or_cause']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method public_correlations_search_search_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/public/correlations/search/{search}'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(search=params.get('search')))
        query_params = remove_none(dict(effectOrCause=params.get('effect_or_cause')))
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
                                            response='list[Correlation]')
        
        return response
        
    def v1_correlations_post(self, body, **kwargs):
        """
        Add correlation or/and vote for it
        Add correlation or/and vote for it

        :param PostCorrelation body: Provides correlation data (required)
        
        :return: None
        """
        
        # verify the required parameter 'body' is set
        if body is None:
            raise ValueError("Missing the required parameter `body` when calling `v1_correlations_post`")
        
        all_params = ['body']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_correlations_post" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/correlations'.replace('{format}', 'json')
        method = 'POST'

        path_params = remove_none(dict())
        query_params = remove_none(dict())
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = params.get('body')

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        
    def v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get(self, organization_id, user_id, variable_name, organization_token, **kwargs):
        """
        Search user correlations for a given effect
        Returns average of all correlations and votes for all user cause variables for a given effect. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

        :param int organization_id: Organization ID (required)
        :param int user_id: User id (required)
        :param str variable_name: Effect variable name (required)
        :param str organization_token: Organization access token (required)
        :param str include_public: Include bublic correlations, Can be \"1\" or empty. 
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'organization_id' is set
        if organization_id is None:
            raise ValueError("Missing the required parameter `organization_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        
        # verify the required parameter 'organization_token' is set
        if organization_token is None:
            raise ValueError("Missing the required parameter `organization_token` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get`")
        
        all_params = ['organization_id', 'user_id', 'variable_name', 'organization_token', 'include_public']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_organizations_organization_id_users_user_id_variables_variable_name_causes_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/organizations/{organizationId}/users/{userId}/variables/{variableName}/causes'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(organizationId=params.get('organization_id'), userId=params.get('user_id'), variableName=params.get('variable_name')))
        query_params = remove_none(dict(organization_token=params.get('organization_token'), include_public=params.get('include_public')))
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
                                            response='list[Correlation]')
        
        return response
        
    def v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get(self, organization_id, user_id, variable_name, organization_token, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user cause variables for a given effect. If parameter \"include_public\" is used, it also returns public correlations. User correlation overwrites or supersedes public correlation.

        :param int organization_id: Organization ID (required)
        :param int user_id: User id (required)
        :param str variable_name: Cause variable name (required)
        :param str organization_token: Organization access token (required)
        :param str include_public: Include bublic correlations, Can be \"1\" or empty. 
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'organization_id' is set
        if organization_id is None:
            raise ValueError("Missing the required parameter `organization_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        
        # verify the required parameter 'user_id' is set
        if user_id is None:
            raise ValueError("Missing the required parameter `user_id` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        
        # verify the required parameter 'organization_token' is set
        if organization_token is None:
            raise ValueError("Missing the required parameter `organization_token` when calling `v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get`")
        
        all_params = ['organization_id', 'user_id', 'variable_name', 'organization_token', 'include_public']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_organizations_organization_id_users_user_id_variables_variable_name_effects_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/organizations/{organizationId}/users/{userId}/variables/{variableName}/effects'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(organizationId=params.get('organization_id'), userId=params.get('user_id'), variableName=params.get('variable_name')))
        query_params = remove_none(dict(organization_token=params.get('organization_token'), include_public=params.get('include_public')))
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
                                            response='list[Correlation]')
        
        return response
        
    def v1_variables_variable_name_causes_get(self, variable_name, **kwargs):
        """
        Search user correlations for a given effect
        Returns average of all correlations and votes for all user cause variables for a given effect

        :param str variable_name: Effect variable name (required)
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_causes_get`")
        
        all_params = ['variable_name']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_variables_variable_name_causes_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables/{variableName}/causes'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(variableName=params.get('variable_name')))
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
                                            response='list[Correlation]')
        
        return response
        
    def v1_variables_variable_name_effects_get(self, variable_name, **kwargs):
        """
        Search user correlations for a given cause
        Returns average of all correlations and votes for all user effect variables for a given cause

        :param str variable_name: Cause variable name (required)
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_effects_get`")
        
        all_params = ['variable_name']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_variables_variable_name_effects_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables/{variableName}/effects'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(variableName=params.get('variable_name')))
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
                                            response='list[Correlation]')
        
        return response
        
    def v1_variables_variable_name_public_causes_get(self, variable_name, **kwargs):
        """
        Search public correlations for a given effect
        Returns average of all correlations and votes for all public cause variables for a given effect

        :param str variable_name: Effect variable name (required)
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_public_causes_get`")
        
        all_params = ['variable_name']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_variables_variable_name_public_causes_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables/{variableName}/public/causes'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(variableName=params.get('variable_name')))
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
                                            response='list[Correlation]')
        
        return response
        
    def v1_variables_variable_name_public_effects_get(self, variable_name, **kwargs):
        """
        Search public correlations for a given cause
        Returns average of all correlations and votes for all public cause variables for a given cause

        :param str variable_name: Cause variable name (required)
        
        :return: list[Correlation]
        """
        
        # verify the required parameter 'variable_name' is set
        if variable_name is None:
            raise ValueError("Missing the required parameter `variable_name` when calling `v1_variables_variable_name_public_effects_get`")
        
        all_params = ['variable_name']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_variables_variable_name_public_effects_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/variables/{variableName}/public/effects'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict(variableName=params.get('variable_name')))
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
                                            response='list[Correlation]')
        
        return response
        








