from app import Gedolim, getGedolimData, Gadol
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


def test_initial_values():
    gadol = Gadol()
    assert gadol.gadol_id == 0
    assert gadol.gadol_name == "rabbi"
    assert gadol.source_name == "src"
    assert gadol.choices_array == ["rabbi", "rabbi1", "rabbi2"]
    assert gadol.gadol_link == "https://www.rabbi.com"

def test_string():
    gadol = Gedolim(id=1, gadol_name="Vilna Gaon", img_src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG", link_src="https://en.wikipedia.org/wiki/Vilna_Gaon")
    gadol = str(gadol)
    assert gadol == "<Student 1-Vilna Gaon-//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG-https://en.wikipedia.org/wiki/Vilna_Gaon>"

def test_data_retrieved():
    data = [['Vilna Gaon', 'Velvel Soloveitchik', 'Sdei Chemed', 'Shlomo Ganzfried', 'Chaim Yosef David Azulai', 'Meir Shapiro', 'Baal HaTanya', 'Steipler', 'Yitzchak Elchanan Spektor', 'Shmuel Salant', 'Avraham Mattisyahu Friedman', 'Chaim Ozer Grodzenski', 'Rabbi Yisrael Meir Kagan', 'Tzvi Hirsch Kalischer', 'Gershon Edelstein', 'Moshe Feinstein'], ['//upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Vilna_Gaon_authentic_portrait.JPG/87px-Vilna_Gaon_authentic_portrait.JPG', '//upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Yitzchak_Zev_Soloveitchik.jpg/96px-Yitzchak_Zev_Soloveitchik.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Medini_1.jpg/91px-Medini_1.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Shlomo_Ganzfried.jpg/86px-Shlomo_Ganzfried.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Chaim_Yosef_David_Azulai.jpg/88px-Chaim_Yosef_David_Azulai.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Meir_Shapiro.jpg/83px-Meir_Shapiro.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/6/62/Schneur_Zalman_of_Liadi.jpg/96px-Schneur_Zalman_of_Liadi.jpg', '//upload.wikimedia.org/wikipedia/en/thumb/4/45/Steipler_Gaon.jpg/85px-Steipler_Gaon.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Yitzchak_Elchanan_Spektor.jpg/85px-Yitzchak_Elchanan_Spektor.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Shmuel_Salant.jpg/84px-Shmuel_Salant.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Avraham_Mattisyahu_of_Shtefanesht.JPG/91px-Avraham_Mattisyahu_of_Shtefanesht.JPG', '//upload.wikimedia.org/wikipedia/commons/thumb/1/19/Reb_Chaim_Ozer.jpg/92px-Reb_Chaim_Ozer.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Yisrael_Meir_Kagan.jpg/94px-Yisrael_Meir_Kagan.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Rabbi_Kalischer.jpg/108px-Rabbi_Kalischer.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Gershon_Edelshtein.jpg/77px-Gershon_Edelshtein.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/3/30/Reb_Moshe_Feinstein.jpg/120px-Reb_Moshe_Feinstein.jpg'], ['https://en.wikipedia.org/wiki/Vilna_Gaon', 'https://en.wikipedia.org/wiki/Velvel_Soloveitchik', 'https://en.wikipedia.org/wiki/Sdei_Chemed', 'https://en.wikipedia.org/wiki/Shlomo_Ganzfried', 'https://en.wikipedia.org/wiki/Chaim_Yosef_David_Azulai', 'https://en.wikipedia.org/wiki/Meir_Shapiro', 'https://en.wikipedia.org/wiki/Baal_HaTanya', 'https://en.wikipedia.org/wiki/Steipler', 'https://en.wikipedia.org/wiki/Yitzchak_Elchanan_Spektor', 'https://en.wikipedia.org/wiki/Shmuel_Salant', 'https://en.wikipedia.org/wiki/Avraham_Mattisyahu_Friedman', 'https://en.wikipedia.org/wiki/Chaim_Ozer_Grodzenski', 'https://en.wikipedia.org/wiki/Rabbi_Yisrael_Meir_Kagan', 'https://en.wikipedia.org/wiki/Tzvi_Hirsch_Kalischer', 'https://en.wikipedia.org/wiki/Gershon_Edelstein', 'https://en.wikipedia.org/wiki/Moshe_Feinstein']]
    test_data = getGedolimData()
    assert data == test_data