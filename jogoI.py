import random

def escolha_jogador():
  """
  Função para obter a escolha do jogador.

  Retorna:
    str: A escolha do jogador ("pedra", "papel" ou "tesoura").
  """
  while True:
    escolha_jogador = input("Digite sua escolha (pedra, papel ou tesoura): ").lower()
    if escolha_jogador in ["pedra", "papel", "tesoura"]:
      return escolha_jogador
    else:
      print("Escolha inválida. Tente novamente!")

def escolha_computador():
  """
  Função para obter a escolha aleatória do computador.

  Retorna:
    str: A escolha do computador ("pedra", "papel" ou "tesoura").
  """
  opcoes = ["pedra", "papel", "tesoura"]
  escolha_computador = random.choice(opcoes)
  return escolha_computador

def determinar_vencedor(escolha_jogador, escolha_computador):
  """
  Função para determinar o vencedor da rodada.

  Argumentos:
    escolha_jogador (str): A escolha do jogador.
    escolha_computador (str): A escolha do computador.

  Retorna:
    str: A mensagem anunciando o vencedor da rodada.
  """
  if escolha_jogador == escolha_computador:
    return "Empate!"
  elif escolha_jogador == "pedra" and escolha_computador == "tesoura":
    return "Você venceu! Pedra quebra tesoura!"
  elif escolha_jogador == "papel" and escolha_computador == "pedra":
    return "Você venceu! Papel embrulha pedra!"
  elif escolha_jogador == "tesoura" and escolha_computador == "papel":
    return "Você venceu! Tesoura corta papel!"
  else:
    return "O computador venceu!"

def jogar_novamente():
  """
  Função para perguntar se o jogador deseja jogar novamente.

  Retorna:
    bool: True se o jogador deseja jogar novamente, False caso contrário.
  """
  while True:
    resposta = input("Deseja jogar novamente? (sim/não): ").lower()
    if resposta in ["sim", "não"]:
      return resposta == "sim"
    else:
      print("Resposta inválida. Tente novamente!")

print("Bem-vindo ao jogo Pedra Papel e Tesoura!")

while True:
  escolha_jogador = escolha_jogador()
  escolha_computador = escolha_computador()

  print(f"Você escolheu {escolha_jogador}.")
  print(f"O computador escolheu {escolha_computador}.")

  resultado = determinar_vencedor(escolha_jogador, escolha_computador)
  print(resultado)

  if not jogar_novamente():
    break

print("Obrigado por jogar!")
