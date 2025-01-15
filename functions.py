import random
import sys
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

caracteres = ['$','#','@','!','&','^']
numbers = ["0","1","2","3","4","5","6","7","8","9"]

def warning():
    newPassword = input("Deseja gerar uma senha? (s/n) ")
    if newPassword == "s" or newPassword == "S":
        return True
    elif newPassword == "n" or newPassword == "N":
        os.system('cls')
        sys.exit("Saindo...")
    
# def LowerUpper():
#     if password == letters:


def generatePasswordLow(): # OK
    while True:
        quantity = int(input("Escolha o tamanho da senha: "))
        if quantity >= 4 and quantity <= 15:
            password = ''
            for i in range(quantity):
                password += (random.choice(letters))
            return f'Senha gerada com sucesso: {password}'
        print("O tamanho da senha deve ser maior ou igual a 4 e menor ou igual a 15")

def generatePasswordMedium(): #OK
    while True:
        quantity = int(input("Escolha o tamanho da senha: "))
        if quantity >= 4 and quantity <= 15:
            password = ''
            for i in range(quantity):
                password += (random.choice(numbers))
            return f'Senha gerada com sucesso: {password}'
        print("O tamanho da senha deve ser maior ou igual a 4 e menor ou igual a 15")

def generatePasswordGood(): # OK
   while True:
        quantity = int(input("Escolha o tamanho da senha: "))
        if quantity >= 4 and quantity <= 15:
            password = ''
            for i in range(quantity):
                password += (random.choice(numbers) + random.choice(letters))
            return f'Senha gerada com sucesso: {password[:quantity]}'
        print("O tamanho da senha deve ser maior ou igual a 4 e menor ou igual a 15")

def generatePasswordGood2(): # OK
   while True:
        quantity = int(input("Escolha o tamanho da senha: "))
        if quantity >= 4 and quantity <= 15:
            password = ''
            for i in range(quantity):
                password += (random.choice(letters) + random.choice(caracteres))
            return f'Senha gerada com sucesso: {password[:quantity]}'
        print("O tamanho da senha deve ser maior ou igual a 4 e menor ou igual a 15")

def generatePasswordGood3(): # OK
   while True:
        quantity = int(input("Escolha o tamanho da senha: "))
        if quantity >= 4 and quantity <= 15:
            password = ''
            for i in range(quantity):
                password += (random.choice(numbers) + random.choice(caracteres))
            return f'Senha gerada com sucesso: {password[:quantity]}'
        print("O tamanho da senha deve ser maior ou igual a 4 e menor ou igual a 15")               

def generatePasswordHard(): # OK
    while True:
        quantity = int(input("Escolha o tamanho da senha: "))
        if quantity >= 4 and quantity <= 15:
            password = ''
            for i in range(quantity):
                password += (random.choice(caracteres) + random.choice(numbers) + random.choice(letters))
            return f'Senha gerada com sucesso: {password[:quantity]}'
        print("O tamanho da senha deve ser maior ou igual a 4 e menor ou igual a 15")