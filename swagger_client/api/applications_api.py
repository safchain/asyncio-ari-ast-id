# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ApplicationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def applications_application_name_event_filter_put(self, application_name, **kwargs):  # noqa: E501
        """Filter application events types.  # noqa: E501

        Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:<br /><br />\"allowed\" - Specifies an allowed list of event types<br />\"disallowed\" - Specifies a disallowed list of event types<br /><br />Further, each of those key's value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:<br /><br />\"type\" - The type name of the event to filter<br /><br />The value must be the string name (case sensitive) of the event type that needs filtering. For example:<br /><br />{ \"allowed\": [ { \"type\": \"StasisStart\" }, { \"type\": \"StasisEnd\" } ] }<br /><br />As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.<br /><br />The following rules apply:<br /><br />* If the body is empty, both the allowed and disallowed filters are set empty.<br />* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).<br />* If only one list type is given then only that type is set. The other type is not updated.<br />* An empty \"allowed\" list means all events are allowed.<br />* An empty \"disallowed\" list means no events are disallowed.<br />* Disallowed events take precedence over allowed events if the event type is specified in both lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_event_filter_put(application_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :param object filter: Specify which event types to allow/disallow
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applications_application_name_event_filter_put_with_http_info(application_name, **kwargs)  # noqa: E501
        else:
            (data) = self.applications_application_name_event_filter_put_with_http_info(application_name, **kwargs)  # noqa: E501
            return data

    def applications_application_name_event_filter_put_with_http_info(self, application_name, **kwargs):  # noqa: E501
        """Filter application events types.  # noqa: E501

        Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:<br /><br />\"allowed\" - Specifies an allowed list of event types<br />\"disallowed\" - Specifies a disallowed list of event types<br /><br />Further, each of those key's value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:<br /><br />\"type\" - The type name of the event to filter<br /><br />The value must be the string name (case sensitive) of the event type that needs filtering. For example:<br /><br />{ \"allowed\": [ { \"type\": \"StasisStart\" }, { \"type\": \"StasisEnd\" } ] }<br /><br />As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.<br /><br />The following rules apply:<br /><br />* If the body is empty, both the allowed and disallowed filters are set empty.<br />* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).<br />* If only one list type is given then only that type is set. The other type is not updated.<br />* An empty \"allowed\" list means all events are allowed.<br />* An empty \"disallowed\" list means no events are disallowed.<br />* Disallowed events take precedence over allowed events if the event type is specified in both lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_event_filter_put_with_http_info(application_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :param object filter: Specify which event types to allow/disallow
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_name', 'x_asterisk_id', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_event_filter_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_name' is set
        if ('application_name' not in params or
                params['application_name'] is None):
            raise ValueError("Missing the required parameter `application_name` when calling `applications_application_name_event_filter_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in params:
            path_params['applicationName'] = params['application_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filter' in params:
            body_params = params['filter']
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/applications/{applicationName}/eventFilter', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applications_application_name_get(self, application_name, **kwargs):  # noqa: E501
        """Get details of an application.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_get(application_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applications_application_name_get_with_http_info(application_name, **kwargs)  # noqa: E501
        else:
            (data) = self.applications_application_name_get_with_http_info(application_name, **kwargs)  # noqa: E501
            return data

    def applications_application_name_get_with_http_info(self, application_name, **kwargs):  # noqa: E501
        """Get details of an application.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_get_with_http_info(application_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_name', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_name' is set
        if ('application_name' not in params or
                params['application_name'] is None):
            raise ValueError("Missing the required parameter `application_name` when calling `applications_application_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in params:
            path_params['applicationName'] = params['application_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/applications/{applicationName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applications_application_name_subscription_delete(self, application_name, event_source, **kwargs):  # noqa: E501
        """Unsubscribe an application from an event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_subscription_delete(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param list[str] event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applications_application_name_subscription_delete_with_http_info(application_name, event_source, **kwargs)  # noqa: E501
        else:
            (data) = self.applications_application_name_subscription_delete_with_http_info(application_name, event_source, **kwargs)  # noqa: E501
            return data

    def applications_application_name_subscription_delete_with_http_info(self, application_name, event_source, **kwargs):  # noqa: E501
        """Unsubscribe an application from an event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_subscription_delete_with_http_info(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param list[str] event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_name', 'event_source', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_subscription_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_name' is set
        if ('application_name' not in params or
                params['application_name'] is None):
            raise ValueError("Missing the required parameter `application_name` when calling `applications_application_name_subscription_delete`")  # noqa: E501
        # verify the required parameter 'event_source' is set
        if ('event_source' not in params or
                params['event_source'] is None):
            raise ValueError("Missing the required parameter `event_source` when calling `applications_application_name_subscription_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in params:
            path_params['applicationName'] = params['application_name']  # noqa: E501

        query_params = []
        if 'event_source' in params:
            query_params.append(('eventSource', params['event_source']))  # noqa: E501
            collection_formats['eventSource'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/applications/{applicationName}/subscription', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applications_application_name_subscription_post(self, application_name, event_source, **kwargs):  # noqa: E501
        """Subscribe an application to a event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_subscription_post(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param list[str] event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applications_application_name_subscription_post_with_http_info(application_name, event_source, **kwargs)  # noqa: E501
        else:
            (data) = self.applications_application_name_subscription_post_with_http_info(application_name, event_source, **kwargs)  # noqa: E501
            return data

    def applications_application_name_subscription_post_with_http_info(self, application_name, event_source, **kwargs):  # noqa: E501
        """Subscribe an application to a event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_application_name_subscription_post_with_http_info(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: Application's name (required)
        :param list[str] event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_name', 'event_source', 'x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_subscription_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_name' is set
        if ('application_name' not in params or
                params['application_name'] is None):
            raise ValueError("Missing the required parameter `application_name` when calling `applications_application_name_subscription_post`")  # noqa: E501
        # verify the required parameter 'event_source' is set
        if ('event_source' not in params or
                params['event_source'] is None):
            raise ValueError("Missing the required parameter `event_source` when calling `applications_application_name_subscription_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in params:
            path_params['applicationName'] = params['application_name']  # noqa: E501

        query_params = []
        if 'event_source' in params:
            query_params.append(('eventSource', params['event_source']))  # noqa: E501
            collection_formats['eventSource'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/applications/{applicationName}/subscription', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applications_get(self, **kwargs):  # noqa: E501
        """List all applications.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: list[Application]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applications_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.applications_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def applications_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all applications.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applications_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_asterisk_id: Asterisk ID used to route the request through the API Gateway
        :return: list[Application]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_asterisk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in params:
            header_params['X-Asterisk-ID'] = params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Application]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)