from flask import Blueprint, render_template

product_details = Blueprint('product_details', __name__)


# @product_details.route("/deneme/<biginteger:product_id>")
def find_product_details_by_id():
    return render_template("mainpage.html")
