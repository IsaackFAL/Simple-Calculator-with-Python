#Menu simples da calculadora
def menu_principal():
    print('------ CALCULADORA ------')
    print('-> Siga os passos a seguir:')

menu_principal()
valor1 = int(input('Digite o primeiro valor'))
valor2 = int(input('Digite o segundo valor'))
ope = input('Qual será a operação?')

#Operações Principais
if ope == 'soma':
    print(f'Seu resultado é: {valor1 + valor2}')
elif ope == 'subtração':
    print(f'Seu resultado é: {valor1 - valor2}')
elif ope == 'divisao':
    print(f'Seu resultado é: {valor1 / valor2}')
elif ope == 'porcentagem':
    print(f'Seu resultado é: {valor1 % valor2}%')
else: 
    print('Inválido, tente novamente!')
    ope = input('Qual será a operação?')