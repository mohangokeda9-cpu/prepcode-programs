amount=94000
withdrawl_amount=input("enter the amount:")
if len(withdrawl_amount)<=amount and amount%500==0:
    print("transation is allowed")
else:
    print("trasantion id not allowed")