class Pedido:
  def __init__(self, numero, nome, prato):
    self.numero = numero
    self.nome = nome
    self.prato = prato

class FilaDePedidos:
  def __init__(self):
    self.filaPedidos = []

  def adicionar_pedido(self, numero, nome, prato):
    novo_pedido = Pedido(numero, nome, prato)
    self.filaPedidos.append(novo_pedido) # Adiciona no final da fila

  def remover_pedido(self):
    if len(self.filaPedidos) < 1:
      return None
    return self.filaPedidos.pop(0) # Remove e retorna o primeiro elemento da fila

  def mostrar_pedidos(self):
    if len(self.filaPedidos) < 1:
      print("Não há pedidos no momento!")
      return
    for pedido in self.filaPedidos:
      print(f"Número: {pedido.numero}, Nome: {pedido.nome}, Prato: {pedido.prato}")


fila = FilaDePedidos()

fila.adicionar_pedido(1, "João", "Hambúrguer")
fila.adicionar_pedido(2, "Maria", "Pizza")
fila.adicionar_pedido(3, "José", "Sushi")

fila.mostrar_pedidos()

pedidoAtendido = fila.remover_pedido()
print(f"Pedido atendido: Número {pedidoAtendido.numero}, Prato: {pedidoAtendido.prato}")

fila.mostrar_pedidos()