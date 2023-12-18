# Introduction

The Mail Service project is a Flask application that provides an email-sending service. It utilizes Flask-Mail for easy integration with email servers.

## Prerequisites

Before you begin, make sure you have Python and pip installed on your machine. You'll also need to the project's dependencies with requiriment.txt.

``` bash
# Install dependencies
pip install requiriment.txt
```

#### Configuration

Before running the project, you need to configure your email credentials in the .env file. Create a .env file at the root of the project with the following content:

``` bash
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_password
MAIL_USE_TLS=True
MAIL_USE_SSL=False
```

Replace the values with your email information.

#### Running the Service

With the dependencies installed and configurations completed, you can start the service with the following command:

``` bash
python app.py
```

The service will start at http://localhost:5000.

#### Endpoints

Send Email

- URL: /email/send
- Method: POST
- Request Body (JSON):

``` json
{
    "recipient_name": "Guilherme",
    "recipient_email": "guilhermebedan123@gmail.com",
    "subject": "Estágio",
    "body": "Olá, %s, estamos te contatando para falar sobre o estágio. Então quando possível nos contate sr. %s."
}
```
