from flask import Blueprint, render_template
from hm.service import hm_service as service

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template("mainpage.html", title="H&M", products=service.filter_by_category("Kadın"))


@core.route('/find_products_by_category/<category>')
def find_products_by_category(category):
    return render_template('mainpage.html', products=service.filter_by_category(category))
