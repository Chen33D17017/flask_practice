import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flask_main import mail
from flask import current_app


def absolute_path(path):
    return os.path.join(current_app.root_path, 'static/profile_pics', path)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = absolute_path(picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def delete_old_pic(old_pic):
    absolute_path = lambda x : os.path.join(current_app.root_path, 'static/profile_pics', x)
    print(old_pic)
    if old_pic != 'default.jpg':
        os.remove(absolute_path(old_pic))


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='s894117@gmail.com',
            recipients=[user.email])
    msg.body=f''' To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no change will be made.
'''
    mail.send(msg)


