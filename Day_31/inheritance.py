'''class whatsappV1:
    def messaging(self):
        print("You can sent messages")

class whatsappV2():
    def calls(self):
        print("You can do audio and video calls") 
class whatsappV3(whatsappV2,whatsappV1): # this is multiple inheritance ---> child class calls many parent classes Ex(V3 is child and V2,V1 is parents)
    def status(self):
       print('You can add the status for 24 hours')

a=whatsappV1()
a.messaging()

b=whatsappV2()
b.calls()

c=whatsappV3()
c.messaging()
c.calls()
c.status()'''

# this is Hierarical inheritance --> this was have one parent many childs 
'''class whatsappV1:
    def messaging(self):
        print("You can sent messages")

class whatsappV2(whatsappV1):
    def calls(self):
        print("You can do audio and video calls") 
class whatsappV3(whatsappV1): 
    def status(self):
       print('You can add the status for 24 hours')

a=whatsappV1()
a.messaging()

b=whatsappV2()
b.messaging
b.calls()

c=whatsappV3()
c.messaging()
c.status()'''

# Hybrid inheritance ---> In this we can have combination of classes
'''class whatsappV1:
    def messaging(self):
        print("You can sent messages")
class whatsappV2:
    def extramessage(self):
        print('You can add emojis, stickers and gifts')        
class whatsappV3(whatsappV1,whatsappV2):
    def calls(self):
        print("You can do audio and video calls") 
class whatsappV4(whatsappV3): 
    def status(self):
       print('You can add the status for 24 hours')

a=whatsappV1()
a.messaging()

b=whatsappV2()
b.extramessage()

c=whatsappV3()
c.messaging()
c.extramessage()
c.calls()


d=whatsappV4()
d.messaging()
d.extramessage()
d.calls()
d.status()'''

# Using super method when we have same methods in other class also we use this 
'''class whatsappV1:
    def status(self):
        print('You can add images and videos')
class whatsappV2(whatsappV1):
    def status(self):
        super().status()
        print('You can add music and stickers')
class whatsappV3(whatsappV2):
    def status(self):
        super().status()
        print('You canlike and recation')

a=whatsappV3()
a.status()'''                        

class whatsappV1:
    def status(self):
        print('You can add images and videos')
class whatsappV2:
    def status(self):
        print('You can add music and stickers')
class whatsappV3(whatsappV2,whatsappV1):
    def status(self):
        whatsappV1.status(self)
        whatsappV2.status(self)
        print('You canlike and recation')

a=whatsappV3()
a.status()