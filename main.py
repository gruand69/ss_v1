from flask import Flask, render_template
from data import db_session

from data.users import User
from data.attractions import Attractions


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index')
def index():
    db_sess = db_session.create_session()
    attractions = db_sess.query(Attractions).all()
    return render_template('index.html', attractions=attractions)


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
    
