import os
from twilio.rest import Client
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        #print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('uploadcomplete.html')

    if request.method == "GET":
        return render_template("index.html")
    return

# adding twilio credentials
# load_dotenv()
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
#
# call = client.calls.create(
#     twiml='<Response><Say>This is a test call</Say></Response>',
#     to='+14047218853',
#     from_='+17089984068'
# )

# TODO: make my program message the voicemail that the caller left
# Follow the instructions in the Twilio CLI Quickstart to install the CLI and then log in to your Twilio account.
# Twilio CLI plugins provide additional capabilities for the CLI. The Assets Plugin allows you to manage static
# assets in a Twilio Assets service from your command line. Install the Assets Plugin with:
# twilio plugins:install @twilio-labs/plugin-assets
# create a new asset service with: twilio assets:init
# upload a file to use with your IVR: twilio assets:upload path/to/file --protected
# Copy the URL, return to the Studio Flow and enter it into the widget configuration. Save the widget and then publish
# the Flow. Give your number a call and you will hear your recording in the IVR instead of the text-to-speech.
# TODO: create a program that lets me upload my voicemails so that it can then run that twilio command?
