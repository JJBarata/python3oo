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


class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Chamando a superclasse Programa
        self.duracao = duracao

    # Criando o método imprime para a classe Filmes, utilizando o método especial "dunder str"
    def __str__(self):
        return f'{programa.nome} - {programa.ano} - {self.duracao} min - {programa.likes} likes'


class Seriados(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # Criando o método imprime para a classe Seriados, utilizando o método especial "dunder str"
    def __repr__(self):
        return f'Série com __repr__ {programa.nome} - {programa.ano} - {self.temporadas} temporadas - {programa.likes} likes'


vingadores = Filmes('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()


arquivox = Seriados('arquivo x', 1992, 11)
arquivox.dar_likes()
arquivox.dar_likes()


filmes_e_series = [vingadores, arquivox]

for programa in filmes_e_series:
    print(programa.__repr__())
    print(programa)

