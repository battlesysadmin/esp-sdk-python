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
from esp_sdk.apis.custom_signature_stats_api import CustomSignatureStatsApi


class TestCustomSignatureStatsApi(unittest.TestCase):
    """ CustomSignatureStatsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.custom_signature_stats_api.CustomSignatureStatsApi()

    def tearDown(self):
        pass

    def test_list(self):
        """
        Test case for list

        A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.
        """
        pass


if __name__ == '__main__':
    unittest.main()
