import logging
from models.user import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from services.user_tasks import store_last_login_info
from services.user_service import UserService
from utils import logger

def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.

           return a json response and an appropriate status code.
    """

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user_service = UserService()
    user = user_service.get_user(username)
    if bool(user) and user.check_password(password):
        access_token = create_access_token(identity=user)
        store_last_login_info.delay(user.username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


def register_user():

    data = request.get_json()
    # Get user data from request
    first_name = data.get("first_name")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not first_name or not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400
    
    user_service = UserService()
    if user_service.get_user(username):
        return jsonify({"message": f"Username:{username} already exists"}), 400

    user_obj = user_service.create_user(**data)
    return jsonify({"message": "User created successfully", 'user': user_obj.to_dict()}), 201
