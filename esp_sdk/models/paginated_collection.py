# coding: utf-8

"""
    ESP Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class PaginatedCollection(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data=None, included=None, links=None):
        """
        PaginatedCollection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'list[object]',
            'included': 'list[object]',
            'links': 'object'
        }

        self.attribute_map = {
            'data': 'data',
            'included': 'included',
            'links': 'links'
        }

        self._data = data
        self._included = included
        self._links = links

    @property
    def data(self):
        """
        Gets the data of this PaginatedCollection.
        Array of objects

        :return: The data of this PaginatedCollection.
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this PaginatedCollection.
        Array of objects

        :param data: The data of this PaginatedCollection.
        :type: list[object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def included(self):
        """
        Gets the included of this PaginatedCollection.
        Array of related objects returned using the 'included' parameter.

        :return: The included of this PaginatedCollection.
        :rtype: list[object]
        """
        return self._included

    @included.setter
    def included(self, included):
        """
        Sets the included of this PaginatedCollection.
        Array of related objects returned using the 'included' parameter.

        :param included: The included of this PaginatedCollection.
        :type: list[object]
        """

        self._included = included

    @property
    def links(self):
        """
        Gets the links of this PaginatedCollection.
        Pagination Links

        :return: The links of this PaginatedCollection.
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PaginatedCollection.
        Pagination Links

        :param links: The links of this PaginatedCollection.
        :type: object
        """

        self._links = links

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
        if not isinstance(other, PaginatedCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
