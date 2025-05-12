


products=[
    {'id':1,'name':'t-shirt','price':12.99,'created_date':'22-01-01','is_on_sale':False,'sale_price':None},
    {'id':2,'name':'shoes','price':22.45,'created_date':'22-01-01','is_on_sale':True,'sale_price':None},
    {'id':3,'name':'dress-shirt','price':43.00,'created_date':'22-01-01','is_on_sale':False,'sale_price':None},
    {'id':4,'name':'socks','price':14.99,'created_date':'22-01-01','is_on_sale':True,'sale_price':7.99},
    {'id':5,'name':'trousers','price':32.50,'created_date':'22-01-01','is_on_sale':True,'sale_price':None},
    {'id':6,'name':'jacket','price':150.00,'created_date':'22-01-01','is_on_sale':False,'sale_price':None},
]
class Process_list_of_product:
    def __init__(self,products):
        self.products=products
    def greater_25_usd(self):
        a=len(self.products);
        products_greater_25 = {};
        for product in range(0, a):

            if (self.products[product]['price'] > 25):
                products_greater_25[product] = {self.products[product]['name']};
        print('These products have a price greater than 25:', products_greater_25);
    def products_sale(self):
        a = len(self.products);
        products_on_sale = {};
        for product in range(0, a):

            if (self.products[product]['is_on_sale']==True):
                products_on_sale[product] = {self.products[product]['name']};
        print('These products are on Sale:', products_on_sale);
    def products_no_price(self):
        a = len(self.products);
        products_no_price = {};
        for product in range(0, a):

            if (self.products[product]['is_on_sale']==True and self.products[product]['sale_price']==None):
                products_no_price[product] = {self.products[product]['name']};
        print('These products are on sale but doesnt contain the sale price:', products_no_price);


myproduct=Process_list_of_product(products)
myproduct.greater_25_usd()
myproduct.products_sale()
myproduct.products_no_price()
