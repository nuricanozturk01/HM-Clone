from flask import Blueprint, flash

from hm import db, Image
from hm.model.category import Category
from hm.model.color import Color
from hm.model.product import Product
from hm.model.size import Size

search_results = Blueprint('search_results', __name__)


def loadProduct(name, amount, price, category, sizes, colors, images):
    product = Product(name=name, amount=amount, price=price)
    product.categories.append(category)
    product.sizes.extend(sizes)
    product.colors.extend(colors)
    product.images.extend(images)
    return product


def loadData():
    # categories
    category_kadin = Category(name="Kadın")
    category_bebek = Category(name="Bebek")
    category_cocuk = Category(name="Çocuk")
    category_divide = Category(name="Divide")
    category_erkek = Category(name="Erkek")
    category_home = Category(name="Home")
    category_spor = Category(name="Spor")

    # size
    size_sm = Size(name="S")
    size_m = Size(name="M")
    size_l = Size(name="L")
    size_xl = Size(name="XL")
    size_xxl = Size(name="XXL")

    # color
    color_bej = Color(name="Bej")
    color_beyaz = Color(name="Beyaz")
    color_turuncu = Color(name="Turuncu")
    color_yesil = Color(name="Yeşil")
    color_siyah = Color(name="Siyah")
    color_lacivert = Color(name="Lacivert")
    color_mavi = Color(name="Mavi")
    color_haki = Color(name="Haki")

    default_sizes = [size_sm, size_m, size_l, size_xl, size_xxl]

    image1 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kargo_sort_bej_1.jpeg")
    image2 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kargo_sort_bej_2.jpeg")

    image3 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/pamuklu_tulum_bej_1.jpeg")
    image4 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/pamuklu_tulum_bej_2.jpeg")

    image5 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_1_beyaz.jpeg")
    image6 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_2_beyaz.jpeg")

    prod1 = loadProduct(name="Şort", amount=10, price=300, category=category_bebek, sizes=default_sizes,
                        colors=[color_bej], images=[image1, image2])

    prod2 = loadProduct(name="Tulum", amount=3, price=400, category=category_bebek, sizes=default_sizes,
                        colors=[color_bej], images=[image3, image4])

    prod3 = loadProduct(name="Tişört", amount=20, price=700, category=category_bebek, sizes=default_sizes,
                        colors=[color_beyaz, color_yesil], images=[image5, image6])

    db.session.add_all([category_kadin, category_bebek, category_cocuk, category_divide, category_erkek, category_home,
                        category_spor, size_sm, size_m, size_l, size_xl, size_xxl])

    db.session.add_all([color_bej, color_beyaz, color_turuncu,
                        color_yesil, color_siyah, color_lacivert, color_mavi, color_haki, prod1, prod2, prod3,
                        image1, image2, image3, image4, image5, image6])

    db.session.commit()


@search_results.route("/load")
def load():
    loadData()
    flash('Thanks for registering! Now you can login!')
    return "<h1> SUCCESS </h1>"
