#Prompt the user for their working hours and rate per hour to calculate their gr
oss pay
hours = input("How many hours do you work per week? ");
hours = float(hours);
rate = input("How much do you get paid per hour? ");
rate = float(rate);
pay = float(hours * rate);
print ("Your weekly gross pay is " , pay);

