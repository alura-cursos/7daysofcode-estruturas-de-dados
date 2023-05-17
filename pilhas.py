class Livro:
  def __init__(self, nome, numeroDePaginas):
    self.nome = nome
    self.numeroDePaginas = numeroDePaginas

class PilhaDeLivros:
  def __init__(self):
    self.pilhaLivros = []

  def adicionar_livro(self,nome, numeroDePaginas):
    novo_livro = Livro(nome, numeroDePaginas)
    self.pilhaLivros.append(novo_livro) # Adiciona no final da pilha

  def remover_livro(self):
    if len(self.pilhaLivros) < 1:
      return None
    return self.pilhaLivros.pop() # Remove e retorna o último elemento adicionado na pilha
  
  def mostrar_livro_topo(self):
    ultimo_index = len(self.pilhaLivros) - 1
    print(f"O livro que está no topo é {self.pilhaLivros[ultimo_index]}")
    return self.pilhaLivros[ultimo_index]

  def mostrar_livros(self):
    if len(self.pilhaLivros) < 1:
      print("Não há livros na pilha no momento!")
      return
    for livro in self.pilhaLivros:
      print(f"Nome: {livro.nome}, número de páginas: {livro.numeroDePaginas}")


pilha = PilhaDeLivros()

pilha.adicionar_livro("A Guerra dos Tronos", 600)
pilha.adicionar_livro("A Fúria dos Reis", 648)
pilha.adicionar_livro("A Tormenta das Espadas", 848)
pilha.adicionar_livro("O Festim dos Corvos", 608)
pilha.adicionar_livro("A Dança dos Dragões", 336)

pilha.mostrar_livros()

livroRemovido = pilha.remover_livro()
print(f"Livro removido da pilha: Nome {livroRemovido.nome}, número de páginas: {livroRemovido.numeroDePaginas}")

pilha.mostrar_livros()