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

   ref: https://github.com/swagger-api/swagger-codegen 
"""

from __future__ import absolute_import
import base64
import urllib3

try:
    import httplib
except ImportError:
    # for python3
    import http.client as httplib
    
import sys
import logging


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Configuration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Constructor
        """
        # Default Base url
        self.host = "https://localhost/api"
        # Default api client
        self.api_client = None
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""

        # Logging Settings
        self.logging_format = '%(asctime)s %(levelname)s %(message)s'
        # Debug file location
        self.__logging_file = None
        # Debug switch
        self.__debug = False
        self.init_logger()

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        
    def init_logger(self):
        """
        Initializes logger settings.
        """
        self.logger = logging.getLogger()
        formatter = logging.Formatter(self.logging_format)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        if self.__debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.WARNING)
        if self.__logging_file:
            file_handler = logging.FileHandler(self.__logging_file)
            file_handler.setFormatter(formatter)
            self.logger.addFilter(file_handler)

    @property
    def logging_file(self):
        return self.__logging_file

    @logging_file.setter
    def logging_file(self, value):
        self.__logging_file = value
        if self.__logging_file:
            formater = logging.Formatter(self.logging_format)
            file_handler = logging.FileHandler(self.__logging_file)
            file_handler.setFormatter(formater)
            self.logger.addHandler(file_handler)

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            self.logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            self.logger.setLevel(logging.WARNING)

    def get_api_key_with_prefix(self, identifier):
        """
        Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.api_key.get(identifier) and self.api_key_prefix.get(identifier):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """
        Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(basic_auth=self.username + ':' + self.password)\
                           .get('authorization')

    def auth_settings(self):
        """
        Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'basicAuth':
                {
                    'type': 'basic',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.get_basic_auth_token()
                },
            'internalApiKey':
                {
                    'type': 'api_key',
                    'in': 'header',
                    'key': 'api_key',
                    'value': self.get_api_key_with_prefix('api_key')
                },
        }

    def to_debug_report(self):
        """
        Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)
