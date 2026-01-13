livros = []
usuarios = []

# ---------- Gerenciamento de Livros ----------

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

# ---------- Gerenciamento de Usuários ----------

def registrar_usuario(nome):
    usuarios.append({
        "nome": nome,
        "livros_emprestados": []
    })