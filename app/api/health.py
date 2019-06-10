"""
Health Views.
"""

import logging

from . import constants, API

logger = logging.getLogger(__name__)


class HealthAPI(API):
    """
    Health views.
    """

    def _get(self) -> tuple:
        """
        Get health view.
        Error handling is performed by the parent class method.
        """
        logger.debug("Health-check")
        return {
            constants.Health.STATUS: constants.Health.ALIVE,
        }
