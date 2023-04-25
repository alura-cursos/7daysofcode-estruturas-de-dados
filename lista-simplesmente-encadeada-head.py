# Definindo a classe Paciente para representar o nó da lista
class Paciente:
  def __init__(self, id, nome, estadoSaude):
    self.id = id
    self.nome = nome
    self.estadoSaude = estadoSaude
    self.proximoPaciente = None

# Definindo a classe ListaDePacientes para representar a lista simplesmente encadeada
class ListaDePacientes:
  def __init__(self):
    self.head = None

  def adicionar_paciente(self, id, nome, estadoSaude):
    novoPaciente = Paciente(id, nome, estadoSaude)
    if self.head is None:
      # Se a lista estiver vazia, o novo paciente é adicionado como cabeça da lista
      self.head = novoPaciente
    else:
      # Caso contrário, o paciente é adicionado ao final da lista
      pacienteAtual = self.head
      while pacienteAtual.proximoPaciente is not None:
        pacienteAtual = pacienteAtual.proximoPaciente
      pacienteAtual.proximoPaciente = novoPaciente

  # Método para remover um paciente da lista, recebe como parâmetro o id do paciente a ser removido
  def remover_paciente(self, id):
    if self.head is None:
      # Se a lista estiver vazia, não há o que remover
      return
    elif self.head.id == id:
      # Se o paciente a ser removido for a cabeça da lista, basta atualizar o ponteiro para o próximo paciente
      self.head = self.head.proximoPaciente
      return
    else:
      # Caso contrário, percorremos a lista até encontrar o paciente a ser removido
      pacienteAtual = self.head
      while pacienteAtual.proximoPaciente is not None:
        if pacienteAtual.proximoPaciente.id == id:
          # Quando encontramos o paciente, atualizamos o ponteiro do paciente anterior para o próximo paciente
          pacienteAtual.proximoPaciente = pacienteAtual.proximoPaciente.proximoPaciente
          return
        pacienteAtual = pacienteAtual.proximoPaciente

  # Método para imprimir todos os pacientes da lista
  def listar_pacientes(self):
    if self.head is None:
      print("Não há pacientes nesta lista.")
    else:
      pacienteAtual = self.head
      while pacienteAtual is not None:
        print(f"Nome: {pacienteAtual.nome}, ID: {pacienteAtual.id}, Estado de saúde: {pacienteAtual.estadoSaude}")
        pacienteAtual = pacienteAtual.proximoPaciente


listaDePacientes = ListaDePacientes()

listaDePacientes.adicionar_paciente(1, "Giovanna", "Estável")
listaDePacientes.adicionar_paciente(2, "Lucas", "Tratamento intensivo")
listaDePacientes.adicionar_paciente(3, "Alex", "Crítico")
listaDePacientes.adicionar_paciente(4, "Beatriz", "Estável")

listaDePacientes.listar_pacientes()

listaDePacientes.remover_paciente(3)

listaDePacientes.listar_pacientes()

