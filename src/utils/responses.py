from datetime import datetime
from flask import make_response, jsonify


class Response:
    def ok(data, message="Successfully request!"):
        return make_response(
            jsonify(
                code=200,
                success=True,
                timestamp=datetime.now(),
                message=message,
                data=data,
            ),
            200,
        )



    def error(message="Internal Server Error"):
        return make_response(
            jsonify(
                code=500,
                success=False,
                timestamp=datetime.now(),
                message=message,
            ),
            500,
        )


    def badRequest(message="Bad Request"):
        return make_response(
            jsonify(
                code=400,
                success=False,
                timestamp=datetime.now(),
                message=message,
            ),
            400,
        )

