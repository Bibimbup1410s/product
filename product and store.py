class Product:
    def __init__(self, name, quantity):  # ต้องมี __ สองข้าง
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):  # ต้องมี __ สองข้าง
        self.products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.products.append(product)

    def show_products(self):
        print("รายการสินค้าที่มีในร้าน:")
        for product in self.products:
            print(f"- {product.name}: {product.quantity} ชิ้น")

my_store = Store()
my_store.add_product("ยาสีฟัน", 90)
my_store.add_product("ถุงขยะ", 50)
my_store.show_products()
