import logging

# ------------------------------ Logger init ----------------------------------
logger = logging.getLogger(__name__)


class Response(Exception):
    def __init__(self, code, body):
        super().__init__()
        self.code = code
        self.body = body

    def response(self):
        return {
            "isBase64Encoded": False,
            "statusCode": self.code,
            "body": self.body,
            "headers": {
                "Content-Type": "application/json"
            }
        }


def success(body=None):
    if not body:
        body = {"message": "Successfully processed request"}
    return Response(200, body)
