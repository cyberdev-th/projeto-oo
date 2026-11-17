"""Classe Livro: representa um livro do acervo."""

class Livro:
    """Um livro com título, autor, ISBN e disponibilidade."""

    def __init__(self, titulo: str, autor: str, isbn: str):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponivel = True

    def emprestar(self) -> bool:
        """Marca como emprestado. True se conseguiu, False se já estava emprestado."""
        if not self._disponivel:
            return False
        self._disponivel = False
        return True

    def devolver(self) -> bool:
        """Marca como disponível. True se conseguiu, False já estava disponível."""
        if self._disponivel:
            return False
        self._disponivel = True
        return True

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def autor(self) -> str:
        return self._autor

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    def __str__(self) -> str:
        status = "disponível" if self._disponivel else "indisponível"
        return f"{self._titulo} - {self._autor} [{status}]"

    def __repr__(self) -> str:
        return f"Livro({self._titulo!r}, {self._autor!r}, {self._isbn!r})"


if __name__ == "__main__":
    print("=== Teste rápido da classe Livro ===")
    l = Livro("Dom Casmurro", "Machado de Assis", "978-852221000")
    print(l)
    print(f"Emprestar: {l.emprestar()}")
    print(l)
    print(f"Emprestar de novo: {l.emprestar()}")
    print(f"Devolver: {l.devolver()}")
    print(f"Devolver de novo: {l.devolver()}")
    print(f"repr: {l!r}")