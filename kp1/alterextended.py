#imports datetime lib
import datetime


#asks for the birth date
print("enter your date of birth")
bday = int(input("day in DD = "))
bmonth = int(input("month in MM = "))
byear = int(input("year in YYYY = "))

#direct input in code without inputfunction currently programmers birth date
# day.day=27
# month.month=12
# year.year=2001

#gets the current date
tday = datetime.datetime.now().day
tmonth = datetime.datetime.now().month
tyear = datetime.datetime.now().year

#calculates the number of total days since birth of christ and since birth of user
bdays=bday+(bmonth*30)+(byear*365)
tdays=tday+(tmonth*30)+(tyear*365)

#calculates the difference between age of christ at birth of user and current date
days=tdays-bdays
#calculations for commonly used time measures
months=days//30
years=days//365
hours=days*24
minutes=hours*60
seconds=minutes*60
print("you are alive for")
print(seconds,"seconds")
print(minutes,"minutes")
print(hours,"hours")
print(days,"days")
print(months,"months")
print(years,"years")
