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

    # Criando o método imprime para a superclasse Programa, utilizando o método especial "dunder str"
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Chamando a superclasse Programa
        self.duracao = duracao

    # Criando o método imprime para a classe Filmes, utilizando o método especial "dunder str"
    def __str__(self):
        return f'Filme {programa.nome} - {programa.ano} - {self.duracao} min - {programa.likes} likes'


class Seriados(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # Criando o método imprime para a classe Seriados, utilizando o método especial "dunder str"
    def __str__(self):
        return f'Série {programa.nome} - {programa.ano} - {self.temporadas} temporadas - {programa.likes} likes'


vingadores = Filmes('vingadores - guerra infinita', 2018, 160)
arquivox = Seriados('arquivo x', 1992, 11)
demolidor = Seriados('demolidor', 2014, 2)
tmep = Filmes('todo mundo em pânico', 1999, 100)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
arquivox.dar_likes()
arquivox.dar_likes()
arquivox.dar_likes()
arquivox.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series = [arquivox, vingadores, tmep, demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {playlist_fim_de_semana.tamanho}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(f'Tem ou não tem? {demolidor in playlist_fim_de_semana.listagem}')


