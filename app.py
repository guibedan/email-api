from flask import Flask, request

from src.config.email import config_email
from src.services.email import EmailService

from src.utils.responses import Response

app = Flask(__name__)
mail = config_email(app)


@app.route('/email/send', methods=['POST'])
def email():
    data = EmailService().send_email(request.get_json())
    try:
        mail.send(data)
        return Response.ok('Email successfully sent.')
    except Exception as e:
        return Response.badRequest(e.__str__())


@app.route('/email/list/send', methods=['POST'])
def list_email():
    data = EmailService().send_list_email(request.get_json())
    try:
        for i in data:
            mail.send(i)
        return Response.ok('Email successfully sent.')
    except Exception as e:
        return Response.badRequest(e.__str__())


if __name__ == '__main__':
    app.run()
