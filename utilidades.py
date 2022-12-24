from required import *

#start
def abertura():
    os.system('cls')
    print(start[1])
    enter = input("***De um Enter pra iniciarmos.***")
    print(f'{enter}\n: ')

    if enter == '':
        os.system('cls')
        options()
    else:
        os.system('cls')
        exit()

#exit
def exit():
    time.sleep(1)
    print('\nObrigado por jogar!')
    os.system('cls')

#options
def options():
    print(select_options[1])
    label = int(input("[1]INICIAR JOGO\n[2]SOBRE\n: "))
    print(label)

    if label == 1:
        game()
    elif label == 2:
        about()
    else:
        time.sleep(2)
        os.system('cls')
        options()

#about
def about():
    os.system('cls')
    print(about_strings[1])
    enter = input("***De um Enter pra voltar a tela inicial.***")
    print(f'{enter}\n: ')

    if enter == '':
        abertura()
    else:
        exit()

#função pra quando o jogador ganhar
def ganho():
    os.system('cls')
    print(sucess[1])

    try:
        print("Deseja jogar novamente?(S/N)")
        resposta = input(': ').lower().strip()[0]
            
        if resposta == 's':
            print(load[1])
            time.sleep(10)
            os.system('cls')
            abertura()
        elif resposta == 'n':
            exit()
    except ValueError:
            print(required_select[1])
            time.sleep(5)
            os.system('cls')

#função pra quando o jogador perde
def morto():
    os.system('cls')
    print(dead[1])
    print(f"A palavra correta era: {aleatorizar(palavras)}")

    print("Deseja jogar novamente?(S/N)")
    resposta = input(': ').lower().strip()[0]
            
    if resposta == 's':
        print(load[1])
        time.sleep(5)
        os.system('cls')
        abertura()
    elif resposta == 'n':
        exit()
    else :
        print(required_select[1])
        time.sleep(5)
        os.system('cls')

#function that generates the word
def aleatorizar(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    return palavra.upper()

def game():
    os.system('cls')
    palavra = aleatorizar(palavras)
    letras_palavras = set(palavras)
    alfabeto = set(string.ascii_uppercase)
    letras_usada = set() 

    lives = 7
    while len(letras_palavras) > 0 and lives > 0:
        print('Você tem', lives, 'vidas restantes e você usou essas letras: ', ' '.join(letras_usada))

        word_list = [letter if letter in letras_usada else '-' for letter in palavra]
        print('Palavras usada: ', ' '.join(word_list))

        letra_usuario = input('Adivinhe uma letra: ').upper()
        if letra_usuario in alfabeto - letras_usada:
            letras_usada.add(letra_usuario)
            if letra_usuario in letras_palavras:
                letras_palavras.remove(letra_usuario)
                print('')

            else:
                lives = lives - 1
                print('\nSua letra,', letra_usuario, 'não está na palavra.')

        elif letra_usuario in letras_usada:
            print('\nVocê já usou essa letra. tente outra letra.')

        else:
            print('\nEssa não é uma letra válida.')

    if lives == 0:
        morto()
    else:
        ganho()