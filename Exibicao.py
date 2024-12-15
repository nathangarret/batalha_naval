# Exibicao

class Exibicao:
    @staticmethod
    def mostrar_tabuleiro(tabuleiro):
        print("  " + " ".join([str(i + 1) for i in range(len(tabuleiro))]))
        for i, linha in enumerate(tabuleiro):
            print(chr(65 + i) + " " + " ".join(linha))

    @staticmethod
    def mensagem(mensagem):
        print(mensagem)