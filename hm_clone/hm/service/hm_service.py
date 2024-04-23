from collections import defaultdict
from sqlalchemy.orm import joinedload

from hm.model.product import Product
from hm.model.category import Category
from hm.model.size import Size
from hm.model.color import Color


def find_products_by_keyword(keyword):
    keyword = f'%{keyword}%'
    products = Product.query.filter(Product.name.like(keyword)).all()
    return products


def find_product_by_id(product_id):
    return Product.query.filter(Product.id == product_id).first()


def filter_by_size(size, keyword, category=None):
    keyword = f'%{keyword}%'

    query = (Product.query.join(Product.sizes).filter(Product.name.like(keyword)).filter(Size.name == size))

    if category:
        query = query.join(Product.categories).filter(Category.name == category).options(joinedload(Product.categories))

    return query.all()


def filter_by_color(color):
    return Product.query.join(Product.colors).filter(Color.name == color).options(joinedload(Product.colors)).all()


def filter_by_category(category):
    return (Product.query.join(Product.categories)
            .filter(Category.name == category)
            .options(joinedload(Product.categories)).all())


def sort_ascending_by_price(keyword, category=None):
    keyword = f'%{keyword}%'
    query = (Product.query
             .join(Product.categories)
             .filter(Product.name.like(keyword)))
    if category:
        query = query.filter(Category.name == category)

    products = query.options(joinedload(Product.categories)).all()
    return sorted(products, key=lambda x: x.price)


def sort_descending_by_price(keyword, category=None):
    keyword = f'%{keyword}%'
    query = (Product.query
             .join(Product.categories)
             .filter(Product.name.like(keyword)))
    if category:
        query = query.filter(Category.name == category)

    products = query.options(joinedload(Product.categories)).all()
    return sorted(products, key=lambda x: x.price, reverse=True)


def find_products_by_category_and_keyword(category, keyword):
    keyword = f'%{keyword}%'
    products = (Product.query
                .join(Product.categories)
                .filter(Category.name == category)
                .filter(Product.name.like(keyword))
                .options(joinedload(Product.categories))
                .all())
    return products


def get_category_counts_dictionary(products):
    category_counts = defaultdict(int)

    for product in products:
        for category in product.categories:
            category_counts[category.name] += 1

    return [(category, count) for category, count in category_counts.items()]
