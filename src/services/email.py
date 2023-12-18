from src.utils.responses import Response
from marshmallow import ValidationError
from flask_mail import Message

from src.schemas.email import EmailSchema


class EmailService:

    def send_email(self, request) -> Message:
        try:
            EmailSchema().load(request)

            msg = Message(
                request['subject'],
                sender='noreply@demo.com',
                recipients=[request['recipient_email']]
            )

            msg.body = request['body'].replace('%s', str(request['recipient_name']))
            return msg
        except ValidationError as e:
            print(e)
            return Response.error(e.__str__())
