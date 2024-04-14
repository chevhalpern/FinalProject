import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import re
from bs4 import BeautifulSoup
import requests
import sqlite3
import random

from sqlalchemy.sql import func

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Gedolim(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        gadol_name = db.Column(db.String(150))
        img_src = db.Column(db.String(255))
        link_src = db.Column(db.String(255))

        def __init__(self, gadol_name, img_src, link_src):
                self.gadol_name = gadol_name
                self.img_src = img_src
                self.link_src = link_src

        def __repr__(self):
                return f'<Student {self.id}-{self.gadol_name}-{self.img_src}-{self.link_src}>'

def getGedolimData():
        response = requests.get("https://en.wikipedia.org/wiki/Gedolim_pictures")
        soup = BeautifulSoup(response.content, 'html.parser')
        images = []
        links = []
        names = []
        all_info = []
        for x in soup.find_all('ul', {"class": "gallery mw-gallery-traditional center"}):
                for k in x.find_all('div', {"class": "gallerytext"}):
                        k = str(k)
                        link = re.findall("href=\".+?(?=\")", k)
                        name = re.findall("title=\".+?(?=\")", k)
                        link = "https://en.wikipedia.org" + ("".join(link)).replace("href=\"", "")
                        links.append(link)
                        name = "".join(name)
                        names.append(name.replace("title=\"", ""))
                x = str(x)
                image = re.findall("src=\".+?(?=\")", x)
                for i in image:
                        i = i.replace("src=\"", "")
                        images.append(i)
        all_info.append(names)
        all_info.append(images)
        all_info.append(links)
        return all_info

@app.post("/add")
def add():
        with app.app_context():  # initialize table with Gedolim
                db.create_all()
                data = getGedolimData()
                count = 0
                for row in range(0, 16):
                        db.session.add(Gedolim(f'{data[0][row]}', f'{data[1][row]}', f'{data[2][row]}'))
                db.session.commit()
                return redirect(url_for("home"))
# def random():
#         with app.app_context():
#                 gedolim = db.session.query(Gedolim).all()
#                 randomNumber = random.randint(0, len(gedolim) - 1)
#                 randomPhotoObject = gedolim[randomNumber]
#                 randomImage = re.findall("//upload.+?(?=-https)", str(randomPhotoObject))
#         return randomImage


@app.get("/")
def home():
        # gedolim_image = db.session.query(Gedolim).all()
        gedolim_image = "//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG"
        return render_template("base.html", gedolim=gedolim_image)

# def generate(){
#                 array = [//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Yitzchak_Zev_Soloveitchik.jpg/96px-Yitzchak_Zev_Soloveitchik.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/3/38/Shlomo_Ganzfried.jpg/86px-Shlomo_Ganzfried.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Chaim_Yosef_David_Azulai.jpg/88px-Chaim_Yosef_David_Azulai.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Meir_Shapiro.jpg/83px-Meir_Shapiro.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/6/62/Schneur_Zalman_of_Liadi.jpg/96px-Schneur_Zalman_of_Liadi.jpg,
#                 //upload.wikimedia.org/wikipedia/en/thumb/4/45/Steipler_Gaon.jpg/85px-Steipler_Gaon.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Yitzchak_Elchanan_Spektor.jpg/85px-Yitzchak_Elchanan_Spektor.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Shmuel_Salant.jpg/84px-Shmuel_Salant.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Avraham_Mattisyahu_of_Shtefanesht.JPG/91px-Avraham_Mattisyahu_of_Shtefanesht.JPG,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/1/19/Reb_Chaim_Ozer.jpg/92px-Reb_Chaim_Ozer.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Yisrael_Meir_Kagan.jpg/94px-Yisrael_Meir_Kagan.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Rabbi_Kalischer.jpg/108px-Rabbi_Kalischer.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Gershon_Edelshtein.jpg/77px-Gershon_Edelshtein.jpg,
#                 //upload.wikimedia.org/wikipedia/commons/thumb/3/30/Reb_Moshe_Feinstein.jpg/120px-Reb_Moshe_Feinstein.jpg
#                 ]
                
#         place = randomNum()
#         let image = document.getElementById('image')
#         image.setAttribute('src', array[place])
#         print(array[place])
#         }
#         function randomNum(){
#                 randomNumber = Math.floor(Math.random() * 17);
#                 return randomNumber;
#                 }

# @app.get("/generate/<int:src>")
# def generate(src):
#         # image = db.session.query(Gedolim).filter(Gedolim.img_src == src).first()
#         # new_image = random_gadol()
#         return redirect(url_for("home"))


# @app.route('/print_items')
# def print_items():
#     cursor = db.execute('SELECT img_src FROM Gedolim')
#     return render_template('print_items.html', items=cursor.fetchall())

# def random_gadol():
#         with app.app_context():
#                 obj = Gedolim.query.all()
#                 randomNumber = random.randint(0, len(obj) - 1)
#                 randomPhotoObject = obj[randomNumber]
#                 randomImage = re.findall("//upload.+?(?=-https)", str(randomPhotoObject))
#         return randomImage

# class RandomChoice():
#         with app.app_context():
#                 obj = Gedolim.query.all()
#                 randomNumber = random.randint(0, len(obj) - 1)
#                 randomPhotoObject = obj[randomNumber]
#                 print(randomPhotoObject)


#         randomImage = re.findall("//upload.+?(?=-https)", str(randomPhotoObject))
# return randomImage

