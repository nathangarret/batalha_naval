# Persistencia.py

import os

class Persistencia:
    ARQ_RANKING = "ranking.txt" # Nome do arquivo onde o ranking será armazenado.

    @staticmethod
    def salvar_pontuacao(nome, pontuacao):
        with open(Persistencia.ARQ_RANKING, "a") as arquivo:
            arquivo.write(f"{nome} {pontuacao}\n")

    @staticmethod
    def carregar_ranking():
        if not os.path.exists(Persistencia.ARQ_RANKING): # Verifica se o arquivo existe.
            return [] # Retorna uma lista vazia se o arquivo não for encontrado.

        with open(Persistencia.ARQ_RANKING, "r") as arquivo:
            linhas = arquivo.readlines()
        return [linha.strip().split(maxsplit=1) for linha in linhas] # Divide cada linha em nome e pontuação.