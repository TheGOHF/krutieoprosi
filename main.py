from flask import Flask, render_template, redirect
from forms.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.users import User
import requests
import json

igorek = 'https://pyquiz.igorek.dev/'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'amogus_sus'
login_manager = LoginManager()
login_manager.init_app(app)


# username = 'TheGOHF'
# password = 'admin'


def main():
    db_session.global_init("db/data.sqlite")
    app.run(port=8000, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cabinet")
@login_required
def cabinet():
    # выступает как базовая при условии, что пользователь авторизирован
    # подключение дб с опросами
    return render_template("cabinet.html")


@app.route("/cabinet/create_table")
@login_required
def create_table():
    #
    return render_template("create_table.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        re = requests.post(f'{igorek}user/login', data=json.dumps({
            "username": form.username.data,
            "password": form.password.data
        }))
        if re.status_code == 200:
            login_user(user, remember=form.remember_me.data)
            user.x_token = re.content
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    current_user.x_token = None
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()

# эксперименты с апи
# data = json.dumps({
#     "username": username,
#     "password": password
# })
# r = requests.post(f'{igorek}user/login', data=data)
# headers = {
#     'x-token': r.text[1:-1]
# }
# re = requests.get(f'{igorek}user/me', headers=headers)
# print(re.text)
