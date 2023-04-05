#def func():
#    numbers = [3, 8, 5, 0, 1, 5, 7, 2, 6]
#    order = input('Select the order in which the numbers will appear (asc, desc or none): ')
#    if order == 'asc': 
#        numbers.sort()
#        print(numbers)
#        ans = input("That worked! Do you want to try again? ")
#        if ans == 'yes':
#            func()
#    elif order == 'desc':
#        numbers.sort(reverse=True)
#        print(numbers)
#        ans = input("That worked! Do you want to try again? ")
#        if ans == 'yes':
#            func()
#    elif order == 'none':
#        print (numbers)
#        ans = input("That worked! Do you want to try again? ")
#        if ans == 'yes':
#            quit()
#    else:
#        print('Your input was incorrect. Try again.')
#        func()
#func()

#numbers = [3, 8, 5, 0, 1, 5, 7, 2, 6]

import inquirer
questions = [
  inquirer.List('size',
                message="What size do you need?",
                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
            ),
]
answers = inquirer.prompt(questions)
print (answers["size"])