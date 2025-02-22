import os

palavra = 'paralelepipedo'
letras_acertadas = ''
tentativa = 0
acertou = 0

while True:

    letra = input('Digite uma letra: ').lower()

    # .lower() transforma a entrada de dados (input) em minusculo.

    if len(letra) > 1:
        print('digite apenas uma letra!')

        # aqui verifica se o usuario colocou apenas uma letra na entrada.

        continue

    if letra in letras_acertadas:
        print('Você ja tentou essa letra, informe outra letra!')

        # aqui faz a analise se a letra esta sendo repetida.

        continue

    if letra in palavra:
        letras_acertadas += letra

        # letras_acertadas recebe todas as letras que ja foram tentadas ou acertadas, assim nao havendo chance
        # de repetir a letra para que nao haja erros.

        tentativa += 1
    
    palavra_formada = ''

    # cria uma nova variavel (palavra_formada) para comportar o resultado da palavra secreta.
    
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

            # aqui faz a junção se acertou a letra ou não trocando os caracteres por * (errou) ou a letra acertada indicando que acertou.

    if palavra_formada == palavra:
        os.system('cls')

        # esse os.system('cls') ele da um clear no terminal assim que passar do if.

        print(f'Você ACERTOU!!! a palavra era {palavra} voce tentou {tentativa}x')
        letras_acertadas = ''
        tentativa = 0
        if tentativa == len(palavra):
            print('Parabens você não errou nenhuma letra!')
        break
    
    print(palavra_formada)
