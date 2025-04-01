from peewee import *

db = SqliteDatabase('gestionStock.db')

class Product(Model):
    product_name = CharField(max_length=100)
    product_price = FloatField(default=0)
    
    class Meta:
        database = db
        

if __name__ == "__main__":
    # connect to database db
    # db.connect()
    # create our table Product
    # db.create_tables([Product])
    
    # Wireless Earbuds, Bluetooth 5.3 Headphones in Ear with 4 ENC | 19.99
    # CRUD Create Read Update Delete
    lottaBudy = Product.create(product_name = 'Lottabody Coconut Oil', product_price = 3.98)
    print(lottaBudy)