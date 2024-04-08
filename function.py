#basic function
def add_nums():
    print(3 + 4)  

add_nums()

#Function Arguments/ Parameters
def add_nums(a,b,c):
    sum = a+b+c
    return sum
total = add_nums(1,2,3)
print(total)

#Arbitrary Arguments, *args = if you dont know the number of args to be passed
def add_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(add_nums(1,2,3))


#Arbitrary Keyword Arguments, **kwargs
def add_ages(**ages):
    sum = 0
    for i,j in ages.items():
        sum += j
    return sum

print(add_ages(mutemi= 20, kioko= 30))

















def greet(name, greeting):
    print(f'{greeting}, {name}' )

greet('Alex', 'Hello')


