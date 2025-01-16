from functions import *
import os

while True:
    os.system('cls')
    print("\033[92m----------------------- [ MORUSU_PASSWORD ] ---------------------\n")
    print("---------------------------------------------------------------")
    print("[ 1 ] Gerar senha com letras (Fraca)")
    print("---------------------------------------------------------------")
    print("[ 2 ] Gerar senha com números  (Fraca)")
    print("---------------------------------------------------------------")
    print("[ 3 ] Gerar senha com letras e números  (Mediana)")
    print("---------------------------------------------------------------")
    print("[ 4 ] Gerar senha com letras e caracteres especiais  (Forte)")
    print("---------------------------------------------------------------")
    print("[ 5 ] Gerar senha com números e caracteres especiais  (Forte)")
    print("---------------------------------------------------------------")
    print("[ 6 ] Gerar senha com letras, números e caracteres especiais (Mais Forte)")
    print("---------------------------------------------------------------")
    print("[ 0 ] Sair")
    print("---------------------------------------------------------------")
    option = input("Selecione uma opção: ")

    match option:
        case "1":
            print(generatePasswordLow())
            warning()
        case "2":
            print(generatePasswordMedium())
            warning()
        case "3":
            print(generatePasswordGood())
            warning()
        case "4":
            print(generatePasswordGood2())
            warning()
        case "5":
            print(generatePasswordGood3())
            warning()
        case "6":
            print(generatePasswordHard())
            warning()        
        case "0":
            os.system('cls')
            print("Saindo...")
            break
        case _:
            print("Opção inválida")
