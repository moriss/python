#Test user's number is under specified thresholds with elif
x = input("Enter a number")
z = int(x)
if(z < 0):
        print("Please type a positive number ")
elif(z < 10):
        print("Ok so", z , " is under 10" )
elif(z < 50):
        print("Now ", z , " is less than 50")

else :
        print("Waw!", z ,  " is over 50 ")

