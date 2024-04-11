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

@app.get("/")
def home():
        gedolim = db.session.query(Gedolim).all()
        return render_template("base.html", gedolim=gedolim)

# @app.route('/image-render/')
# def random_gadol():
#         with app.app_context():
#                 obj = Gedolim.query.all()
#                 randomNumber = random.randint(0, len(obj) - 1)
#                 randomPhotoObject = obj[randomNumber]
#                 randomImage = re.findall("//upload.+?(?=-https)", str(randomPhotoObject))
#         return redirect(url_for("home"))

