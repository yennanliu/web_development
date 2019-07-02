from config import *

class ProductData(db.Model):
    __tablename__ = 'products'

    def __init__(self
                 , title
                 , description
                 , sold
                 ):
        self.title = title
        self.description = description
        self.sold = sold