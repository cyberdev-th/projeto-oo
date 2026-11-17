"""Classe Usuário: representa um usuário da biblioteca."""

from biblioteca.livro import Livro

class Usuario:
    """Um usuário com nome, id e lista de livros emprestados."""

    LIMITE_LIVROS = 3

    def __init__(self, nome: str, id: str):
        self._nome = nome
        self._id = id
        self._livros_emprestados: list[Livro] = []

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def id(self) -> str:
        return self._id

    @property
    def livros_emprestados(self) -> list[Livro]:
        return list(self._livros_emprestados)

    def pode_emprestar(self) -> bool:
        """Verifica se o usuário ainda pode pegar mais livros."""
        return len(self._livros_emprestados) < self.LIMITE_LIVROS

    def adicionar_livro(self, livro: Livro) -> bool:
        """Tenta adicionar um livro. True se conseguiu, False se já está no limite."""
        if not self.pode_emprestar():
            return False
        self._livros_emprestados.append(livro)
        return True

    def remover_livro(self, livro: Livro) -> bool:
        """Remove o livro da lista. False se ele não estava lá."""
        if livro not in self._livros_emprestados:
            return False
        self._livros_emprestados.remove(livro)
        return True

    def __str__(self) -> str:
        qtd = len(self._livros_emprestados)
        return f"{self._nome} (id={self._id}) - {qtd} livro(s)"

    def __repr__(self) -> str:
        return f"Usuario({self._nome!r}, {self._id!r})"



if __name__ == "__main__":
    print("=== Teste rápido da classe Usuario ===")
    u = Usuario("Ana", "1")
    print(u)
    print(f"Pode emprestar? {u.pode_emprestar()}")

    l1 = Livro("Dom Casmurro", "Machado", "111")
    l2 = Livro("Memórias Póstumas", "Machado", "222")
    l3 = Livro("Grande Sertão", "Rosa", "333")
    l4 = Livro("Sagarana", "Rosa", "444")

    print(f"Adiciona l1: {u.adicionar_livro(l1)}")
    print(f"Adiciona l2: {u.adicionar_livro(l2)}")
    print(f"Adiciona l3: {u.adicionar_livro(l3)}")
    print(f"Adiciona l4 (deve falhar): {u.adicionar_livro(l4)}")

    print(u)
    print(f"Pode emprestar? {u.pode_emprestar()} (esperado: False)")

    print(f"Remove l1: {u.remover_livro(l1)}")
    print(f"Remove l1 de novo: {u.remover_livro(l1)} (esperado: False)")
    print(f"Pode emprestar? {u.pode_emprestar()} (esperado: True)")

    # Teste de cópia defensiva
    qtd_antes = len(u.livros_emprestados)
    u.livros_emprestados.append("hack")
    qtd_depois = len(u.livros_emprestados)
    print(f"Cópia defensiva: antes={qtd_antes}, depois={qtd_depois} (esperado: iguais)")