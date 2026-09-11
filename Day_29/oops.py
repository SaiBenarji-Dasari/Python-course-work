class Flipkart:
    products={'shirts':10000,"handbag":2345,"pants":3444}
    discount=20

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name} welcome to the app")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on, grab the products....")


kowshik=Flipkart()
kowshik.userinfo("kowshik",7894561230,'hyb')
kowshik.displaydiscount()
kowshik.display()
phani=Flipkart()
phani.userinfo("officer",1264574373,"che")
phani.displaydiscount()
phani.display()

print(kowshik.products)
print(kowshik.name)

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)
#using a object we can access-->instans methode , class methode, static methode ,class attribute, instance attribute
#using class we can access-->class methode static methode, class attribute