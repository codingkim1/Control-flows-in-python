#simple example:
snack = lambda : print('njugu')
snack()

#its normal function
def snack():
  print('njugu')
snack()

#A lambda function with arguments
def num_square(num):
    return num ** 2

print(num_square(5))

#rewriting in lambda fn
num_square = lambda num : num ** 2

print(num_square(6)) 












