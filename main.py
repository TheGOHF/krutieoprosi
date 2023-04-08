from flask import Flask, render_template
import requests
import json

igorek = 'https://pyquiz.igorek.dev/'
app = Flask(__name__)


# username = 'TheGOHF'
# password = 'admin'


def main():
    app.run(port=8000, host='127.0.0.1')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    # выступает как базовая
    # подключение формы
    return render_template("login.html")


@app.route("/cabinet")
def cabinet():
    # выступает как базовая при условии, что пользователь авторизирован
    # подключение дб с опросами
    return render_template("cabinet.html")


@app.route("/cabinet/create_table")
def create_table():
    #
    return render_template("create_table.html")


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
