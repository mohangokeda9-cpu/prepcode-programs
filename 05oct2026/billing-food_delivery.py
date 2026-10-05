food_price=200
quantity=2
delivery_charge=40
discount_percentage=10
subtotal=food_price*quantity 
discount=subtotal*discount_percentage/100
final_bill=subtotal+delivery_charge-discount
print("final bill=",final_bill)