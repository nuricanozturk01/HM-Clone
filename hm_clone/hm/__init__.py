import os

from flask import Flask
from flask_migrate import Migrate

from hm.core.views import core
from hm.extensions import db
from hm.model.category import Category
from hm.model.color import Color
from hm.model.product import Product
from hm.model.size import Size
from hm.model.image import Image
from hm.product_details.views import product_details
from hm.search_results.views import search_results


def generate_secret_key(length=24):
    return os.urandom(length).hex()


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = generate_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:12345678@localhost/hm_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate(app, db)

db.init_app(app)

app.register_blueprint(core)
app.register_blueprint(search_results)
app.register_blueprint(product_details)
