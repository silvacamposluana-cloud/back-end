from random import choice
aluno1=str(input('o primeiro aluno: '))
aluno2=str(input('o segundo aluno: '))
aluno3=str(input('o terceiro aluno: '))
aluno4=str(input('o quarto aluno: '))
lista= [aluno1,aluno2,aluno3,aluno4]
ecolhido=choice(lista)#escolhe um da lista 
print('o aluno ecolhio foi {}'.format(ecolhido))
