"""Blueprint

- blueprint registration
- routes/api declaration 
- for each api, there is controller function acting as a middeware
    - perform basic checks
    - perform permissions
    - make response object
"""
from flask import Blueprint
from auth.v2.login import login_api
from auth.v2.logout import logout_api
from auth.v2.me import me_api

auth_bp = Blueprint('auth_v2', __name__,)

@auth_bp.route('/login')
def login_controller():
    return login_api()

@auth_bp.route('/logout')
def logout_controller():
    return logout_api()

@auth_bp.route('/me')
def me_controller():
    return me_api()
