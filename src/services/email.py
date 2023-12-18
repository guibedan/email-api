from typing import List

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

    def send_list_email(self, request) -> List[Message]:
        list_mail = []
        for i in range(len(request['recipient_email'])):
            try:

                data_temp = {
                    'subject': request['subject'],
                    'recipient_email': request['recipient_email'][i],
                    'recipient_name': request['recipient_name'][i],
                    'body': request['body']
                }

                EmailSchema().load(data_temp)

                msg = Message(
                    data_temp['subject'],
                    sender='noreply@demo.com',
                    recipients=[data_temp['recipient_email']]
                )

                msg.body = request['body'].replace('%s', str(data_temp['recipient_name']))
                list_mail.append(msg)
            except ValidationError as e:
                print(e)
                return Response.error(e.__str__())
        return list_mail
