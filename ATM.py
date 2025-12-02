balance = 50000
pin = 8619

user_pin = int(input("Enter your pin :"))
if user_pin == pin :
    print ("Your balance is :" , balance)
    amount = int (input ("Enter amount to withdrawal :"))
    balance -= amount # balance = balance - amount
    print ("congrats amount recived", "new balance is" , balance)
else :
    print(" Pin incorrect")