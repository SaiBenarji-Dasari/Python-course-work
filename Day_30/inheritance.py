class whatsappV1:
    def __init__(self,name):
        self.name=name
        print(f":Welcome to the whatsapp - V1 {self.name}!")

    def messaging(self):
        print("You can sent messages")

class whatsappV2(whatsappV1):
    def __init__(self, name):
        self.name=name
        print(f"Welcome to the whatsapp -V2 {self.name}!")

    def calls(self):
        print(f"You can do audio and video calls") 

sai=whatsappV1('sai')
sai.messaging()

benarji=whatsappV2('benarji')
benarji.messaging()
benarji.calls()