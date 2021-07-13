class Filmes:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_likes(self):
        self.likes += 1


class Seriados:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_likes(self):
        self.likes += 1


vingadores = Filmes('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


arquivox = Seriados('arquivo x', 1992, 11)
arquivox.dar_likes()
arquivox.dar_likes()
print(f'Seriado: {arquivox.nome} - Ano: {arquivox.ano} - Temporadas: {arquivox.temporadas} - Likes: {arquivox.likes}')
