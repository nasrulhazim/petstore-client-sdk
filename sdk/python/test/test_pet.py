# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.pet import Pet  # noqa: E501
from openapi_client.rest import ApiException

class TestPet(unittest.TestCase):
    """Pet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Pet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pet.Pet()  # noqa: E501
        if include_optional :
            return Pet(
                id = 56, 
                category = openapi_client.models.category.Category(
                    id = 56, 
                    name = '0', ), 
                name = 'doggie', 
                photo_urls = [
                    '0'
                    ], 
                tags = [
                    openapi_client.models.tag.Tag(
                        id = 56, 
                        name = '0', )
                    ], 
                status = 'available'
            )
        else :
            return Pet(
                name = 'doggie',
                photo_urls = [
                    '0'
                    ],
        )

    def testPet(self):
        """Test Pet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
