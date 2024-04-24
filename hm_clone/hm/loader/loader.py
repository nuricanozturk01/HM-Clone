from flask import Blueprint, request

from hm.extensions import db
from hm.model.category import Category
from hm.model.color import Color
from hm.model.product import Product
from hm.model.size import Size
from hm.model.image import Image

loader = Blueprint('loader', __name__)


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
    category_cocuk = Category(name="Cocuk")
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
    color_yesil = Color(name="Yesil")
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
    image7 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_1_yesil.jpeg")
    image8 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_2_yesil.jpeg")
    image9 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_turuncu_1.jpeg")
    image10 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_turuncu_2.jpeg")
    image11 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_beyaz_1.jpeg")
    image12 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tisort_beyaz_2.jpeg")
    image13 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/can_elbise_beyaz_1.jpeg")
    image14 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/can_elbise_beyaz_2.jpeg")
    image15 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/can_elbise_siyah_1.jpeg")
    image16 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/can_elbise_siyah_2.jpeg")
    image17 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_sort_siyah_1.jpeg")
    image18 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_sort_siyah_2.jpeg")
    image19 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kolsuz_ust_bej_1.jpeg")
    image20 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kolsuz_ust_bej_2.jpeg")
    image21 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tek_omuzlu_ust_siyah_1.jpeg")
    image22 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tek_omuzlu_ust_siyah_2.jpeg")
    image23 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/yaka_gomlek_1_beyaz.jpeg")
    image24 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/yaka_gomlek_2_beyaz.jpeg")
    image25 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/yaka_gomlek_1_lacivert.jpeg")
    image26 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/yaka_gomlek_2_lacivert.jpeg")
    image27 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/polo_tisort_beyaz_1.jpeg")
    image28 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/polo_tisort_beyaz_2.jpeg")
    image29 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/banyo_havlusu_yesil_1.jpeg")
    image30 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/banyo_havlusu_yesil_2.jpeg")
    image31 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tepsi_bej_1.jpeg")
    image32 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/tepsi_bej_2.jpeg")
    image33 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/diz_boyu_etek_siyah-1.jpeg")
    image34 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/diz_boyu_etek_siyah-2.jpeg")
    image35 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/diz_boyu_etek_cicek-1.jpeg")
    image36 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/diz_boyu_etek_cicek-2.jpeg")
    image37 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/firfirli_ust_beyaz_1.jpeg")
    image38 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/firfirli_ust_beyaz_2.jpeg")

    image39 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kabarik_kollu_ust_yesil-1.jpeg")
    image40 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kabarik_kollu_ust_yesil_2.jpeg")
    image41 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kabarik_kollu_ust_siyah_1.jpeg")
    image42 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/kabarik_kollu_ust_siyah_2.jpeg")

    image43 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_gomlek_beyaz-1.jpeg")

    image44 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_gomlek_beyaz-2.jpeg")

    image45 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_karisimli_bluz_1_mavi.jpeg")

    image46 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_karisimli_bluz_2_mavi.jpeg")

    image47 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_karisimli_bluz_1_beyaz.jpeg")

    image48 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/keten_karisimli_bluz_2_beyaz.jpeg")

    image49 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_tayt_mavi_1.jpeg")

    image50 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_tayt_mavi_2.jpeg")

    image51 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_tayt_siyah_1.jpeg")

    image52 = Image(
        name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_tayt_siyah_2.jpeg")

    image53 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_ustu_haki_1.jpeg")

    image54 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_ustu_haki_2.jpeg")

    image55 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_ustu_siyah_1.jpeg")

    image56 = Image(name="https://callofproject-images.s3.eu-central-1.amazonaws.com/hm/spor_ustu_siyah_2.jpeg")

    prod1 = loadProduct(name="Sort", amount=10, price=1300, category=category_bebek, sizes=default_sizes,
                        colors=[color_bej], images=[image1, image2])

    prod2 = loadProduct(name="Tulum", amount=3, price=400, category=category_bebek, sizes=default_sizes,
                        colors=[color_bej], images=[image3, image4])

    prod3 = loadProduct(name="Tisört", amount=20, price=1700, category=category_bebek, sizes=default_sizes,
                        colors=[color_beyaz, color_yesil], images=[image5, image6, image7, image8])

    prod4 = loadProduct(name="Tisört", amount=5, price=654, category=category_cocuk, sizes=default_sizes,
                        colors=[color_turuncu], images=[image9, image10])

    prod5 = loadProduct(name="Tisört", amount=54, price=523, category=category_cocuk, sizes=[size_m, size_l],
                        colors=[color_beyaz], images=[image11, image12])

    prod6 = loadProduct(name="Can Elbise", amount=12, price=8653, category=category_divide,
                        sizes=[size_m, size_l, size_sm], colors=[color_beyaz, color_siyah],
                        images=[image13, image14, image15, image16])

    prod7 = loadProduct(name="Sort", amount=15, price=843, category=category_divide,
                        sizes=default_sizes, colors=[color_siyah], images=[image17, image18])

    prod8 = loadProduct(name="Atlet", amount=15, price=1234, category=category_divide,
                        sizes=default_sizes, colors=[color_bej], images=[image19, image20])

    prod9 = loadProduct(name="Tek Omuzlu", amount=15, price=486, category=category_divide,
                        sizes=default_sizes, colors=[color_siyah], images=[image21, image22])

    prod10 = loadProduct(name="Gomlek", amount=15, price=346, category=category_erkek,
                         sizes=default_sizes, colors=[color_beyaz, color_mavi],
                         images=[image23, image24, image25, image26])

    prod11 = loadProduct(name="Polo Tisort", amount=15, price=999, category=category_erkek,
                         sizes=[size_m, size_sm, size_xl], colors=[color_beyaz],
                         images=[image27, image28])
    prod12 = loadProduct(name="Havlu", amount=15, price=1999, category=category_home,
                         sizes=default_sizes, colors=[color_yesil],
                         images=[image29, image30])

    prod13 = loadProduct(name="Tepsi", amount=15, price=283, category=category_home,
                         sizes=default_sizes, colors=[color_bej],
                         images=[image31, image32])

    prod14 = loadProduct(name="Etek", amount=150, price=642, category=category_kadin,
                         sizes=default_sizes, colors=[color_siyah, color_beyaz],
                         images=[image33, image34, image35, image36])

    prod15 = loadProduct(name="Fırfırlı üst", amount=12, price=1923, category=category_kadin,
                         sizes=default_sizes, colors=[color_beyaz],
                         images=[image37, image38])

    prod16 = loadProduct(name="Kabarık kollu üst", amount=10, price=1881, category=category_kadin,
                         sizes=default_sizes, colors=[color_yesil, color_siyah],
                         images=[image39, image40, image41, image42])

    prod17 = loadProduct(name="Gomlek", amount=150, price=1000, category=category_kadin,
                         sizes=default_sizes, colors=[color_beyaz],
                         images=[image43, image44])

    prod18 = loadProduct(name="Bluz", amount=150, price=642, category=category_kadin,
                         sizes=default_sizes, colors=[color_beyaz, color_mavi],
                         images=[image45, image46, image47, image48])

    prod19 = loadProduct(name="Tayt", amount=150, price=942, category=category_spor,
                         sizes=default_sizes, colors=[color_siyah, color_mavi],
                         images=[image49, image50, image51, image52])

    prod20 = loadProduct(name="üst", amount=150, price=250, category=category_spor,
                         sizes=default_sizes, colors=[color_siyah, color_haki],
                         images=[image53, image54, image55, image56])

    product_list = [
        prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10,
        prod11, prod12, prod13, prod14, prod15, prod16, prod17, prod18, prod19, prod20
    ]

    image_list = [
        image1, image2, image3, image4, image5, image6, image7, image8, image9, image10,
        image11, image12, image13, image14, image15, image16, image17, image18, image19, image20,
        image21, image22, image23, image24, image25, image26, image27, image28, image29, image30,
        image31, image32, image33, image34, image35, image36, image37, image38, image39, image40,
        image41, image42, image43, image44, image45, image46, image47, image48, image49, image50,
        image51, image52, image53, image54, image55, image56
    ]

    db.session.add_all([category_kadin, category_bebek, category_cocuk, category_divide, category_erkek, category_home,
                        category_spor, size_sm, size_m, size_l, size_xl, size_xxl,
                        color_bej, color_beyaz, color_turuncu, color_yesil, color_siyah, color_lacivert, color_mavi,
                        color_haki])

    db.session.add_all(product_list)
    db.session.add_all(image_list)
    db.session.commit()


@loader.route("/load")
def load():
    key = request.args.get("key")
    if key != "19nuricanozturk99":
        return "<h1> INVALID KEY </h1>"

    if not Category.query.all():
        loadData()
        return "<h1> SUCCESS </h1>"

    return "<h1> ALREADY LOADED </h1>"
