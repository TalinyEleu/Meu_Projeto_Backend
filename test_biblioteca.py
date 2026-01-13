# Teste
from biblioteca import adicionar_livro, livros

def test_adicionar_livro():
    livros.clear()
    adicionar_livro("1984", "George Orwell")
    assert len(livros) == 1
    assert livros[0]["titulo"] == "1984"
    assert livros[0]["disponivel"] is True