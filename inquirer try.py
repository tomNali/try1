import inquirer

x = 0
while x > 5:
    x += 1
    if x == 3:
        break
print(x)    
#questions = [
#  inquirer.List('size',
#                message="What size do you need?",
#                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#            ),
#]
#answers = inquirer.prompt(questions)
#print (answers["size"])

questions = [
  inquirer.List('list',
                message ="What order do you want the list to be?",
                choices=['Ascendant', 'Descendant', 'None'],
            ),
]
answers = inquirer.prompt(questions)
print (answers["list"])

