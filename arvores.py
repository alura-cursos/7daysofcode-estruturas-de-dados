class Produto:
  def __init__(self, id, nome, quantidade):
    self.id = id
    self.nome = nome
    self.quantidade = quantidade

class Node:
  def __init__(self, produto):
    self.esquerda = None
    self.direita = None
    self.produto = produto

class ArvoreProduto:
  def __init__(self):
    self.raiz = None

  def inserir_produto(self, id, nome, quantidade):
    produto = Produto(id, nome, quantidade)
    if self.raiz is None:
      self.raiz = Node(produto)
    else:
      self._inserir_produto(produto, self.raiz)

  def _inserir_produto(self, produto, node):
    if produto.id < node.produto.id:
      if node.esquerda is None:
        node.esquerda = Node(produto)
      else:
        self._inserir_produto(produto, node.esquerda)
    elif produto.id > node.produto.id:
      if node.direita is None:
        node.direita = Node(produto)
      else:
        self._inserir_produto(produto, node.direita)
    else:
      node.produto = produto  # se o ID já existe, atualiza as informações do produto

  def buscar_produto(self, id):
    return self._buscar_produto(id, self.raiz)

  def _buscar_produto(self, id, node):
    if node is None or node.produto.id == id:
      return node
    elif id < node.produto.id:
      return self._buscar_produto(id, node.esquerda)
    else:
      return self._buscar_produto(id, node.direita)

arvore = ArvoreProduto()

arvore.inserir_produto(1, 'Camiseta', 10)
arvore.inserir_produto(2, 'Vestido', 20)
arvore.inserir_produto(3, 'Tenis', 5)

produtoBuscado1 = arvore.buscar_produto(2)
print(produtoBuscado1.produto.nome) # Retorna o produto

produtoBuscado2 = arvore.buscar_produto(20)
print(produtoBuscado2) # Retorna None

