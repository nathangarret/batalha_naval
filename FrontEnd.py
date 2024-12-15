# FrontEnd

from Tabuleiro import Tabuleiro
from Exibicao import Exibicao
from Persistencia import Persistencia

def iniciar_jogo():
    while True:
        Exibicao.mensagem("\nMenu Principal:")
        Exibicao.mensagem("1. Iniciar Jogo")
        Exibicao.mensagem("2. Ver Ranking")
        Exibicao.mensagem("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogar()
        elif opcao == "2":
            mostrar_ranking()
        elif opcao == "3":
            break
        else:
            Exibicao.mensagem("Opção inválida!")

def jogar():
    tabuleiro = Tabuleiro()
    tabuleiro.posicionar_embarcacoes()

    jogadas = 0
    while not tabuleiro.todas_embarcacoes_afundadas():
        Exibicao.mostrar_tabuleiro(tabuleiro.obter_tabuleiro_visivel())
        entrada = input("Informe a coordenada (ex: A1) ou -1 para desistir: ").upper()

        if entrada == "-1":
            Exibicao.mensagem("Jogo encerrado pelo usuário.")
            return

        try:
            linha = ord(entrada[0]) - 65
            coluna = int(entrada[1:]) - 1
            resultado = tabuleiro.atacar(linha, coluna)
            Exibicao.mensagem(resultado)
            jogadas += 1
        except (IndexError, ValueError):
            Exibicao.mensagem("Coordenada inválida. Tente novamente.")

    Exibicao.mensagem("Parabéns! Você afundou todas as embarcações!")
    nome = input("Digite seu nome para o ranking: ")
    Persistencia.salvar_pontuacao(nome, jogadas)

def mostrar_ranking():
    ranking = Persistencia.carregar_ranking()
    Exibicao.mensagem("\nRanking:")
    Exibicao.mensagem("==== Melhores Pontuacões ====")
    Exibicao.mensagem(f"{'Nome':<10} {'# Jogadas':>20}")
    for i, (nome, pontuacao) in enumerate(sorted(ranking, key=lambda x: int(x[1]))):
        Exibicao.mensagem(f"{i + 1:<2} {nome:<10} {pontuacao:>10}")