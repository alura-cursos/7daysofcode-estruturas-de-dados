class Jogo:
  def __init__(self):
    self.pontuacao = {}

  def adicionar_jogador(self, usuario):
    self.pontuacao[usuario] = 0
  
  def atualizar_pontuacao(self, usuario, pontos):
    if usuario in self.pontuacao:
      self.pontuacao[usuario] += pontos

  def remover_jogador(self, usuario):
    del self.pontuacao[usuario]

  def listar_pontuacao(self):
    if len(self.pontuacao) == 0: 
      print("Não há jogadores nesta rodada no momento!")
      return
    ranking = sorted(self.pontuacao.items(), key=lambda x: x[1], reverse=True)
    for usuario, pontos in ranking:
      print(f"{usuario}: {pontos} pontos")

  def obter_vencedor(self):
    max_pontos = max(self.pontuacao.values()) # encontra a maior pontuação
    for usuario, pontos in self.pontuacao.items():
      if pontos == max_pontos:
        print(f"O usuário {usuario} venceu o jogo com {pontos} pontos!")
        return usuario # retorna o nome do jogador com a maior pontuação
      
jogo = Jogo()

jogo.adicionar_jogador('GiMoeller')
jogo.adicionar_jogador('SoccerChamp23')
jogo.adicionar_jogador('MusicManiac')
jogo.adicionar_jogador('FitnessFanatic')
jogo.adicionar_jogador('StarGazer92')
jogo.adicionar_jogador('BookWorm1985')

jogo.atualizar_pontuacao('GiMoeller', 20)
jogo.atualizar_pontuacao('StarGazer92', 10)

jogo.listar_pontuacao()

jogo.remover_jogador('FitnessFanatic')

jogo.listar_pontuacao()

jogo.obter_vencedor()

  
