import inquirer

sudoku = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

for i in sudoku:
    print (i)

def canvi():
    
    x = int(input('De quina fila vols canviar un valor? '))
    x = x - 1
    y = int(input('De quina columna vols canviar un valor? '))
    y = y - 1
    a = input('Quin valor vols posar-hi? ')

    sudoku[x][y] = a
    for i in sudoku:
            print (i)

    questions = [
        inquirer.List('list',
                    message ="Vols canviar un valor del sudoku? (Només pots posar valors de l'1 al 9)",
                    choices=['Sí', 'No'],
                ),
        ]
    answers = inquirer.prompt(questions)

    if answers['list'] == 'Sí':
        canvi()
    elif answers['list'] == 'No':
        buides = []
        def buida():
            for fil in range(9):
                for col in range(9):
                    if sudoku[fil][col] == 'x':
                        buides.append((fil, col))          
        buida()

        def comp(fil, col, num):
            if num in sudoku[fil]:
                return False
            for i in range(9):
                if sudoku[i][col] == num:
                    return False
            quadfil = (fil // 3) * 3
            quadcol = (col // 3) * 3
            for x in range(quadfil, quadfil + 3):
                for y in range(quadcol, quadcol + 3):
                    if sudoku[x][y] == num:
                        return False
                  
            return True

        def res(buides):
            if len(buides) == 0:
                return True
            fil, col = buides[0]

            for num in range(1, 10):
                if comp(fil, col, str(num)):
                    sudoku[fil][col] = str(num)
                    
                    if res(buides[1:]):
                        return True
                    sudoku[fil][col] = 'x'
            return False
        
        buides = []
        for fil in range(9):
                for col in range(9):
                    if sudoku[fil][col] == 'x':
                        buides.append((fil, col))  
        
        res(buides)

        for fil in sudoku:
            print (fil)

canvi()