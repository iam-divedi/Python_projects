print('FIZZ BUZZ PROGRAM')
till_num = int(input('Enter the specified number: '))
my_list = []

for num in range(1, till_num + 1):
    result = ""

    if num % 3 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        result += 'Buzz'

    if result == "":
        result = num

    my_list.append(result)

print(my_list)
