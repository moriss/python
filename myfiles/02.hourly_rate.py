#Calculate hourly rate with time and a half over 40 hours 
hours = input("Enter Weekly Hours ")
rate = input("Enter Hourly Rate ")
hours = int(hours)
rate = int(rate)
if(hours>40):
	srate=(hours*rate)+(40-hours*0.5)
	try:
		print("Super Rate " , strate)
	except:
		print("Super Rate " , srate) 
elif (hours<40):
	print("Basic Rate ", hours*rate)
