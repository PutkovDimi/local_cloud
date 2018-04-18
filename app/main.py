import os
from flask import Flask, render_template, request
from flask import send_from_directory, current_app
from datetime import datetime
from flask_mail import Message
from threading import Thread
from flask_login import login_user, logout_user, login_required
from flask import redirect, flash, url_for
from app.auth.forms import LoginForm
from app.models import User
from app import create_app
from app import get_DB_object
from app import auth
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask import Blueprint

UPLOAD_FOLDER = '/Downloads/'
ALLOWED_EXTENSIONS = set(['odt', 'txt', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app, auth = create_app(os.getenv('FLASK_CONFIG') or 'default')
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# auth = Blueprint('auth', __name__)

mail = Mail(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        user_id = get_DB_object.find_user(email=form.email.data)["_id"]
        if user_id:
            user = User(user_id=user_id)
            if user:
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') or url_for('index'))
        flash("Invalid email or password")
    # checks if the user is authernticated
    # or not, if yes it skips authentfic.
    # does not allow user to use get method
    if request.method == 'GET':
        return render_template('auth/login.html',
                               form=form,
                               title='Login')
    return render_template('auth/login.html', form=form)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))


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


def get_files():
    return os.listdir(os.path.dirname(os.path.abspath(__file__)) + UPLOAD_FOLDER)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/", methods=["GET", "POST"])
def index():
    args = {"method": "GET"}
    file_list = get_files()
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
    file_list = get_files()
    return render_template("index.html",
                           args=args, file_list=file_list, current_time=datetime.utcnow())


@app.route("/upload/<filename>", methods=["GET"])
def download(filename):
    upload_path = os.path.join(current_app.root_path + UPLOAD_FOLDER[1::])
    print(upload_path)
    return send_from_directory(upload_path, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
