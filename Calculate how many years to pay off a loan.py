# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:24:50 2020

@author: frank
"""

"""
To calculate how many months / years it takes to pay off a loan.

This code assumes that the balance, interest rate and monthly payment stays constant.
"""

import datetime
import calendar

balance = 5000
interest_rate = 13 * .01 # which equals 0.13 (13%)
monthly_payment = 500

today = datetime.date.today()

days_in_current_month = calendar.monthrange(today.year, today.month)[1]

days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days = days_till_end_month + 1)

end_date = start_date

count = 0

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment
    count += 1
    balance = round(balance, 2)
    
    if balance < 0:
        balance = 0.00
        years = round(count / 12)
        print("It will take {} months ({} year/s) to pay off with the final payment made on {}".format(count, years, end_date))
        break

    # print(end_date, balance)
    
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days = days_in_current_month)