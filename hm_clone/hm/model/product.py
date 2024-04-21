from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from hm import db

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
