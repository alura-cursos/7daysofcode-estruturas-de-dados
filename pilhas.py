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

pilha.adicionar_livro("Harry Potter e a Pedra Filosofal", 223)
pilha.adicionar_livro("Harry Potter e a Câmara Secreta", 251)
pilha.adicionar_livro("Harry Potter e o Prisioneiro de Azkaban", 317)
pilha.adicionar_livro("Harry Potter e o Cálice de Fogo", 636)
pilha.adicionar_livro("Harry Potter e a Ordem da Fênix", 766)
pilha.adicionar_livro("Harry Potter e o Enigma do Príncipe", 607)
pilha.adicionar_livro("Harry Potter e as Relíquias da Morte", 607)

pilha.mostrar_livros()

livroRemovido = pilha.remover_livro()
print(f"Livro removido da pilha: Nome {livroRemovido.nome}, número de páginas: {livroRemovido.numeroDePaginas}")

pilha.mostrar_livros()