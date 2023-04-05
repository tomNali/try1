import inquirer

def func():
            
    f1 = (" a b c | d e f | g h i ") 
    print(f1)
    f2 = (" a b c | d e f | g h i ")
    print(f2)
    f3 = (" a b c | d e f | g h i ")
    print(f3)
    print(" --------------------- ")
    f4 = (" a b c | d e f | g h i ")
    print(f4)
    f5 = (" a b c | d e f | g h i ")
    print(f5)
    f6 = (" a b c | d e f | g h i ")
    print(f6)
    print(" --------------------- ")
    f7 = (" a b c | d e f | g h i ")
    print(f7)
    f8 = (" a b c | d e f | g h i ")
    print(f8)
    f9 = (" a b c | d e f | g h i ")
    print(f9)

    def canvi():

        fila = input("De quina fila vols canviar un valor? (Introdueix només un número de l'1 al 9) ")
        col = input("De quina columna de la fila " + str(fila) + " vols canviar el valor? (Introdueix la lletra que representi la columna) ")
        valor = str(input("Quin valor vols posar en aquesta posició? "))  

        if fila == 1:    

            f1 = f1.replace(col, valor)

        if fila == 2:    

            f2 = f2.replace(col, valor)

        if fila == 3:    

            f3 = f3.replace(col, valor)

        if fila == 4:    

            f4 = f4.replace(col, valor)

        if fila == 5:    

            f5 = f5.replace(col, valor)

        if fila == 6:    

            f6 = f6.replace(col, valor)

        if fila == 7:    

            f7 = f7.replace(col, valor)

        if fila == 8:    

            f8 = f8.replace(col, valor)

        if fila == 9:    

            f9 = f9.replace(col, valor)

        questions = [
            inquirer.List('list',
                        message ="Vols canviar un altre valor? ",
                        choices=['Sí', 'No'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        print (answers["list"])

        if answers['list'] == 'Sí':
            canvi()
        else:

            print(f1)
            print(f2)
            print(f3)
            print(" --------------------- ")
            print(f4)
            print(f5)
            print(f6)
            print(" --------------------- ")
            print(f7)
            print(f8)
            print(f9)

    canvi()

func()