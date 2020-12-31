# Importing the required modules 
import random
import string
import time
from os import system
from datetime import datetime
##**##

#Clear Screen function
def clear():
    _ = system('cls')
##**##

# Start Screen function
def start_screen():
    clear()
    global name_emp
    global ein
    print(''.center(80, '-'))
    print('Employee Payroll System'.upper().center(80))
    print(''.center(80, '-'))
    dt = datetime.now()
    print(dt.strftime('%c'))
    print('Enter the details:'.upper())
    name_emp = input("Name of the employee: ")
    ein = input("EIN (Employee Indetification Number): ")
    def pay_basis_fun():
        pay_basis = input('''How are you paid?
        Hourly (h/H)
        Daily (d/D)
        Weekly (w/W)
        Monthly (m/M)
        : ''')
        if pay_basis == 'h' or pay_basis == 'H' or pay_basis == 'Hourly' or pay_basis == 'hourly':
            hourly()
        elif pay_basis == 'd' or pay_basis == 'D' or pay_basis == 'Daily' or pay_basis == 'daily':
            daily()
        elif pay_basis == 'w' or pay_basis == 'W' or pay_basis == 'weekly' or pay_basis == 'Weekly':
            weekly()
        elif pay_basis == 'm' or pay_basis == 'M' or pay_basis == 'monthly' or pay_basis == 'Monthly':
            monthly()
        else:
            print("Please enter the correct option!")
            pay_basis_fun()
    pay_basis_fun()
##**##

# Payment functions:
def hourly():
    hour = int(input("How many hours worked: "))
    rate = int(input("Hourly rate: "))
    gross_payment = hour * rate
    print('Gross Payment: Rs. ' + str(gross_payment))
    print('TAX = 8%')
    gross_payment = gross_payment - (gross_payment*8/100)
    print('Gross Payment: Rs. ' + str(gross_payment))
    deduct = int(input("Deduction: "))
    gross_payment = gross_payment - deduct
    print('Gross Payment: Rs. ' + str(gross_payment))
    bonus = int(input("Bonus: "))
    net_payment = gross_payment + bonus
    print('Net Payment: Rs. ' + str(net_payment))
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait..')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait...')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print(''.center(80, '*'))
    print('PAYMENT RECEIPT'.center(80, '-'))
    dt = datetime.now()
    receipt_time = dt.strftime('%c')
    print('Issued on: ' + receipt_time)
    print('Name: '+ name_emp)
    print('EIN (Employee Identification Number): ' + ein)
    print('NET Payment: Rs. '+ str(round(net_payment)))
    print('To receive the payment please give the 16 digit token to the cashier.')
    pay_token = string.hexdigits
    print ( 'Your token: '+''.join(random.choice(pay_token) for i in range(16)) )
    print(''.center(80, '*'))
    print("Press any key to exit or press n/N to make another receipt")
    opt = input(">>>")
    if opt == 'n' or opt == 'N':
        start_screen()
    else:
        exit()

def daily():
    days = int(input("How many days worked: "))
    rate = int(input("Daily rate: "))
    gross_payment = days * rate
    print('Gross Payment: Rs. ' + str(gross_payment))
    print('TAX = 8%')
    gross_payment = gross_payment - (gross_payment*8/100)
    print('Gross Payment: Rs. '+ str(gross_payment))
    deduct = int(input("Deduction: "))
    gross_payment = gross_payment - deduct
    print('Gross Payment: Rs. ' + str(gross_payment))
    bonus = int(input("Bonus: "))
    net_payment = gross_payment + bonus
    print('Net Payment: Rs. ' + str(net_payment))
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait..')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait...')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print(''.center(80, '*'))
    print('PAYMENT RECEIPT'.center(80, '-'))
    dt = datetime.now()
    receipt_time = dt.strftime('%c')
    print('Issued on: ' + receipt_time)
    print('Name: '+ name_emp)
    print('EIN (Employee Identification Number): ' + ein)
    print('NET Payment: Rs. '+ str(round(net_payment)))
    print('To receive the payment please give the 16 digit token to the cashier.')
    pay_token = string.hexdigits
    print ( 'Your token: '+''.join(random.choice(pay_token) for i in range(16)) )
    print(''.center(80, '*'))
    print("Press any key to exit or press n/N to make another receipt")
    opt = input(">>>")
    if opt == 'n' or opt == 'N':
        start_screen()
    else:
        exit()

def weekly():
    weeks = int(input("How many weeks worked: "))
    rate = int(input("Weekly Rate: "))
    gross_payment = weeks * rate
    print('Gross Payment: Rs. ' + str(gross_payment))
    print('TAX = 8%')
    gross_payment = gross_payment - (gross_payment*8/100)
    print('Gross Payment: Rs. '+ str(gross_payment))
    deduct = int(input("Deduction: "))
    gross_payment = gross_payment - deduct
    print('Gross Payment: Rs. ' + str(gross_payment))
    bonus = int(input("Bonus: "))
    net_payment = gross_payment + bonus
    print('Net Payment: Rs. ' + str(net_payment))
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait..')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait...')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print(''.center(80, '*'))
    print('PAYMENT RECEIPT'.center(80, '-'))
    dt = datetime.now()
    receipt_time = dt.strftime('%c')
    print('Issued on: ' + receipt_time)
    print('Name: '+ name_emp)
    print('EIN (Employee Identification Number): ' + ein)
    print('NET Payment: Rs. '+ str(round(net_payment)))
    print('To receive the payment please give the 16 digit token to the cashier.')
    pay_token = string.hexdigits
    print ( 'Your token: '+''.join(random.choice(pay_token) for i in range(16)) )
    print(''.center(80, '*'))
    print("Press any key to exit or press n/N to make another receipt")
    opt = input(">>>")
    if opt == 'n' or opt == 'N':
        start_screen()
    else:
        exit()

def monthly():
    months = int(input("How many months worked: "))
    rate = int(input("Monthly rate: "))
    gross_payment = months * rate
    print('Gross Payment: Rs. ' + str(gross_payment))
    print('TAX = 8%')
    gross_payment = gross_payment - (gross_payment*8/100)
    print('Gross Payment: Rs. '+ str(gross_payment))
    deduct = int(input("Deduction: "))
    gross_payment = gross_payment - deduct
    print('Gross Payment: Rs. ' + str(gross_payment))
    bonus = int(input("Bonus: "))
    net_payment = gross_payment + bonus
    print('Net Payment: Rs. ' + str(net_payment))
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait..')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait...')
    time.sleep(0.5)
    clear()
    print('Making payment receipt')
    print('Please Wait.')
    time.sleep(0.5)
    clear()
    print(''.center(80, '*'))
    print('PAYMENT RECEIPT'.center(80, '-'))
    dt = datetime.now()
    receipt_time = dt.strftime('%c')
    print('Issued on: ' + receipt_time)
    print('Name: '+ name_emp)
    print('EIN (Employee Identification Number): ' + ein)
    print('NET Payment: Rs. '+ str(round(net_payment)))
    print('To receive the payment please give the 16 digit token to the cashier.')
    pay_token = string.hexdigits
    print ( 'Your token: '+''.join(random.choice(pay_token) for i in range(16)) )
    print(''.center(80, '*'))
    print("Press any key to exit or press n/N to make another receipt")
    opt = input(">>>")
    if opt == 'n' or opt == 'N':
        start_screen()
    else:
        exit()
##**##

# Opening
clear()
print(''.center(80, '-'))
print('Employee Payroll System'.upper().center(80))
print(''.center(80, '-'))
print('This is a Payroll System for Employees made by Aditya Kumar')
input("Press Enter to continue...")
clear()
## *X* ##
start_screen()
exit()