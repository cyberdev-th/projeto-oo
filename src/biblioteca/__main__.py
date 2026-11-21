"""Ponto de entrada do sistema de biblioteca

Rode com: PYTHONPATH=src python -m biblioteca
"""

from biblioteca.biblioteca import Biblioteca
from biblioteca.livro import Livro
from biblioteca.usuario import Usuario

def separador(titulo: str) -> None:
    print(f"\n{'=' * 50}")
    print(f" {titulo}")
    print("=" * 50)

def main() -> None:
    separador("1. Criando biblioteca e cadastrando livros e usuários")

    biblio = Biblioteca("Central")

    dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", "111")
    memorias = Livro("Memórias Póstumas", "Machado de Assis", "222")
    grande_sertao = Livro("Grande Sertão: Veredas", "Guimarães Rosa", "333")

    print(f"Adiciona Dom Casmurro:  {biblio.adicionar_livro(dom_casmurro)}")
    print(f"Adiciona Memórias:      {biblio.adicionar_livro(memorias)}")
    print(f"Adiciona Grande Sertão: {biblio.adicionar_livro(grande_sertao)}")
    print(f"Adiciona repetido:      {biblio.adicionar_livro(dom_casmurro)} (esperado: False)")

    ana = Usuario('Ana', '1')
    bia = Usuario('Bia', '2')

    print(f"Cadastra Ana: {biblio.cadastrar_usuario(ana)}")
    print(f"Cafastra Bia: {biblio.cadastrar_usuario(bia)}")
    print(f"Cadastra Ana de novo: {biblio.cadastrar_usuario(ana)} (esperado: False)")

    print(f"\n{biblio}")

    separador("2. Ana pega Dom Casmurro")
    e1 = biblio.emprestar(dom_casmurro, ana)
    print(f"Empréstimo criado: {'sim' if e1 else 'não'}")
    print(f"Dom Casmurro disponível? {dom_casmurro.disponivel} (esperado: False)")

    separador("3. Bia tenta o mesmo livro (já emprestado)")
    e2 = biblio.emprestar(dom_casmurro, bia)
    print(f"Empréstimo criado: {'sim' if e2 else 'não'} (esperado: não)")

    separador("4. Ana devolve Dom Casmurro")
    multa = biblio.devolver(e1)
    print(f"Devolução: multa = R$ {multa:.2f}")
    print(f"Dom Casmurro disponível? {dom_casmurro.disponivel} (esperado: True)")

    separador("5. Ana tenta devolver novamente")
    multa2 = biblio.devolver(e1)
    print(f"Devolução: {multa2} (esperado: None)")

    separador("6. Estado Final")
    print(biblio)
    print(f"Empréstimos ativos: {len(biblio.emprestimos_ativos())}")
    print(f"Livros em atraso: {len(biblio.livros_em_atraso())}")

if __name__ == "__main__":
    main()