import click
from services.user_service import UserService

@click.command()
@click.option('--first_name', prompt='Enter first name', help='The first name of the user', required=True)
@click.option('--username', prompt='Enter username', help='The username of the user', required=True)
@click.option('--email', prompt='Enter email', help='The email of the user', required=True)
@click.option('--password', prompt='Enter password', hide_input=True, help='The password of the user', required=True)
@click.option('--last_name', prompt='Enter last name', help='The last name of the user')
def createuser(first_name, username, email, password, last_name):
    user_service = UserService()
    if user_service.get_user(username):
        raise click.ClickException(f"Username '{username}' already exists")
    
    user_obj = user_service.create_user(first_name, last_name, username, email, password)
    click.echo(f"User Created: {user_obj.to_dict()}")

if __name__ == '__main__':
    createuser()
