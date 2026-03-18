def menu():
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

def cadastrar():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{idade}\n")

    print("Usuário cadastrado com sucesso!")

def listar():
    try:
        with open("usuarios.txt", "r") as arquivo:
            usuarios = arquivo.readlines()

            if not usuarios:
                print("Nenhum usuário cadastrado.")
                return

            print("\n=== USUÁRIOS ===")
            for usuario in usuarios:
                nome, idade = usuario.strip().split(",")
                print(f"Nome: {nome} | Idade: {idade}")

    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")