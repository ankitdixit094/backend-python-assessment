from app import jwt
from models.user import User
from utils import logger

class UserService:
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

    def get_user(self, username):
        return User.objects.filter(username=username).first()


    def create_user(self, first_name, last_name, username, email, password):
        # Create new user
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return new_user


@jwt.user_identity_loader
def user_identity_lookup(user):
    logger.info(f"1={user}")
    logger.info(f"1={user.id}")
    return user.id

@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    logger.info(f"2={identity}")
    logger.info(f"2={identity.id}")
    return User.objects.filter(id=identity).first()