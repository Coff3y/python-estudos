def pedir_nome():

    name = input("Qual o seu nome?\n").strip()
    if not name:
        name = input("Um espaço vazio não é um nome... Tente novamente\n").strip()
    return name

def pedir_idade():
    while True: 
        age = input("Qual a sua idade?\n").strip()
        if not age:
            print("Um espaço vazio não é considerado um valor... Tente novamente.\n")
            continue
        try:
            age = int(age)
            if not age > 0:
                print("Tente um número positivo")
                continue
            return age
        except ValueError:
            print("Digite apenas um número.")

def main():
    nome = pedir_nome()
    idade = pedir_idade()

    if idade <= 6:
        print(f"Uau! Com {idade} anos saber ler e escrever é de fato impressionante {nome}!")

    elif idade >= 60:
        print(f"Hmmmm, eu diria que ter {idade} anos de idade e ainda brincar com isso é meio que falta do que fazer não acha {nome}?")
    
    else:
        print(f"Bacana! Prazer em conhece-lo {nome}, lembro-me bem quando eu tinha {idade} anos também... Já faz bastante tempo ;(")


if __name__ == "__main__":
    main()