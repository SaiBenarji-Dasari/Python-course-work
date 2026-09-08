from abc import ABC,abstractmethod

class  phonepay(ABC):
    def senderinnfo(self):
        print("You can enter their number or QR")
    def amount(self):
        print("You can enter amount")
    def  pin(self):
        print("You need to enter pin")

    @abstractmethod
    def transcation(self):
        pass

class HDFC(phonepay):
    def transcation(self):
        print("Payment using hdfc bank")     
class SBI(phonepay):
    def transcation(self):
        print("Payment using sbi bank")
class HSBC(phonepay):
    def transcation(self):
        print("Payment using hsbc bank")    
class IDFC(phonepay):
    def transcation(self):
        print("Payment using idfc bank")    
class ICIC(phonepay):
    def transcation(self):
        print("Payment using icic bank")                                            
sai=HDFC()
sai.senderinnfo()
sai.amount()
sai.pin()
sai.transcation()
         