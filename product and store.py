class Product:
    def __init__(self, name, quantity):  # ต้องมี __ สองข้าง
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):  # ต้องมี __ สองข้าง
        self.products = []

    def add_product(self, name, quantity):
        obj = Product(name, quantity)
        if obj.name in self.__products:
            self.__products[obj.name].quantity += obj.quantity
        else:
            self.__products[obj.name] = obj

    def show_products(self):
        for name ,obj in self.__products.items():
            print(f"{obj.name}  :  {obj.quantity}")

my_store = Store()
my_store.add_product("ยาสีฟัน", 90)
my_store.add_product("ถุงขยะ", 50)
my_store.show_products()
