def contador_play():
    #******************************************************
    contarNovamente = 1
    while contarNovamente == 1:
        numeroPedidoAll = input('\nEscreva a quantidade de palavras/frases para a contagem de caracteres: ')
        while type(numeroPedidoAll) != int:
            if numeroPedidoAll.isdigit() == True:
                numeroPedido = int(numeroPedidoAll)
                break
            else:
                numeroPedidoAll = input('\nVocê deve inserir um número!. Escreva novamente: ')
        #******************************************************
        contador = 0
        lista_palavras = []
        while contador < numeroPedido:
            contadorDeLetras = input('Escreva a palavra/frase (cuidado com os espaços em branco, eles também são contados!): ')
            contador = contador + 1
            lista_palavras.append(contadorDeLetras)
        print('\n')
        #******************************************************
        tuplaLista = tuple(lista_palavras)
        looping = 0
        for n in range(numeroPedido + 1):
            if numeroPedido != 0:
                print('A palavra/frase "{}" possui "{}" caracteres.'.format(tuplaLista[n].strip(), len(tuplaLista[n].strip())))
                print('*******************************************')
                looping = looping + 1
                if looping == numeroPedido:
                    break
            else:
                print('Não é possível fazer a contagem caso a quantidade de palavras/frases for igual a "0".')
        #******************************************************
        perguntaQuerAll = str(input('\n\nDeseja medir novamente? (1 para sim e 0 para não): '))
        while type(perguntaQuerAll) != int:
            if perguntaQuerAll.isdigit() == True and perguntaQuerAll == '0' or perguntaQuerAll == '1':
                perguntaQuer = int(perguntaQuerAll)
                break           
            else:
                perguntaQuerAll = input('\nVocê deve inserir apenas "0" ou "1". Escreva novamente: ')
        if perguntaQuer == 0:
            print('\n\n\n')
            print('*******************************************')
            print('*************Fim de operação!!*************')
            print('*******************************************')
            contarNovamente = contarNovamente - 1
        #****************************************************** 

def jogo_play():
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

def forca_play():
    jogarNovamente = 1
    while jogarNovamente == 1:
        palavra_secreta_lista = []
        palavra_secreta = input('Escreva a palavra para o jogo da forca!: ')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        for letras in palavra_secreta:
            palavra_secreta_lista.append('_')

        forca = False
        vitoria = False
        chutes = 5
        print('A palavra secreta possui {} letras. {}\n'.format(len(palavra_secreta_lista), palavra_secreta_lista))

        while not forca and not vitoria:
            chute = input('Escreva a letra que é o seu chute: ')
            if chute.strip().upper() in palavra_secreta.strip().upper():
                contador = 0
                for letras in palavra_secreta:
                    if chute.strip().upper() == letras.strip().upper():
                        palavra_secreta_lista[contador] = chute.strip().upper()
                    contador += 1
                print(palavra_secreta_lista)    
            else:
                print('A letra "{}" não está na palavra. Tentativa {}/{}'.format(chute, chutes, '6'))
                chutes -= 1
        
            forca = chutes == -1
            vitoria = '_' not in palavra_secreta_lista

            if vitoria:
                print('Você ganhou!!!!')
                break
            if forca:
                print('Você perdeu! A palavra secreta era: {}'.format(palavra_secreta))
                break
        perguntaQuerAll = str(input('Deseja jogar novamente? (1) para sim ou (0) para não: '))
        while type(perguntaQuerAll) != int:
            if perguntaQuerAll.isdigit() == True and perguntaQuerAll == '0' or perguntaQuerAll == '1':
                perguntaQuer = int(perguntaQuerAll)
                break           
            else:
                perguntaQuerAll = input('\nVocê deve inserir apenas "0" ou "1". Escreva novamente: ')
        if perguntaQuer == 0:
            jogarNovamente -= 1
def calculadora_play():
    repetir = 1
    while repetir == 1:
        perguntaOp = str(input('Insira a operação que deseja fazer!\n(+) para soma\n(-) para subtração\n(*) para multiplicação\n(%) para divisão\nEscreva aqui: '))
        if perguntaOp != "+" and perguntaOp != "-" and perguntaOp != "*" and perguntaOp != "%":
            while perguntaOp != "+" or perguntaOp != "-" or perguntaOp != "*" or perguntaOp != "%":
                perguntaOp = str(input('Você deve inserir apenas "(+), (-), (*) ou (%). Escreva novamente: '))
                if perguntaOp == "+" or perguntaOp == "-" or perguntaOp == "*" or perguntaOp == "%":
                    break

        resultado = 0

        perguntaVezesAll = str(input('Quantos números diferentes para a operação? Escreva aqui: '))
        while type(perguntaVezesAll) != int:
            if perguntaVezesAll.isdigit() == True and perguntaVezesAll != '0' and perguntaVezesAll != '1':
                perguntaVezes = int(perguntaVezesAll)
                break
            else:
                perguntaVezesAll = str(input('Você deve inserir um número e que seja maior que 1!\nEscreva novamente: '))


        for n in range(perguntaVezes):
            perguntaNumeroAll = str(input('Insira o número: '))
            while type(perguntaNumeroAll) != int:
                if perguntaNumeroAll.isdigit() == True:
                    perguntaNumero = int(perguntaNumeroAll)
                    break
                else:
                    perguntaNumeroAll = str(input('Você deve inserir um número!\nEscreva novamente: '))

            if perguntaOp == '+':
                if n == 0:
                    resultado = perguntaNumero
                if n != 0:
                    resultado += perguntaNumero
            if perguntaOp == '-':
                if n == 0:
                    resultado = perguntaNumero
                if n != 0:
                    resultado -= perguntaNumero
            if perguntaOp == '*':
                if n == 0:
                    resultado = perguntaNumero
                if n != 0:
                    resultado *= perguntaNumero
            if perguntaOp == '%':
                if n == 0:
                    resultado = perguntaNumero
                if n != 0:
                    resultado /= perguntaNumero

        print('O resultado da sua operação foi de: {r}!'.format(r = resultado))

        perguntaNovamenteAll = str(input('Deseja fazer uma nova operação? Insira (1) para sim ou (0) para não: '))
        while type(perguntaNovamenteAll) != int:
            if perguntaNovamenteAll.isdigit() == True and perguntaNovamenteAll == '0' or perguntaNovamenteAll == '1':
                perguntaNovamente = int(perguntaNovamenteAll)
                break
            else:
                perguntaNovamenteAll = str(input('Você deve inserir apenas (0) ou (1)!\nEscreva novamente: '))
        if perguntaNovamente == 0:
            print('\n\n\n')
            print('*******************************************')
            print('*************Fim de operação!!*************')
            print('*******************************************')
            repetir -= 1

print('******************************************')
print('*******Bem-vindo ao meu programa!!********')
print('******************************************')
começar = 1
while começar == 1:
    escolhaAll = str(input('\n\nEscolha um número!\n(1) para "Contador de letras"\n(2) para "Joguinho advinhe o número"\n(3) para "Jogar forca"\n(4) para "Calculadora"\n(5) para "Sair"\nEscreva aqui: '))
    while escolhaAll != int:
        if escolhaAll.isdigit == True or escolhaAll == '1' or escolhaAll == '2' or escolhaAll == '3' or escolhaAll == '4' or escolhaAll == '5':
            escolha = int(escolhaAll)
            break
        else:
            escolhaAll = str(input('\nVocê deve escolher apenas (1), (2), (3), (4) e (5)\nEscreva novamente: '))
    if escolha == 1:
        print('\nVocê escolheu "Contador de letras"\n')
        contador_play()
    elif escolha == 2:
        print('\nVocê escolheu "Joguinho advinhe o número"\n')
        jogo_play()
    elif escolha == 3:
        print('\nVocê escolheu "Jogar forca"\n')
        forca_play()
    elif escolha == 4:
        print('\nVoê escolheu "Calculadora"\n')
        calculadora_play()
    elif escolha == 5:
        print('\nVocê escolheu "Sair"\n')
        print('\n\n********************')
        print('*******Fim!!********')
        print('********************')
        print('\n\n\nPrograma feito por Gabriel Milanez!')
        começar = começar - 1