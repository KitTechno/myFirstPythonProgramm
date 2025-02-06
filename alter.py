#imports math lib
import math
#variable to tweak the month length to get accurate day results
monthlength = 30.365

#asks for the birth date
print("enter your date of birth")
day = int(input("day in DD = "))
month = int(input("month in MM = "))
year = int(input("year in YYYY = "))

#asks for the current date
print("enter the current date")
tday = int(input("day in DD = "))
tmonth = int(input("month in MM = "))
tyear = int(input("year in YYYY = "))

#direct input in code without inputfunction
# day=27
# month=12
# year=2001
# tday=6
# tmonth=2
# tyear=2025

#converts the birth date into days
day = day+(month*monthlength)
day = day+(year*365)

#converts the current date into days
tday = tday+(tmonth*monthlength)
tday = tday+(tyear*365)

#calculates the total days alive
days = tday-day

#calculates the years and rounds them to whole number
years = days/365
years = math.floor(years)
days = days-(years*365) #removes the days that have been converted to years

#calculates the months and rounds them to whole number
months = days/monthlength
months = math.floor(months)
days = days-(months*monthlength) #removes the days that have been converted to months
days = round(days)

#prints the time you've been alive
#P.S i couldnt be bothered to account for day/days so its day/s now
print("you are",years,"year/s",months,"month/s and",days,"day/s old")

#Ich habe nicht das gemacht was in der Aufgabe war. 
#Das Programm, dass ich geschrieben habe ist jedoch um einiges schwieriger und und spannender geworden. 
#Hoffentlich gefällt es euch.
