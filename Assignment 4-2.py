name = input("Employee's name: ")
shifts = int(input("Number of Shifts: "))
transactions = int(input("Number of transactions: "))
T_dollar_value = float(input("Transaction dollar value: "))

product_score = (T_dollar_value / transactions) / shifts
bonus = product_score

if product_score <= 30:
    bonus = 50.00
else:
    if 31 <= product_score <= 69:
        bonus = 75.00
    else:
        if 70 <= product_score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

print(f'Employee Name: {name}')
print(f'Employee Bonus: ${bonus}')