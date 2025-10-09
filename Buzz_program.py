print('BUZZ FIZZ PROGRAM')

till_num = int(input('Enter the specified number: '))//input
my_list = []

for num in range(1, till_num + 1):
    if num % 5 == 0 and num % 3 == 0:
        result = 'BuzzFizz'
    elif num % 5 == 0:
        result = 'Buzz'
    elif num % 3 == 0:
        result = 'Fizz'
    else:
        result = num
    
    my_list.append(result)

print(my_list)
