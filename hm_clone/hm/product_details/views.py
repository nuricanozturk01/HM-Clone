from flask import Blueprint, render_template, request
from hm.service import hm_service as service

product_details = Blueprint('product_details', __name__)


def get_image_dict(product):
    image_dict = {}
    image_count = len(product.images) if product else 0

    if image_count == 2:
        image_dict[product.colors[0].name] = [product.images[0].name, product.images[1].name]

    if image_count == 4:
        image_dict[product.colors[0].name] = [product.images[0].name, product.images[1].name]
        image_dict[product.colors[1].name] = [product.images[2].name, product.images[3].name]

    return image_dict


@product_details.route("/find/product-detail")
def find_product_details_by_id():
    product = service.find_product_by_id(request.args.get("id"))
    image_dictionary = get_image_dict(product)
    return render_template("product_details.html", product=product, image_dict=image_dictionary)
