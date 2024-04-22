from flask import Flask, render_template, redirect, request
from data import db_session

from data.users import User
from data.attractions import Attractions
from forms.user import RegisterForm, LoginForm
from forms.attractions import AttractionsForm

from flask_login import (LoginManager,
                         login_user,
                         logout_user,
                         login_required,
                         current_user)


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               message="Wrong login or password",
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/')
def index():
    db_sess = db_session.create_session()
    attractions = db_sess.query(Attractions).all()
    return render_template('index.html', attractions=attractions)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают!")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            sex=form.sex.data,
            age=form.age.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация',
                           form=form)


@app.route('/attractions', methods=['GET', 'POST'])
@login_required
def add_attractions():
    form = AttractionsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        attractions = Attractions()
        attractions.name = form.name.data
        attractions.description = form.description.data
        attractions.сity = form.city.data
        attractions.country = form.country.data
        f = request.files['file']
        data = f.read()
        with open(f'static/img/{attractions.name}.jpg', 'wb+') as file:
            file.write(data)
        attractions.pic = f'static/img/{attractions.name}.jpg'
        attractions.map = f'https://yandex.ru/maps/?mode=search&text={attractions.name}'
        current_user.attractions.append(attractions)

        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('attractions.html', title='Добавление новости',
                           form=form)


def main():
    db_session.global_init('/home/gruand69/Dev/ss_v1/db/ss.db')
    app.run(port=8080, host='127.0.0.1')

    # user = User()
    # user.name = "grugrig"
    # user.sex = "male"
    # user.age = 17
    # user.about = "younger son"
    # user.email = "grugrig@email.ru"

    # user1 = User()
    # user1.name = "gruil"
    # user1.sex = "male"
    # user1.age = 31
    # user1.about = "eldest son"
    # user1.email = "gruil@email.ru"

    # user2 = User()
    # user2.name = "gruann"
    # user2.sex = "female"
    # user2.age = 52
    # user2.about = "mother"
    # user2.email = "gruann@email.ru"

    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.add(user1)
    # db_sess.add(user2)
    # db_sess.commit()

    # attraction = Attractions()
    # attraction.name = "moscow_city"
    # attraction.description = "group of skyscraper in Moscow"
    # attraction.сity = "Moscow"
    # attraction.country = "Russia"
    # attraction.map = "https://yandex.ru/maps/?mode=search&text=Москва+сити"
    # attraction.pic = "static/img/moskva_city.jpg"
    # attraction.user_id = 1

    # attraction1 = Attractions()
    # attraction1.name = "vb_template"
    # attraction1.description = "church located on Red Square in Moscow"
    # attraction1.сity = "Moscow"
    # attraction1.country = "Russia"
    # attraction1.map = "https://yandex.ru/maps/?mode=search&text=Москва+Покровский+собор"
    # attraction1.pic = "static/img/vb_template.jpg"
    # attraction1.user_id = 2

    # attraction2 = Attractions()
    # attraction2.name = "luvr"
    # attraction2.description = "museum located in center of Paris"
    # attraction2.сity = "Paris"
    # attraction2.country = "France"
    # attraction2.map = "https://yandex.ru/maps/?mode=search&text=Париж+Лувр"
    # attraction2.pic = "static/img/luvr.jpeg"
    # attraction2.user_id = 3

    # attraction3 = Attractions()
    # attraction3.name = "efil_tower"
    # attraction3.description = "famous tower located in Paris"
    # attraction3.сity = "Paris"
    # attraction3.country = "France"
    # attraction3.map = "https://yandex.ru/maps/?mode=search&text=Париж+Эйфелева+башня"
    # attraction3.pic = "static/img/efil_tower.jpg"
    # attraction3.user_id = 3

    # db_sess = db_session.create_session()
    # db_sess.add(attraction)
    # db_sess.add(attraction1)
    # db_sess.add(attraction2)
    # db_sess.add(attraction3)
    # db_sess.commit()


if __name__ == '__main__':
    main()
    
