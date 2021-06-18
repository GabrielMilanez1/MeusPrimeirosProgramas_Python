def play():
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

if __name__ == '__main__':
    play()