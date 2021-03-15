from datetime import datetime

print("Please enter the created date of the server")
d1=input("Day")
m1=input("Month")
y1=input("Year")
print("Please enter the deleted date of the server")
d2=input("Day")
m2=input("Month")
y2=input("Year")

create_date=datetime(int(y1),int(m1),int(d1)).date()
delete_date=datetime(int(y2),int(m2),int(d2)).date()
cost=0
differnce=(delete_date - create_date).days
if differnce == 0:
    cost=20
elif (differnce > 1) and (differnce < 30):
    cost=30*differnce
elif (differnce > 30) and (differnce < 365):
    num_months = (delete_date.year - create_date.year) * 12 + (delete_date.month - create_date.month)
    cost=1000*num_months
else:
    cost=20000
print("Cost = ",cost)
