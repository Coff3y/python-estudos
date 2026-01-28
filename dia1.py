def pedir_usuario():
    nome = input("Qual o seu nome?\n").strip()

    while not nome:
        nome = input("Insira um nome válido.\n").strip()
    return nome

def pedir_idade():
    while True:
        idade = input("Qual sua idade?\n").strip()
        
        if not idade:
            print("Tente um número válido.")
            continue

        try:
            idade = int(idade)
            return idade
        except ValueError:
            print("Por favor, apenas um número.\n")

def main():
    username = pedir_usuario()
    age = pedir_idade()
    print(f"Seja bem-vindo {username}!")
    if age <= 5:
        print(f"Acho que {age} anos é muito pouco para alguém saber ler e escrever. Mas tudo bem né...")
    elif age >= 50:
        print(f"Alguém com {age} anos não está velho demais para isso?")
    else:
        print(f"Então você tem {age}, muito legal!")

if __name__ == "__main__":
    main()