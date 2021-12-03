import requests
import os
import json
DAYS_IN_WEEK = 7
inp = input("Domain Name (ex : google.com) : ")
res = requests.get(
    "https://input.payapi.io/v1/api/fraud/domain/age/"+inp)
r1 = res.text
a = json.loads(r1)
number_of_days = a["result"]
st=a["message"]
year = int(number_of_days / 365)
week = int((number_of_days % 365) /DAYS_IN_WEEK)
days = (number_of_days % 365) % DAYS_IN_WEEK
print ("Days : ",days)
print ("Weeks :",week)
print("Years : ",year)
print (st)


