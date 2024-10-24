#let the user know they did not enter a number

zint = input("Enter a number ")
try:
        x = int(zint)
        print(x)
except:
        x=-1
if x < 0:
        print("You have not entered a number ")

