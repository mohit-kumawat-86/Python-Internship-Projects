age =  int(input("Enter your age:"))
ticket = True
if age > 18 :
    print("You can watch the movie")
    if ticket == True :
        print("You can go inside")
elif age < 15:
    print("You can watch the movie with parents")
else:
    print("Not allowed")