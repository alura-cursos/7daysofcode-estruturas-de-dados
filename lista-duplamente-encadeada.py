# Definindo a classe Produto para representar cada item do estoque
class Produto:
  def __init__(self, codigo_barras, nome, preco, quantidade):
    self.codigo_barras = codigo_barras
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade
    self.proximo_produto = None
    self.produto_anterior = None

# Definindo a classe ListaDeProdutos para representar a lista duplamente encadeada
class ListaDeProdutos:
  def __init__(self):
    self.head = None
    self.tail = None

  def adicionar_produto(self, codigo_barras, nome, preco, quantidade):
    novo_produto = Produto(codigo_barras, nome, preco, quantidade)
    if self.head is None:
      self.head = novo_produto
      self.tail = novo_produto
    else:
      self.tail.proximo_produto = novo_produto
      novo_produto.produto_anterior = self.tail
      self.tail = novo_produto

  def remover_produto(self, codigo_barras):
    if self.head is None:
      return
    elif self.head.codigo_barras == codigo_barras:
      self.head = self.head.proximo_produto
      if self.head is not None:
        self.head.produto_anterior = None
      else:
        self.tail = None
      return
    elif self.tail.codigo_barras == codigo_barras:
      self.tail = self.tail.produto_anterior
      self.tail.proximo_produto = None
      return
    else:
      produto_atual = self.head
      while produto_atual is not None:
        if produto_atual.codigo_barras == codigo_barras:
          produto_atual.produto_anterior.proximo_produto = produto_atual.proximo_produto
          produto_atual.proximo_produto.produto_anterior = produto_atual.produto_anterior
          return
        produto_atual = produto_atual.proximo_produto

  def atualizar_quantidade(self, codigo_barras, nova_quantidade):
    produto_atual = self.head
    while produto_atual is not None:
      if produto_atual.codigo_barras == codigo_barras:
        produto_atual.quantidade = nova_quantidade
        return
      produto_atual = produto_atual.proximo_produto

  def listar_produtos(self):
    if self.head is None:
      print("Não há produtos no estoque.")
    else:
      produto_atual = self.head
      while produto_atual is not None:
        print(f"Código de barras: {produto_atual.codigo_barras}, Nome: {produto_atual.nome}, Preço: {produto_atual.preco}, Quantidade: {produto_atual.quantidade}")
        produto_atual = produto_atual.proximo_produto

listaDeProdutos = ListaDeProdutos()

listaDeProdutos.adicionar_produto("001", "Arroz", 10.50, 50)
listaDeProdutos.adicionar_produto("002", "Feijão", 8.90, 30)
listaDeProdutos.adicionar_produto("003", "Macarrão", 5.99, 70)
listaDeProdutos.adicionar_produto("004", "Óleo", 7.50, 20)

listaDeProdutos.listar_produtos()

listaDeProdutos.atualizar_quantidade("001", 40)

listaDeProdutos.listar_produtos()

listaDeProdutos.remover_produto("003")

listaDeProdutos.listar_produtos()