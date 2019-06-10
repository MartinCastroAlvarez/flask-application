"""
API Views.

Login is managed by the controller.
Views only check if the user is authenticated.
"""

import logging

from werkzeug.exceptions import Unauthorized, NotFound

from flask.views import MethodView
from flask import jsonify, request

from . import constants
from . import errors

logger = logging.getLogger(__name__)


class API(MethodView):
    """
    Parent class for all views.
    All views in this app should inherit from this class definition.
    """

    ERROR_MAP = {
        Unauthorized: errors.AuthException(),
        NotFound: errors.EndpointNotFoundException(),
    }

    def __call(self, method: str, callback: object, *args, **kwargs) -> tuple:
        """
        Handler for all methods.
        """
        try:
            logger.debug("[%s] [%s] [%s]", method, self, request.json)
            response = callback(*args, **kwargs) or {}
            logger.debug("[%s] [%s] [%s]", method, self, response)
        except Exception as e:
            logger.exception("[%s] [%s] [FAILED]", method, self)
            e = self.ERROR_MAP.get(e.__class__, e)
            if not isinstance(e, errors.MariaException):
                e = errors.MariaException(str(e))
            return jsonify({
                constants.Error.PLURAL: e.to_json(),
            }), e.code
        else:
            logger.exception("[%s] [%s] [OK]", method, self)
            return jsonify(response)
        finally:
            logger.exception("[%s] [%s] [END]", method, self)

    def get(self, *args, **kwargs) -> tuple:
        """
        GET request.

        All exceptions will be handled by this parent method.

        If the child class does not override this method,
        then a 405 error is returned.

        404 and 403 errors are caught by custom exceptions.
        """
        return self.__call("GET", self._get, *args, **kwargs)

    def post(self, *args, **kwargs) -> tuple:
        """
        POST request.

        All exceptions will be handled by this parent method.

        If the child class does not override this method,
        then a 405 error is returned.

        404 and 403 errors are caught by custom exceptions.
        """
        return self.__call("POST", self._post, *args, **kwargs)

    def delete(self, *args, **kwargs) -> tuple:
        """
        DELETE request.

        All exceptions will be handled by this parent method.

        If the child class does not override this method,
        then a 405 error is returned.

        404 and 403 errors are caught by custom exceptions.
        """
        return self.__call("DELETE", self._delete, *args, **kwargs)

    def put(self, *args, **kwargs) -> tuple:
        """
        PUT request.

        All exceptions will be handled by this parent method.

        If the child class does not override this method,
        then a 405 error is returned.

        404 and 403 errors are caught by custom exceptions.
        """
        return self.__call("PUT", self._put, *args, **kwargs)

    def _get(self, *args, **kwargs) -> dict:
        """
        Override this method in subclasses.
        """
        raise errors.MethodNotImplementedException()

    def _post(self, *args, **kwargs) -> dict:
        """
        Override this method in subclasses.
        """
        raise errors.MethodNotImplementedException()

    def _delete(self, *args, **kwargs) -> dict:
        """
        Override this method in subclasses.
        """
        raise errors.MethodNotImplementedException()

    def _put(self, *args, **kwargs) -> dict:
        """
        Override this method in subclasses.
        """
        raise errors.MethodNotImplementedException()
