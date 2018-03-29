import os
from datetime import datetime
from flask import request, render_template, session, redirect, url_for, flash, send_from_directory, current_app
from . import main
from .. import get_DB_object
from ..email import send_email

UPLOAD_FOLDER = '../Downloads/'
ALLOWED_EXTENSIONS = set(['odt', 'txt', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def getFiles():
    return os.listdir(UPLOAD_FOLDER)


@main.route("/", methods=["GET", "POST"])
def index():
    args = {"method": "GET"}
    file_list = getFiles()
    if request.method == "POST":
        file = request.files["file"]
        if not file.filename:
            flash('Looks like you have not chosen any file')
            args["res"] = "No selected files"
        if file and allowed_file(file.filename):
            if file.filename in file_list:
                flash("It already exists brother")
            else:
                flash('Your file was saved successfully')
                send_email("putkovdimi@gmail.com", 'New File',
                           'mail/new_file', filename=file.filename)
                file.save(UPLOAD_FOLDER + file.filename)
        args["method"] = "POST"
    file_list = getFiles()
    return render_template("index.html",
                           args=args, file_list=file_list, current_time=datetime.utcnow())


@main.route("/upload/<filename>", methods=["GET"])
def download(filename):
    upload_path = os.path.join(current_app.root_path + UPLOAD_FOLDER[1::])
    print(upload_path)
    return send_from_directory(upload_path, filename=filename)
