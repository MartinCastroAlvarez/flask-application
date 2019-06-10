"""
Testing health API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import health
from app.api import errors
from app.api import constants


class TestHealthEndpoint(unittest.TestCase):
    """
    Testing health endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = health.HealthAPI().get()
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Health.ALIVE, str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = health.HealthAPI().post()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = health.HealthAPI().put()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = health.HealthAPI().delete()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))
