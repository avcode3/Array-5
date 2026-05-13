# Problem 2 

'''
Write a program to calculate tax if Salary and Tax Brackets are given as list in the form [ [10000, .3],[20000, .2], [30000, .1], [None, .1]]. You don’t know in the beginning how many tax brackets are there. You have to test for all of them
'''

def calculate_tax(salary,tax_brackets):
    tax_payment = 0
    remaining_money = salary
    for limit,rate in tax_brackets:
        if remaining_money <= 0:
            break
        if limit is None:
            tax_payment = tax_payment + (remaining_money*rate) 
            remaining_money = 0 
        elif limit > remaining_money:
            tax_payment = tax_payment + (remaining_money*rate) 
            remaining_money = remaining_money - limit
        else:
            tax_payment = tax_payment + (remaining_money*rate) 
            remaining_money = 0
    return tax_payment


tax_brackets = [
    [10000, 0.10],
    [20000, 0.20],
    [10000, 0.30],
    [None, 0.40]
]
salary = 71000

tax = calculate_tax(salary, tax_brackets)
print(tax)