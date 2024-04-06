#if..else
bill = 1500
discount = 100
if bill > 2000:
    print('Bill is greater than 2000')
    bill = bill - discount
else:
    print('Bill is below 2000!')

print('Final bill: ' + str(bill))
# print(f'Final bill:   {bill}')

#if..elif..else

grade = 65
if grade >=90:
    print('A')
elif grade >=80:
    print('B')
elif grade >=70:
    print('C')
elif grade >=60:
    print('D')
else:
    print('E')

