    #Try and except with the hourly rate calculation. (for non numerical chars)
hours =input("Hours: ")
rate =input("Hourly rate: ")
try:
        hours=float(hours)
        rate=float(rate)
        print(hours*rate)
except:
        print("Please enter valid digits")
        quit

