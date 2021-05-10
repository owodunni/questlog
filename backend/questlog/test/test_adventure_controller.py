# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from questlog.generated.models.adventure import Adventure  # noqa: E501
from questlog.test import BaseTestCase


class TestAdventureController(BaseTestCase):
    """AdventureController integration test stubs"""

    def test_get_adventure(self):
        """Test case for get_adventure

        Get all adventures
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open("/adventure", method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_adventure_guid(self):
        """Test case for get_adventure_guid

        Find adventure by Id
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/adventure/{adventure_id}".format(adventure_id="adventure_id_example"),
            method="GET",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_post_adventure(self):
        """Test case for post_adventure

        Add a new adventure
        """
        body = Adventure()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/adventure",
            method="POST",
            headers=headers,
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
