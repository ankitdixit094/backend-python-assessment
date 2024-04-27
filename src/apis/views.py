import logging
from models.user import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from services.user_tasks import store_last_login_info

logger = logging.getLogger("default")


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

    user = User.objects.filter(username=username).first()
    logger.info(user.username)

    if bool(user) and user.check_password(password):
        access_token = create_access_token(identity=user)
        store_last_login_info.delay(username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


def register_user():
    data = request.get_json()
    # Get user data from request
    first_name = data.get("first_name")
    last_name = data.get("last_name", "")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Validate user data (implement proper validation)
    if not first_name or not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Check for existing user
    existing_user = User.objects.filter(username=username)
    if bool(existing_user):
        return jsonify({"error": "Username already exists"}), 400

    # Create new user
    new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
    new_user.set_password(password)
    new_user.save()

    return jsonify({"message": "User created successfully"}), 201
