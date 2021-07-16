# Calculando o fatorial de um número:
def fatorial(num):
    if num < 0:
        print('Não existe fatorial de número negativo. tente novamente!')
    elif num == 1:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact


num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial(num)}')
