# print the leap year;
year=45

if (year%4==0 and year%100!=0):
    print("it is leap year",year)
elif(year%400==0):
    print("it leap year", year) 
else:
    print("it is not leap year", year)       

