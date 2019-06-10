"""
Application models.

The DB connector is initialized here.
"""

import logging

from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

logger.debug("Creating DB connector.")
db = SQLAlchemy(session_options=dict(autoflush=False))
