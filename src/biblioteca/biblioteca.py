"""Classe Biblioteca: orquestra livros, usuários e empréstimos."""

from biblioteca.livro import Livro
from biblioteca.usuario import Usuario
from biblioteca.emprestimo import Emprestimo

class Biblioteca:
    """Uma biblioteca com acervo, usuários e histórico de empréstimos."""

    def __init__(self, nome: str):
        self._nome = nome
        self._livros: list[Livro] = []
        self._usuarios: list[Usuario] = []
        self._emprestimos: list[Emprestimo] = []

    @property
    def nome(self) -> str:
        return self._nome

    #------------------ Cadastros -----------------------

    def adicionar_livro(self, livro: Livro) -> bool:
        """Adiciona ao acervo. False se ISBN já existe."""
        if self.buscar_livro(livro.isbn):
            return False
        self._livros.append(livro)
        return True

    def cadastrar_usuario(self, usuario: Usuario) -> bool:
        """Cadastra usuário. False se id já existe."""
        if self.buscar_usuario(usuario.id):
            return False
        self._usuarios.append(usuario)
        return True

    # ------------- Buscas -----------------------

    def buscar_livro(self, isbn: str) -> Livro | None:
        """Retorna o livro com esse Isbn, ou None"""
        for livro in self._livros:
            if livro.isbn == isbn:
                return livro
        return None

    def buscar_usuario(self, id_usuario: str) -> Usuario | None:
        """Retorna o usuário com esse id, ou None."""
        for usuario in self._usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None

    # ------------------ Regras de negócio ----------------------

    def emprestar(self, livro: Livro, usuario: Usuario) -> Emprestimo | None:
        """Tenta emprestar. Retorna Emprestimo criado ou None se falhou."""
        livro_no_acervo = self.buscar_livro(livro.isbn)
        if livro_no_acervo is None:
            return None
        usuario_cadastrado = self.buscar_usuario(usuario.id)
        if usuario_cadastrado is None:
            return None
        if not livro_no_acervo.disponivel:
            return None
        if not usuario_cadastrado.pode_emprestar():
            return None

        livro_no_acervo.emprestar()
        usuario_cadastrado.adicionar_livro(livro_no_acervo)
        emprestimo = Emprestimo(livro_no_acervo, usuario_cadastrado)
        self._emprestimos.append(emprestimo)
        return emprestimo

    def devolver(self, emprestimo: Emprestimo) -> float | None:
        """
        Registra devolução. Retorna a multa (float) se deu certo,
        ou None se o empréstimo não pertence a esta biblioteca ou já foi devolvido.
        """

        if emprestimo not in self._emprestimos:
            return None
        if not emprestimo.ativo:
            return None

        multa = emprestimo.multa
        emprestimo.livro.devolver()
        emprestimo.usuario.remover_livro(emprestimo.livro)
        emprestimo.registrar_devolucao()
        return multa

    # --------------- Consultas -------------------------

    def emprestimos_ativos(self) -> list[Emprestimo]:
        """Lista só os empréstimos ainda não devolvidos."""
        return [e for e in self._emprestimos if e.ativo]

    def livros_em_atraso(self) -> list[Emprestimo]:
        """Lista empréstimos ativos com atraso > o dias."""
        return [e for e in self._emprestimos if e.ativo and e.dias_atraso > 0]

    def __str__(self) -> str:
        return (
            f'Biblioteca "{self.nome}" - '
            f"{len(self._livros)} livro(s), "
            f"{len(self._usuarios)} usuário(s), "
            f"{len(self.emprestimos_ativos())} empréstimo(s) ativo(s)"
        )

    def __repr__(self) -> str:
        return f"Biblioteca({self._nome!r})"


if __name__ == "__main__":
    print("=== Teste rápido da classe Biblioteca ===")

    biblio = Biblioteca("Central")
    l1 = Livro("Dom Casmurro", "Machado", "111")
    l2 = Livro("Memórias Póstumas", "Machado", "222")
    u1 = Usuario("Ana", "1")
    u2 = Usuario("Bia", "2")

    print(f"Adiciona l1: {biblio.adicionar_livro(l1)}")
    print(f"Adiciona l2: {biblio.adicionar_livro(l2)}")
    print(f"Adiciona l1 de novo: {biblio.adicionar_livro(l1)} (esperado: False)")
    print(f"Cadastra u1: {biblio.cadastrar_usuario(u1)}")
    print(f"Cadastra u2: {biblio.cadastrar_usuario(u2)}")
    print(biblio)

    print("\n--- Empréstimo ---")
    e1 = biblio.emprestar(l1, u1)
    print(f"Ana pega l1: {'sim' if e1 else 'não'}")
    print(f"l1 disponível? {l1.disponivel} (esperado: False)")

    e2 = biblio.emprestar(l1, u2)
    print(f"Bia tenta l1 (já emprestado): {'sim' if e2 else 'não'} (esperado: não)")

    print("\n--- Devolução ---")
    multa = biblio.devolver(e1)
    print(f"Devolução: multa = R$ {multa:.2f}")
    print(f"l1 disponível? {l1.disponivel} (esperado: True)")

    multa2 = biblio.devolver(e1)
    print(f"Devolve de novo: {multa2} (esperado: None)")
    print(biblio)