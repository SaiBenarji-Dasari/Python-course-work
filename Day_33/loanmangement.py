from abc import ABC,abstractmethod
class customer:
    def __init__(self,customer_id,name,email,phonenumber,age,income,credit_score):
        self.customer_id=customer_id
        self.name=name
        self.age=age
        self.email=email
        self.phonenumber=phonenumber
        self.age=age
        self.income=income
        self.credit_score=credit_score

    def check_eligibility(self):
        if self.age<21 or self.credit_score< 650 or self.income<25000:
            return False
        return True
    def display_customer(self):
        print('\ncustomer details')
        print('-----------------')
        print('customer_id:', self.customer_id)
        print('name:', self.name)
        print('email:',self.email)
        print('phonenumber:', self.phonenumber)
        print('age:', self.age)
        print('income:',self.income)
        print('credit_score: ',self.credit_score) 

sai=customer(1,'sai','sai@gmail.com','3144861531',25,30000,750)
print("Eligibilty:",sai.check_eligibility)
sai.display_customer()           

kowshik=customer(2,'kowshik','kowshik@gmail.com','31448617979',20,22000,600)
print("Eligibilty:",kowshik.check_eligibility())
kowshik.display_customer()           

class loan(ABC):
    def __init__(self,loan_id,customer,loan_amount,interst_rate,loan_tensure):

        self.loan_id=loan_id
        self.customer=customer
        self.loan_amount=loan_amount
        self.interst_rate=interst_rate
        self.loan_tensure=loan_tensure
        self.repayment_history=[]
        self.status='Applied'
       
    def calculate_emi(self):
        pass
    def check_loan_eligibility(self):
        if not self.customer.check_eligibility():
            self.status='Rejected'
            return False
        return True
    def sanction_loan(self):
        if self.status=="Rejected":
            print('Loan application was rejected')
            return
        if not self.check_loan_eligibility():
            print('customer is not eligible for the loan')
            return
        self.status="sanctioned"
        print("\nLoan sanctioned successfully")
    def repay(self,amount):
        if self.status!='sanctioned':
            print('repayment is not allowed')
            print('Lon status:',self.status)
            return
        if amount <=0:
            print('Invalid repayment amount')
            return
        if amount > self.__balance:
            print('Repayment amount is greater than outstanding balance')
            return
        self.__blance -= amount
        self.__total_paid += amount
        self.repayment_history.append(amount)

        print('\nRepayment successfully')
        print('amount paid    :',amount)
        print('outsanding balance  :',self.__blance)

        if self.__blance==0:
            self.status='closed'
            print('loan closed successfully')

    def get_balance(self):
        return self.__balnce 
    def get_loan_amount(self):
        return self.__loan_amount
    def get_total_paid(self):
        return self.__total_paid

    def display_statement(self):

        print('\n') 
        print('='*40)
        print('Loan satement') 
        print('='*40)

        print('Loan ID                       :', self.loan_id)  
        print('customer Name                 :' ,self.customer)
        print('Loan Amount                   :', self.loan_amount)
        print('Intrest Rate                  :', self.interst_rate)
        print('Tensure                       :', self.loan_tensure)
        print('Loan Status                   :', self.status)

        print('\nRepayment_history')

        if not self.repayment_history:
            print("no repayment mod")
        else:
            for i in range(len(self.repayment_history)):
                print(f"Payment {i+1}       : {self.repayment_history[i]}")
        print('='*40)

    def __str__(self):
        return (
            f"Loan ID: {self.loan_id},"
            f" Customer:  {self.customer.name},"
            f"Loan Amount: {self.loan_amount},"
            f"Otstanding:  {self.__blance}"
        )                 