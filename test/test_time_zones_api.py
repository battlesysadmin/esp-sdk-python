# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.time_zones_api import TimeZonesApi


class TestTimeZonesApi(unittest.TestCase):
    """ TimeZonesApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.time_zones_api.TimeZonesApi()

    def tearDown(self):
        pass

    def test_list(self):
        """
        Test case for list

        A successful call to this API returns a list of time zones.
        """
        pass


if __name__ == '__main__':
    unittest.main()
