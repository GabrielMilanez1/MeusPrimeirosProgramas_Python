def play():
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
if __name__ == '__main__':
    play()