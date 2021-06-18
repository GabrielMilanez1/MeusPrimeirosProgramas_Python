def play():
    print('********************************************************************************************************************')
    print('*****************************************Bem-vindo ao "joguinhoAdivinha"!!!*****************************************')
    print('********************************************************************************************************************') 

    contador = 1
    while contador == 1:

        import random
        numeroSorteado = round(random.random() * 10)
        numeroPensadoAll = str(input('\n\nQual número de 0 a 10 eu pensei? Tente advinhar!: '))
        while type(numeroPensadoAll) != int:
                if numeroPensadoAll.isdigit() == True and numeroPensadoAll == '0' or numeroPensadoAll == '1' or numeroPensadoAll == '2' or numeroPensadoAll == '3' or numeroPensadoAll == '4' or numeroPensadoAll == '5' or numeroPensadoAll == '6' or numeroPensadoAll == '7' or numeroPensadoAll == '8' or numeroPensadoAll == '9' or numeroPensadoAll == '10':
                    numeroPensado = int(numeroPensadoAll)
                    break
                else:
                    numeroPensadoAll = input('\nVocê deve digitar um número de 0 a 10. Tente novamente: ')
        while numeroPensado >= 11 or numeroPensado <= -1:
            numeroPensado = int(input('\nVocê deve inserir um número de 0 a 10. Tente novamente: '))
            if numeroPensado < 11 and numeroPensado > -1:
                break
            
        if numeroPensado == numeroSorteado:
            print('\nVocê acertou amigo, parabéns!')
        else:
            print('\nVocê errou amigo, o numéro que eu pensei era o: {}'.format(numeroSorteado))

        aAll = str(input('\nDeseja jogar novamente? Digite "1" para sim, ou "0" para não: '))
        while type(aAll) != int:
            if aAll.isdigit() == True and aAll == '0' or aAll == '1':
                a = int(aAll)
                break
            else:
                aAll = input('\nVocê deve inserir apenas "0" ou "1".\nEscreva novamente: ')
        if a == 0:
            contador - 1
            print('\n\nFim de jogo!!')
            break
if __name__ == '__main__':
    play()