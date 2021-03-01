"""
The users Blueprint handles user management for this application.
Specifically, this Blueprint allows new users to register and existing
users to log in and to log out of the application.
"""

from .users_blueprint import users_blueprint
from . import routes
