class Filmes:
    def __init__(self, titulo, diretor, duracao, ano, classificacaoEtaria):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
        self.ano = ano
        self.classificacaoEtaria = classificacaoEtaria

    def Assistir(self):
        print(f"Assistindo o filme '{self.titulo}'.")

    def Avaliar(self):
        print(f"'{self.titulo}' avaliado!")

    def ver_info_filme(self):
        print(f"Filme: '{self.titulo}. Diretor: {self.diretor}. Duração: {self.duracao} minutos. Ano: {self.ano}. Classificação Etária: {self.classificacaoEtaria} anos")

class Series:
    def __init__(self, titulo, temporada, episodio, ano, classificacaoEtaria):
        self.titulo = titulo
        self.temporada = temporada
        self.episodio = episodio
        self.ano = ano
        self.classificacaoEtaria = classificacaoEtaria

    def Assistir(self):
            print(f"Assistindo a serie '{self.titulo}'.")

    def Avaliar(self):
            print(f"'{self.titulo}' avaliado!")

    def ver_info_serie(self):
            print(f"Serie: '{self.titulo}. Temporada: {self.temporada}. Episódio: {self.episodio}. Ano: {self.ano}. Classificação Etária: {self.classificacaoEtaria} anos")

class Usuario:
    def __init__(self, nome, email, senha, idade):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade

    def Cadastrar(self):
        print(f"{self.nome} cadastrado com sucesso!")

    def Logar(self):
            print(f"{self.nome} logado com sucesso!")

    def AlterarSenha(self):
        print(f"{self.senha} alterada com sucesso!")

filme1 = Filmes("Harry Potter e a Câmara Secreta", "Chris Columbus", 161, 2002, 10)
filme1.Assistir()
filme1.Avaliar()
filme1.ver_info_filme()
print()
filme2 = Filmes("Como Treinar o Seu Dragão", "Chris Sanders", 98, 2010, "Livre")
filme2.Assistir()
filme2.Avaliar()
filme2.ver_info_filme()
print()
filme3 = Filmes("As Branquelas", "Keenen Ivory Wayans", 104, 2004, 14)
filme3.Assistir()
filme3.Avaliar()
filme3.ver_info_filme()