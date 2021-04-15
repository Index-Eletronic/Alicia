'''
Faça um programa que insira as palavras numa lista e diga se estão corretas..
'''
import random
from random import randint
from time import sleep
#import playsound

print('-=' * 10, "\33[0;30;41mBEM VINDO A PROFa.ALICIA V1.0\33[m", '-=' * 10 )
print()
print('O QUE VOCÊ GOSTARIA DE ESTUDAR HOJE?')
print('ESCOLHA A OPÇÃO:')
print('''        [1] - EXERCICÍOS DE PORTUGUÊS
        [2] - EXERCÍCIOS DE MATEMÁTICA
        [3] - EXERCÍCIOS DE GEOGRÁFIA
        [4] - SAIR DO PROGRAMA''')
#playsound.playsound('kid_francescoli_moon_-6694487603817081186.mp3')
opcao = int(input(' Digite a opção que deseja:'))
conta = conte = 0
n1 = 0
n2 = 0
if opcao == 1:
    print('\033[1;93mBEM VINDO A AULA DE PORTUGUÊS !\33[m')
    sleep(2)
    print('\033[1;35mOBJETIVO:\33[m ADIVINHE SE A PALABRA SORTEADA TEM "S", "SS"')
    sleep(2)
elif opcao == 2:
    print('\033[1;93m BEM VINDO A AULA DE MATEMÁTICA !\33[m')
    sleep(2)
    print('\033[1;35mOBJETIVO:\33[m FAÇA AS CONTAS A SEGUIR.')
    sleep(2)
elif opcao == 3:
    print('BEM VINDO A AULA DE GEOGRÁFIA')

elif opcao == 4:
    print('SAINDO DO PROGRAMA')
    sleep(3)

while opcao != 4:
    if opcao == 1:
        palavra = random.choice(
            [ 'ânsia', 'ansiar', 'ansioso', 'ansiedade', 'cansar', 'cansado',
             'descansar', 'descanso',
             'diversão', 'excursão', 'farsa', 'ganso', 'hortênsia', 'pretensão', 'pretensioso',
             'propensão', 'remorso', 'sebo', 'tenso', 'utensílio', 'acesso', 'acessório', 'acessível',
             'assar', 'asseio', 'assinar',
             'carrossel', 'cassino', 'concessão', 'discussão', 'escassez', 'escasso', 'essencial',
             'expressão', 'fracasso', 'impressão', 'massa',
             'massagista', 'missão', 'necessário', 'obsessão', 'opressão', 'pêssego', 'procissão',
             'profissão', 'ressurreição', 'sessenta',
             'sossegar', 'sossego', 'submissão', 'sucessivo']).strip().upper()
        if 'S' in palavra:
            sems = palavra.replace("S", "")
        elif 'SS' in palavra:
            sems = palavra.replace("SS", "")
        #elif 'C' in palavra:
            #sems = palavra.replace("C", "")
       #elif 'Ç' in palavra:
           # sems =palavra.replace("Ç", "")

        print(f'A PALABRA SORTEADA É: {sems}')
        resp = str(input('DIGITE A PALAVRA CORRETA AQUI: ')).strip().upper()

        if resp == palavra:
            print('\033[1;92mVOCÊ ACERTOU\33[m')
            conta += 1
        else:
            print('\033[;31mVOCÊ ERROU! \33[m')
            print(f'A palavra correta é:\033[1;35m {palavra}\33[m')
            conte += 1

            pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
            if pergunta in 'Nn':
                print(f'\033[;1mRESULTADO: ACERTOS = {conta} e ERROS= {conte}\33[m')
                break

    elif opcao == 2:
        n1 = randint(0, 20)
        n2 = randint(0, 20)
        escolha = random.choice(['SOMA', 'SUBTRAÇÃO','MULTIPLICAÇÃO'])
        sleep(2)
        print(f' === \033[;1mO COMPUTADOR ESCOLHEU 2 NUMEROS ->:\33[m', end=' ')
        sleep(1)
        print(f'\033[1;91m{n1}\33[m', end=' ')
        sleep(1)
        print( ' E ', end=' ')
        sleep(1)
        print(f'\033[1;91m{n2}\33[m')
        result = float(input(f'Qual o resultado da \033[;1m{escolha}\33[m entre eles: '))
        soma = n1 + n2
        subi = n1 - n2
        #divi = n1 / n2
        mult = n1 * n2

        if result == soma or result == subi or result == mult:
            print('\033[1;92mVOCÊ ACERTOU\33[m')
            conta += 1
        else:
            print('\033[;31mVOCÊ ERROU! \33[m')
            print(f'O resultado correto é: {"Soma: ", soma, "Subitração: ", subi, "Multiplicação: ", mult}')
            conte += 1

        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if pergunta in 'Nn':
            print(f'\033[;1mRESULTADO: ACERTOS = {conta} e ERROS= {conte}\33[m')
            break

