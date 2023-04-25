# Definindo a classe ListaDeCompras para representar a lista de compras
class ListaDeCompras:
  def __init__(self):
    self.items = []
    self.quantidades = []

  # Adicionando um novo item à lista de compras
  def adicionar_item(self, item, quantidade):
    self.items.append(item)
    self.quantidades.append(quantidade)

    # Removendo um item da lista de compras
  def remover_item(self, item):
    indexDoItem = self.items.index(item)
    self.items.pop(indexDoItem)
    self.quantidades.pop(indexDoItem)

    # Listando todos os itens da lista de compras
  def listar_itens(self):
    print("Lista de compras")
    for i in range(len(self.items)):
      print(f"{self.items[i]}: {self.quantidades[i]}")

listaDeCompras = ListaDeCompras()

listaDeCompras.adicionar_item('Pão', 1)
listaDeCompras.adicionar_item('Banana', 5)
listaDeCompras.adicionar_item('Bolacha', 2)
listaDeCompras.adicionar_item('Melancia', 1)

listaDeCompras.listar_itens()

listaDeCompras.remover_item('Bolacha')

listaDeCompras.listar_itens()