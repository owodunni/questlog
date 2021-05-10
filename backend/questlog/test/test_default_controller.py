# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from questlog.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_healthcheck(self):
        """Test case for get_healthcheck

        Server healtcheck
        """
        headers = {}
        response = self.client.open("/healthcheck", method="GET", headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
