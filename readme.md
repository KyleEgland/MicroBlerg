# MicroBlerg

Just another blog web-app created by following a tutorial.

## Windows notes

Manually setting environment variables in PowerShell:

`$env:FLASK_APP = '.\microblerg.py'`
`$env:FLASK_DEBUG = 1`

List all environment variables
`dir env:`

## Running SMTP debugging server

Run this command in a separate terminal window:

`(venv) PS C:\workspace\microblerg> python -m smtpd -n -c DebuggingServer localhost:8025`

Set the following environment variables
`$env:FLASK_DEBUG = 0`
`$env:MAIL_SERVER = "localhost"`
`$env:MAIL_PORT = 8025`
