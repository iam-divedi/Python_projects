import random
while True:
    print(f'Number of dice is {random.randint(1, 6)}')
    user_input = input('do you want to conntinue y/n ')
    if user_input=='n':
            break
