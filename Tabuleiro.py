import random

class Tabuleiro:
    def __init__(self, tamanho=6):
        self.tamanho = tamanho
        self.tabuleiro = [["\u2588" for _ in range(tamanho)] for _ in range(tamanho)]
        self.visivel = [["\u2588" for _ in range(tamanho)] for _ in range(tamanho)]
        self.embarcacoes = []
        self.jogadas = 0
        self.navios_afundados = 0
        self.submarinos_afundados = 0

    def posicionar_embarcacoes(self):
        # Posicionar 5 navios (1 posição cada)
        for _ in range(5):
            self._posicionar_embarcacao(1)

        # Posicionar 3 submarinos (2 posições cada)
        for _ in range(3):
            self._posicionar_embarcacao(2)

    def _posicionar_embarcacao(self, tamanho):
        while True:
            orientacao = random.choice(["H", "V"])
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)

            if self._verificar_posicao_disponivel(linha, coluna, tamanho, orientacao):
                posicoes = []
                for i in range(tamanho):
                    if orientacao == "H":
                        self.tabuleiro[linha][coluna + i] = "E"
                        posicoes.append((linha, coluna + i))
                    else:
                        self.tabuleiro[linha + i][coluna] = "E"
                        posicoes.append((linha + i, coluna))
                self.embarcacoes.append(posicoes)
                break

    def _verificar_posicao_disponivel(self, linha, coluna, tamanho, orientacao):
        try:
            for i in range(tamanho):
                if orientacao == "H":
                    if self.tabuleiro[linha][coluna + i] != "\u2588":
                        return False
                else:
                    if self.tabuleiro[linha + i][coluna] != "\u2588":
                        return False
            return True
        except IndexError:
            return False

    def atacar(self, linha, coluna):
        self.exibir_status()
        self.jogadas += 1
        if self.tabuleiro[linha][coluna] == "E":
            self.tabuleiro[linha][coluna] = "\u2316"  # X
            self.visivel[linha][coluna] = "\u2316"
            self._verificar_embarcacao_afundada()
            return "Embarcação Atingida"
        elif self.tabuleiro[linha][coluna] == "\u2316":
            return "Embarcação afundada"
        elif self.tabuleiro[linha][coluna] == "\u2588":
            self.tabuleiro[linha][coluna] = "_"
            self.visivel[linha][coluna] = "_"
            return "Água"

    def _verificar_embarcacao_afundada(self):
        for embarcacao in self.embarcacoes:
            if all(self.tabuleiro[linha][coluna] == "\u2316" for linha, coluna in embarcacao):
                for linha, coluna in embarcacao:
                    self.tabuleiro[linha][coluna] = "X"
                    self.visivel[linha][coluna] = "X"
                if len(embarcacao) == 1:
                    self.navios_afundados += 1
                else:
                    self.submarinos_afundados += 1
                self.embarcacoes.remove(embarcacao)

    def todas_embarcacoes_afundadas(self):
        return all(
            self.tabuleiro[linha][coluna] != "E"
            for linha in range(self.tamanho)
            for coluna in range(self.tamanho)
        )

    def obter_tabuleiro_visivel(self):
        return self.visivel

    def exibir_status(self):
        print(f"Jogadas até agora: {self.jogadas}")
        print(f"Afundados até agora = Navios {self.navios_afundados} de 5 | Submarinos {self.submarinos_afundados} de 3")