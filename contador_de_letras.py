def play():
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
if __name__ == '__main__':
    play()