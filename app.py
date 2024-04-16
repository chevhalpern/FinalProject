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

# INITIALIZE DATABASE PROPERTIES
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

# USING WEB SCRAPPING TO GET DATA
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

# ADD GATHERED DATA TO DATABASE
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

# INITIALIZE HTML AND SEND PARAMETER
@app.get("/")
def home():
        gadol = Gadol()
        return render_template("base.html", gedolim=gadol)

# @app.get("/refresh/<int:gadol_id>")
# def refresh(gadol_id):
#         gadol = db.session.query(Gedolim).filter(Gedolim.id == gadol_id).first()
#         new_gadol = Gadol()
#         if new_gadol.id != gadol.id:
#                 return redirect(url_for("home"))


# CREATE CLASS AND INITIALIZE PROPERTIES
class Gadol:
        def randomChoice1(target):
                with app.app_context():
                        gedolim = db.session.query(Gedolim).all()
                        while True:
                                randomNumber = random.randint(0, len(gedolim) - 1)
                                if randomNumber != target:
                                        return randomNumber                            

        def randomChoice2(gadol, choice1):
                with app.app_context():
                        gedolim = db.session.query(Gedolim).all()
                        while True:
                                randomNumber = random.randint(0, len(gedolim) - 1)
                                if randomNumber != gadol:
                                        if randomNumber != choice1:
                                                return randomNumber
                                        
        
        def randomizeChoices(correct, option1, option2):
                choices = ["placeholder1", "placeholder2", "placeholder3"]
                place1 = random.randint(0, 2)
                while True:
                        place2 = random.randint(0, 2)
                        if place2 != place1:
                                break
                while True:
                        place3 = random.randint(0, 2)
                        if place3 != place1:
                                if place3 != place2:
                                        break
                choices[place1] = correct
                choices[place2] = option1
                choices[place3] = option2
                return choices
                                        
        with app.app_context():
                gedolim = db.session.query(Gedolim).all()
                randomNumber = random.randint(0, len(gedolim) - 1)
                randomPhotoObject = gedolim[randomNumber]
                link = re.findall("http.+?(?=>)", str(randomPhotoObject))
                link = "".join(link)
                source = re.findall("//upload.+?(?=-https)", str(randomPhotoObject))
                source = "".join(source)
                name = re.findall("Student.+?(?=-//)", str(randomPhotoObject))
                id = randomNumber + 1
                name = ("".join(name)).replace(f"Student {randomNumber + 1}-", "")
                randomNum1 = randomChoice1(randomNumber)
                optObject1 = gedolim[randomNum1]
                choice1 = re.findall("Student.+?(?=-//)", str(optObject1))
                choice1 = ("".join(choice1)).replace(f"Student {randomNum1 + 1}-", "")
                randomNum2 = randomChoice2(randomNumber, randomNum1)
                optObject2 = gedolim[randomNum2]
                choice2 = re.findall("Student.+?(?=-//)", str(optObject2))
                choice2 = ("".join(choice2)).replace(f"Student {randomNum2 + 1}-", "")
                choices = randomizeChoices(name, choice1, choice2)

        def __init__(self, gadol_id=id, source_name=source, gadol_name=name, choices_array=choices, gadol_link=link):
                self._gadol_id = gadol_id
                self._source_name = source_name
                self._gadol_name = gadol_name
                self._choices_array = choices_array
                self._gadol_link = gadol_link

        @property
        def gadol_id(self):
                return self._gadol_id
        
        @property
        def source_name(self):
                return self._source_name

        @property
        def gadol_name(self):
                return self._gadol_name
        
        @property
        def choices_array(self):
                return self._choices_array

        @property
        def gadol_link(self):
                return self._gadol_link