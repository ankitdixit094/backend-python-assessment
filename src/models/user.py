from mongoengine import StringField, EmailField, Document
from werkzeug.security import generate_password_hash, check_password_hash
from app import db




class User(db.Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=False)
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password_hash = db.StringField(required=True)
    last_login = db.DateTimeField(required=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Converts the user object to a dictionary."""
        user_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'last_login': self.last_login
        }
        return user_dict

