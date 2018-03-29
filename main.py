import os
from flask import Flask, render_template, request, flash
from flask import send_from_directory, current_app
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask_mail import Mail
from flask.ext.mail import Message
from threading import Thread

UPLOAD_FOLDER = './app/Downloads/'
ALLOWED_EXTENSIONS = set(['odt', 'txt', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
app.config['STORAGE_MAIL_SUBJECT_PREFIX'] = '[Storage]'
app.config['STORAGE_MAIL_SENDER'] = 'Storage Admin <putkovdimi@gmail.com>'

mail = Mail(app)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['STORAGE_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['STORAGE_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def getFiles():
    return os.listdir(UPLOAD_FOLDER)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/", methods=["GET", "POST"])
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




@app.route("/upload/<filename>", methods=["GET"])
def download(filename):
    upload_path = os.path.join(current_app.root_path + UPLOAD_FOLDER[1::])
    print(upload_path)
    return send_from_directory(upload_path, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)