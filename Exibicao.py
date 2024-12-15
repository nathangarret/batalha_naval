# Exibicao.py

class Exibicao:
    # Classe responsável pela exibição de elementos visuais do jogo, como o tabuleiro e mensagens. 
    # Estáticos, pois não dependem de instâncias da classe.
    @staticmethod
    def mostrar_tabuleiro(tabuleiro):
        # Exibe a linha superior com números das colunas, numerados de 1 até o tamanho do tabuleiro.
        print("  " + " ".join([str(i + 1) for i in range(len(tabuleiro))]))
        for i, linha in enumerate(tabuleiro):
            print(chr(65 + i) + " " + " ".join(linha)) # 65 - Tabela ASCII 'A'

    @staticmethod
    def mensagem(mensagem):
        print(mensagem)