import json

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from hm.extensions import db

product_category = Table('product_category', db.metadata,
                         Column('product_id', Integer, ForeignKey('product.id')),
                         Column('category_id', Integer, ForeignKey('category.id')))

product_size = Table('product_size', db.metadata,
                     Column('product_id', Integer, ForeignKey('product.id')),
                     Column('size_id', Integer, ForeignKey('size.id')))

product_color = Table("product_color", db.metadata,
                      Column("product_id", Integer, ForeignKey('product.id')),
                      Column("color_id", Integer, ForeignKey('color.id')))

product_image = Table("product_image", db.metadata,
                      Column("product_id", Integer, ForeignKey('product.id')),
                      Column("image_id", Integer, ForeignKey('image.id')))


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)
    categories = relationship("Category", secondary=product_category, backref="products")
    sizes = relationship("Size", secondary=product_size, backref="products")
    colors = relationship("Color", secondary=product_color, backref="products")
    images = relationship("Image", secondary=product_image, backref="products")

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    @classmethod
    def create(cls, id, name, amount, price, categories, sizes, colors, images):
        product = cls(name=name, amount=amount, price=price)
        product.id = id
        product.categories = categories
        product.sizes = sizes
        product.colors = colors
        product.images = images
        return product

    def get_id(self):
        return self.id

    def __repr__(self):
        categories = [{'id': category.id, 'name': category.name} for category in self.categories]
        sizes = [{'id': size.id, 'name': size.name} for size in self.sizes]
        colors = [{'id': color.id, 'name': color.name} for color in self.colors]
        images = [{'id': image.id, 'name': image.name} for image in self.images]

        product_json = {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'price': self.price,
            'categories': categories,
            'sizes': sizes,
            'colors': colors,
            'images': images
        }
        return json.dumps(product_json)
