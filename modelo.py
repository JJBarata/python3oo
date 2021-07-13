class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Usando um '@property', não será preciso alterar o objeto 'likes' no resto do código
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    # Usando um '@property', não será preciso alterar o objeto 'nome' no resto do código
    @property
    def nome(self):
        return self._nome

    # Com o getter, poderemos fazer o tratamento do objeto 'novo_nome', definindo o novo método 'nome' 'titularizado'
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Chamando a superclasse Programa
        self.duracao = duracao


class Seriados(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filmes('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


arquivox = Seriados('arquivo x', 1992, 11)
arquivox.dar_likes()
arquivox.dar_likes()
print(f'Seriado: {arquivox.nome} - Ano: {arquivox.ano} - Temporadas: {arquivox.temporadas} - Likes: {arquivox.likes}')


