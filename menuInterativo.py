ARQUIVO = "usuarios.txt"


def pedir_nome():
    while True:
        nome = input("Qual o seu nome?\n").strip()
        if nome: #por que não usar o if not??
            return nome
        print("Nome inválido...\n")


def pedir_idade():
    while True:
        idade = input("Qual sua idade?\n").strip()
        if not idade:
            print("Digite um único valor válido")
            continue

        try:
            idade = int(idade)
            if idade <= 0:
                print("Sua idade com certeza não é negativa, tente novamente\n")
                continue
            else:
                return idade
        except ValueError:
            print("Digite apenas um número")


def salvar_usuario(nome, idade):
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{idade}\n")
    print("\nUsuário salvo com sucesso!\n")


def listar_usuarios():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            print("\n---- Usuários cadastrados ----")
            for lista in arquivo:
                nome, idade = lista.strip().split(",")
                print(f"Nome: {nome} | Idade: {idade}")
            print("-------------------------------\n")
    except FileNotFoundError:
        print("Nenhum usuário encontrado...\n")            


def menu():
    print("====== MENU =====")
    print("1 - Cadastrar novo usuário.")
    print("2 - Listar usuários.")
    print("3 - Sair.")


def cadastrar_usuario():
    nome = pedir_nome()
    idade = pedir_idade()
    salvar_usuario(nome, idade)

def main():
    while True:
        menu()
        opcao = input("\n Selecione uma opção...\n")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            listar_usuarios()

        else:
            print("Compreendo, até logo!....")
            break

if __name__ == "__main__":
    main()


