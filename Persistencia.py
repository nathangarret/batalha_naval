# Persistência

import os

class Persistencia:
    ARQUIVO_RANKING = "ranking.txt"

    @staticmethod
    def salvar_pontuacao(nome, pontuacao):
        with open(Persistencia.ARQUIVO_RANKING, "a") as arquivo:
            arquivo.write(f"{nome} {pontuacao}\n")

    @staticmethod
    def carregar_ranking():
        if not os.path.exists(Persistencia.ARQUIVO_RANKING):
            return []

        with open(Persistencia.ARQUIVO_RANKING, "r") as arquivo:
            linhas = arquivo.readlines()
        return [linha.strip().split(maxsplit=1) for linha in linhas]