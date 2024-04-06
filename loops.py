#For Loops
names = ['Alex', 'Judy', 'Shawn', 'Shania']
for name in names:
    print(name)

#For Loops: Using Range
my_message = 'Hallo World!'
for i in range(6):
    print(my_message)

#While Loops
count = 0
while count <= 4:
    print(count)
    count += 1

#Loop controls: Break and continue
cars = ['premio', 'vits', 'demio', 'fielder', 'note']
fav_car = 'fielder'

for car in cars:
    print(car)
    if car == fav_car:
        print('Got it!')
        break 

#Using while loop
cars = ['premio', 'vits', 'demio', 'fielder', 'note']
fav_car = 'fielder'

length = len(car) #to know how many times we need to iterate based on collection size
count = 0  #used to compare against length 

while count < length:
    print(cars[count])
    if cars[count] == fav_car:
        print('Got it!')
        break 
    count += 1


#Python continue Statement
ages = [20,10,15,25,30]

for age in ages:
    if age < 18:
        continue
    print(age)
        

#Nested Loops
groups = [['Alex', 'Judy'], ['Shawn', 'Shania']]

for group in groups:     #outer loop will iterate over each list in the group
    for name in group:   #inner loop will iterate thr each name in each list
        print(name)


