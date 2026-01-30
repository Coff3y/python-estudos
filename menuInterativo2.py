import json

ARQUIVO = "usuariosJSON.json"

def pedir_usuario():
        while True:
                nome = input("Qual o seu nome?\n").strip()
                if nome:
                        return nome
                else:
                        print("Insira um nome válido...\n")
                        continue
                
def pedir_idade():
        while True:
                
            idade = input("Qual a sua idade?\n").strip()

            if not idade:
                        print("Insira um digito válido...\n")
                        continue
            try:
                    idade = int(idade)
                    if idade <= 0:
                            print("Idade Inválida.\n")
                            continue
                    return idade
                
            except ValueError:
                    print("Digite apenas números.\n")        


def carregar_usuarios():
        try:
                with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                    return json.load(arquivo)
        except FileNotFoundError:
                return []

def salvar_usuarios(usuarios):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

def adicionar_usuarios(nome, idade):
        usuarios = carregar_usuarios()

        usuarios.append({
            "nome": nome,
            "idade": idade})
            
        salvar_usuarios(usuarios)
        print("\nUsuário salvo com sucesso!\n")


def listar_usuarios():
        usuarios = carregar_usuarios()

        if not usuarios:
                print("\n Nenhum usuário cadastrado...\n")
                return
        print("------ Usuários Cadastrados ------")
        for user in usuarios:
                print(f"Nome: {user['nome']} | Idade: {user['idade']}")
        print("----------------------------------")

def menu():
    print("\n====== MENU ======")
    print("1. Cadastrar novo usuário.")
    print("2. Listar usuários.")
    print("3. Sair.")
            
def main():
       while True:
            
            menu()
            
            opcao = input("Pressione o número referente a opção desejada...\n").strip()
            
            if opcao == "1":
                   nome = pedir_usuario()
                   idade = pedir_idade()
                   adicionar_usuarios(nome, idade)
            
            if opcao == "2":
                   listar_usuarios()
            
            if opcao == "3":
                   print("Até mais! 👋")
                   break

            else:
                   print("\nOpção inválida.\n")

if __name__ == "__main__":
       main()