from flask import Flask, render_template
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# @app.route('/')
# @app.route('/index')
# def index():
#     param = {}
#     param['username'] = "Ученик Яндекс.Лицея"
#     param['title'] = "Домашняя страница"
#     return render_template('index.html', **param)


def main():
    db_session.global_init('/home/gruand69/Dev/ss_v1/db/ss.db')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
    
