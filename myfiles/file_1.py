#Prompt the user for their working hours and rate per hour to calculate their gross pay
hours = input("How many hours do you work per week? ");
rate = input("How much do you get paid per hour? ");

pay = float(hours) * float(rate);
print ("Your weekly gross pay is " , pay);

