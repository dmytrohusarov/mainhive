import boto3
import os
import random
import string


def get_client():
    return boto3.client("cognito-idp")


# # ------------------------------ Helpers --------------------------------------
def dict_to_user_attrs(m: dict):
    return [{"Name": k, "Value": v} for k, v in m.items()]


def temp_password():
    rules = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "@$!*-"
    ]
    random.shuffle(rules)

    n = 2
    password = ""
    for i, rule in enumerate(rules):
        password += "".join(random.choice(rule) for _ in range(n))
    return password


def create_user(user: dict):
    return get_client().sign_up(
        ClientId=os.environ.get('CL_ID'),
        Username=user["email"],
        UserAttributes=dict_to_user_attrs({
            "email": user["email"],
        }), Password=temp_password())


def get_user(email: str):
    return get_client().admin_get_user(
        UserPoolId=os.environ.get('UP_ID'),
        Username=email
    )
