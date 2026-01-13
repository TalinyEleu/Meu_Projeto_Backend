
livros = []
usuarios = []

# Gerenciamento de Livros

def adicionar_livro(titulo, autor):
    livros.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })

def remover_livro(titulo):
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)
            return True
    return False

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    for livro in livros:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'{livro["titulo"]} - {livro["autor"]} | {status}')

# Gerenciamento de Usuários

def registrar_usuario(nome):
    usuarios.append({
        "nome": nome,
        "livros_emprestados": []
    })

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for usuario in usuarios:
        print(f'Nome: {usuario["nome"]} | Livros: {usuario["livros_emprestados"]}')

# Empréstimos

def emprestar_livro(titulo, nome_usuario):
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower() and livro["disponivel"]:
            for usuario in usuarios:
                if usuario["nome"].lower() == nome_usuario.lower():
                    livro["disponivel"] = False
                    usuario["livros_emprestados"].append(titulo)
                    return True
    return False
    
def consultar_disponibilidade():
    print("\nLivros disponíveis:")
    for livro in livros:
        if livro["disponivel"]:
            print(livro["titulo"])

    print("\nLivros emprestados:")
    for livro in livros:
        if not livro["disponivel"]:
            print(livro["titulo"])

# Menu Principal

def menu():
    while True:
        print("\n===== MENU BIBLIOTECA =====")
        print("1 - Adicionar livro")
        print("2 - Remover livro")
        print("3 - Listar livros")
        print("4 - Registrar usuário")
        print("5 - Registrar empréstimo")
        print("6 - Consultar disponibilidade")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                adicionar_livro(titulo, autor)
                print("Livro adicionado com sucesso!")
            elif opcao == "2":
                titulo = input("Título do livro a remover: ")
                if remover_livro(titulo):
                    print("Livro removido com sucesso!")
                else:
                    print("Livro não encontrado.")

            elif opcao == "3":
                listar_livros()

            elif opcao == "4":
                nome = input("Nome do usuário: ")
                registrar_usuario(nome)
                print("Usuário registrado com sucesso!")

            elif opcao == "5":
                titulo = input("Título do livro: ")
                nome = input("Nome do usuário: ")
                if emprestar_livro(titulo, nome):
                    print("Empréstimo realizado com sucesso!")
                else:
                    print("Erro ao realizar empréstimo.")

            elif opcao == "6":
                consultar_disponibilidade()

            elif opcao == "0":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    menu()