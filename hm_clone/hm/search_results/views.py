from flask import Blueprint, render_template, request

from hm.service import hm_service as service

search_results = Blueprint('search_results', __name__)


@search_results.route("/search/by/keyword")
def search_products_by_keyword():
    keyword = request.args.get("keyword")
    products = service.find_products_by_keyword(keyword)
    category_counts_dictionary = service.get_category_counts_dictionary(products)
    return render_template('search_results.html',
                           keyword=keyword,
                           products=products,
                           currentCategory="no_category",
                           categories=category_counts_dictionary)


@search_results.route("/search/by/category")
def find_products_by_category_and_keyword():
    keyword = request.args.get("keyword")
    category = request.args.get("category")
    products = service.find_products_by_category_and_keyword(category, keyword)
    category_counts_dictionary = service.get_category_counts_dictionary(service.find_products_by_keyword(keyword))
    return render_template('search_results.html',
                           keyword=keyword,
                           products=products,
                           currentCategory=category,
                           categories=category_counts_dictionary)


@search_results.route("/sort/price/ascending")
def sort_by_price_ascending():
    keyword = request.args.get("keyword")
    category = request.args.get("category")

    products = service.sort_ascending_by_price(keyword)

    if category != "no_category":
        products = service.sort_ascending_by_price(keyword, category)

    category_counts_dictionary = service.get_category_counts_dictionary(service.find_products_by_keyword(keyword))

    return render_template('search_results.html',
                           keyword=keyword,
                           products=products,
                           currentCategory=category,
                           categories=category_counts_dictionary)


@search_results.route("/sort/price/descending")
def sort_by_price_descending():
    keyword = request.args.get("keyword")
    category = request.args.get("category")

    products = service.sort_descending_by_price(keyword)

    if category != "no_category":
        products = service.sort_descending_by_price(keyword, category)

    category_counts_dictionary = service.get_category_counts_dictionary(service.find_products_by_keyword(keyword))

    return render_template('search_results.html',
                           keyword=keyword,
                           currentCategory=category,
                           products=products,
                           categories=category_counts_dictionary)


@search_results.route("/filter/by/size")
def filter_by_size():
    size = request.args.get("size")
    keyword = request.args.get("keyword")
    category = request.args.get("category")

    products = service.filter_by_size(size, keyword)

    if category != "no_category":
        products = service.filter_by_size(size, keyword, category)

    category_counts_dictionary = service.get_category_counts_dictionary(service.find_products_by_keyword(keyword))

    return render_template('search_results.html',
                           keyword=keyword,
                           products=products,
                           currentCategory=category,
                           categories=category_counts_dictionary)
