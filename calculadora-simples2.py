#Calculadora simples com funções
#Menu principal da calculadora
def Menu():
    print('------ MENU PRINCIPAL ------')
    print('-> Insira as informações necessárias:')
    valor1 = int(input('Qual o primeiro valor?'))
    valor2 = int(input('Qual o segundo valor?'))
    ope = str(input('Qual a operação a ser feita?'))
    condicao(valor1, valor2, ope)

def soma(valor1, valor2):
    resultado = valor1 + valor2
    print(f'O resultado da soma é {resultado}!')

def substracao(valor1, valor2):
    resultado = valor1 - valor2
    print(f'O resultado da subtração é {resultado}!')

def divisao(valor1, valor2):
    resultado = valor1 / valor2
    print(f'O resultado da divisão é {resultado}!')

def porcentagem(valor1, valor2):
    resultado = valor1 % valor2
    print(f'A porcentagem de {valor1} e {valor2} é {resultado}%!')

def condicao(valor1, valor2, ope):
    if ope == 'soma':
        soma(valor1, valor2)
    elif ope == 'subtracao':
        substracao(valor1, valor2)
    elif ope == 'divisao':
        divisao(valor1, valor2)
    elif ope == 'porcentagem':
        porcentagem(valor1, valor2)
    else:
        print('------ Valores inválidos, tente novamente! ------')
        Menu()

Menu()
