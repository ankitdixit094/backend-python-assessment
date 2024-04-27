from app import jwt
from models.user import User

class UserService(object):
    """
    service function for user related business logic
    """

    def login_user(self):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """

        pass

    # def create_user(self, first_name, last_name, username, email, password):
    #     logger.info(f"first_name:{first_name}, last_name:{last_name}, username:{username}, email:{email}, password:{password}")
    #     # Validate user data (implement proper validation)
    #     if not first_name or not username or not email or not password:
    #         return jsonify({"error": "Missing required fields"}), 400

    #     # Check for existing user
    #     existing_user = User.objects.filter(username=username)
    #     if bool(existing_user):
    #         return jsonify({"error": "Username already exists"}), 400

    #     # Create new user
    #     new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
    #     new_user.set_password(password)
    #     new_user.save()


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.objects.filter(id=identity).first()