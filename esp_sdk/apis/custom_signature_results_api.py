# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomSignatureResultsApi(object):
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

    def create(self, code, custom_signature_definition_id, external_account_id, language, region_id, **kwargs):
        """
        Create a(n) Result
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(code, custom_signature_definition_id, external_account_id, language, region_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code: The code to run (required)
        :param int custom_signature_definition_id: ID of the custom signature definition this result should belong to. (required)
        :param int external_account_id: ID of the external account the code should run for. (required)
        :param str language: The language of the code (required)
        :param int region_id: ID of the region the code should run for. (required)
        :param str region: Code of the region the result code should run for. Ex: us-east-1. This can be sent instead of region_id
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(code, custom_signature_definition_id, external_account_id, language, region_id, **kwargs)
        else:
            (data) = self.create_with_http_info(code, custom_signature_definition_id, external_account_id, language, region_id, **kwargs)
            return data

    def create_with_http_info(self, code, custom_signature_definition_id, external_account_id, language, region_id, **kwargs):
        """
        Create a(n) Result
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(code, custom_signature_definition_id, external_account_id, language, region_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code: The code to run (required)
        :param int custom_signature_definition_id: ID of the custom signature definition this result should belong to. (required)
        :param int external_account_id: ID of the external account the code should run for. (required)
        :param str language: The language of the code (required)
        :param int region_id: ID of the region the code should run for. (required)
        :param str region: Code of the region the result code should run for. Ex: us-east-1. This can be sent instead of region_id
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'custom_signature_definition_id', 'external_account_id', 'language', 'region_id', 'region']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params) or (params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `create`")
        # verify the required parameter 'custom_signature_definition_id' is set
        if ('custom_signature_definition_id' not in params) or (params['custom_signature_definition_id'] is None):
            raise ValueError("Missing the required parameter `custom_signature_definition_id` when calling `create`")
        # verify the required parameter 'external_account_id' is set
        if ('external_account_id' not in params) or (params['external_account_id'] is None):
            raise ValueError("Missing the required parameter `external_account_id` when calling `create`")
        # verify the required parameter 'language' is set
        if ('language' not in params) or (params['language'] is None):
            raise ValueError("Missing the required parameter `language` when calling `create`")
        # verify the required parameter 'region_id' is set
        if ('region_id' not in params) or (params['region_id'] is None):
            raise ValueError("Missing the required parameter `region_id` when calling `create`")


        collection_formats = {}

        resource_path = '/api/v2/custom_signature_results.json_api'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'code' in params:
            form_params.append(('code', params['code']))
        if 'custom_signature_definition_id' in params:
            form_params.append(('custom_signature_definition_id', params['custom_signature_definition_id']))
        if 'external_account_id' in params:
            form_params.append(('external_account_id', params['external_account_id']))
        if 'language' in params:
            form_params.append(('language', params['language']))
        if 'region_id' in params:
            form_params.append(('region_id', params['region_id']))
        if 'region' in params:
            form_params.append(('region', params['region']))

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Result',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, **kwargs):
        """
        Get a list of Results
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param dict(str, str) page: Page Number
        :param dict(str, str) filter: Filter Params for Searching
        :param str include: Included Objects
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get a list of Results
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param dict(str, str) page: Page Number
        :param dict(str, str) filter: Filter Params for Searching
        :param str include: Included Objects
        :return: PaginatedCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'filter', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v2/custom_signature_results.json_api'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'page' in params:
            form_params.append(('page', params['page']))
        if 'filter' in params:
            form_params.append(('filter', params['filter']))

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaginatedCollection',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def show(self, id, **kwargs):
        """
        Show a single Result
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Result Id (required)
        :param str include: Included Objects
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_with_http_info(id, **kwargs)
        else:
            (data) = self.show_with_http_info(id, **kwargs)
            return data

    def show_with_http_info(self, id, **kwargs):
        """
        Show a single Result
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Result Id (required)
        :param str include: Included Objects
        :return: Result
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `show`")


        collection_formats = {}

        resource_path = '/api/v2/custom_signature_results/{id}.json_api'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Result',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
