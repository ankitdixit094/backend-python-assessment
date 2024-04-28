from celery.utils.log import get_task_logger
from datetime import datetime
from app import celery
from models.user import User
from services.user_service import UserService


logger = get_task_logger(__name__)



@celery.task(name='tasks.store_last_login_info')
def store_last_login_info(username):
    try:
        user_service = UserService()
        existing_user = user_service.get_user(username)
        if not bool(existing_user):
            logger.info(f'User {username} doesn\'t exists')
        existing_user.last_login = datetime.now()
        existing_user.save()
        logger.info(f'Last login information updated for user: {username}')
    except Exception as e:
        logger.error(f'Error occurred while updating last login information: {e}')
