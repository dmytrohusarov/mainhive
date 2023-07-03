import logging
from app import cognito, response

# ------------------------------ Logger init ----------------------------------
logger = logging.getLogger(__name__)


def create_user(record: dict):
    return cognito.create_user({
        "email": record["email"]
    })


def process_record(record: dict):
    email = record["email"]
    try:
        cognito.get_user(record, email)
        logger.info("User already exists")

    except cognito.get_client().exceptions.UserNotFoundException:
        logger.info("Creating new user")
        logger.info(create_user(record))


def process_event(context: dict):
    process_record(context)
    return response.success()


# ---------------------------- Lambda Handler ---------------------------------
def lambda_handler(event, context):
    process_event(event)
