"""Classe Emprestimo: liga um Livro a um Usuario com datas e multas."""

from datetime import datetime, timedelta

from biblioteca.livro import Livro
from biblioteca.usuario import Usuario

class Emprestimo:
    """Um empréstimo de livro para usuário, com prazo e multa."""

    PRAZO_DIAS = 14
    VALOR_MULTA_POR_DIA = 2.50

    def __init__(self, livro: Livro, usuario: Usuario):
        self._livro = livro
        self._usuario = usuario
        self._data_emprestimo = datetime.now()
        self._data_devolucao: datetime | None = None

    @property
    def livro(self) -> Livro:
        return self._livro

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @property
    def ativo(self) -> bool:
        """True enquanto não foi devolvido."""
        return self._data_devolucao is None

    @property
    def data_limite(self) -> datetime:
        """Data máxima para devolver sem multa."""
        return self._data_emprestimo + timedelta(days=self.PRAZO_DIAS)

    @property
    def dias_atraso(self) -> int:
        """Dias de atraso(0 se estiver no prazo.)"""
        if self.ativo:
            referencia = datetime.now()
        else:
            referencia = self._data_devolucao
        diferenca = referencia - self.data_limite
        return max(0, diferenca.days)

    @property
    def multa(self) -> float:
        """Valor da multa em reais(dia_atraso * valor_por_dia)"""
        return round(self.dias_atraso * self.VALOR_MULTA_POR_DIA, 2)

    def registrar_devolucao(self) -> bool:
        """Marca como devolvido. False se já foi devolvido."""
        if not self.ativo:
            return False
        self._data_devolucao = datetime.now()
        return True

    def __str__(self) -> str:
        data = self._data_emprestimo.strftime("%d/%m/%Y")
        status = "ativo" if self.ativo else "devolvido"
        return f"Empréstimo: {self._livro.titulo} para {self._usuario.nome} em {data} [{status}]"

    def __repr__(self) -> str:
        return f"Emprestimo({self._livro!r}, {self._usuario!r})"


if __name__ == "__main__":
    print("=== Teste rápido da classe Emprestimo ===")
    l = Livro("Dom Casmurro", "Machado", "111")
    u = Usuario("Ana", "1")
    e = Emprestimo(l, u)

    print(e)
    print(f"Ativo? {e.ativo}")
    print(f"Data limite: {e.data_limite.strftime('%d/%m/%Y')}")
    print(f"Dias de atraso: {e.dias_atraso}")
    print(f"Multa: R$ {e.multa:.2f}")

    print(f"Registra devolução: {e.registrar_devolucao()}")
    print(f"Registra de novo: {e.registrar_devolucao()} (esperado: False)")
    print(f"Ativo? {e.ativo} (esperado: False)")

    # Simula atraso: empréstimo há 20 dias (prazo 14 → 6 dias de atraso)
    e2 = Emprestimo(l, u)
    e2._data_emprestimo = datetime.now() - timedelta(days=20)
    print(f"\nSimulando atraso de 20 dias:")
    print(f"  Dias de atraso: {e2.dias_atraso} (esperado: 6)")
    print(f"  Multa: R$ {e2.multa:.2f} (esperado: 15.00)")