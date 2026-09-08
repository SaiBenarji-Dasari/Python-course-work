class Flipkart:
    products={'mobile': 2000,"headset":15000,"laptops":1000000}
    discount=30 
    @classmethod
    def display(cls):
        print(cls.products)


    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name}, Wellcome to the flipkart")
    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on, grab the products..")

    
sai=Flipkart()
sai.userinfo('sai','111344748','hyd')
sai.displaydiscount()
kowshik=Flipkart()
kowshik.userinfo('kowshik','111344748','mtm')
kowshik.displaydiscount()
benarji=Flipkart()
benarji.userinfo('benarji','111344748','che')
benarji.displaydiscount()

#using object  --> inst method, cls method, sta mathod, clss attr, ins attr
#using class --> cls method, sta method, class attr

print(sai.products)
print(sai.name)
print(Flipkart.products)