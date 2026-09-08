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

class Series(Filmes):
    def __init__(self, titulo, ano, classificacaoEtaria, temporada, episodio):
        super().__init__(titulo, None, None, ano, classificacaoEtaria)
        self.temporada = temporada
        self.episodio = episodio       
    def Assistir(self):
            print(f"Assistindo a série '{self.titulo}'.")

    def ver_info_serie(self):
            print(f"Série: '{self.titulo}'. Temporada: {self.temporada}. Episódio: {self.episodio}. Ano: {self.ano}. Classificação Etária: {self.classificacaoEtaria} anos")

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

class Assinante(Usuario):
     def __init__(self, nome, email, senha, idade, plano):
          super().__init__(nome, email, senha, idade)
          self.plano = plano

     def Gereniciar_Assinatura(self):
        print(f"Nome: {self.nome} | Sua assinatura: '{self.plano}'.")
        opc = int(input("Digite 1 para mudar de plano | Digite 2 para pausar assinatura | Digite 3 para cancelar a assinatura \nDigite sua opção: "))
        if opc == 1:
             assinatura = input("Planos disponíveis: Premium(vigente) | Plus | Pro\nDigite sua opção: ").lower()
             if assinatura == "premium":
                  print("Esse já é seu plano.")
             elif assinatura == "plus":
                  self.plano = "Plus"
                  print("Seu plano foi mudado: Plano 'Plus' vigente.")
             elif assinatura == "pro":
                  self.plano = "Pro"
                  print("Seu plano foi mudado: Plano 'Pro' vigente.")
             else:
                  print("Opção inválida.")
        elif opc == 2:
             ctz = input("Você realmente deseja pausar sua assinatura? (sim/não): ").lower()
             if ctz == "não":
                  print("Assinatura não foi pausada.")
             if ctz == "sim":
                  print("Assinatura pausada.")
        elif opc == 3:
             ctz = input("Você realmente deseja cancelar sua assinatura? (sim/não)").lower()
             if ctz == "não":
                  print("Assinatura não cancelada.")
             if ctz == "sim":
                  print("Assinatura cancelada.")
        else:
             print("Opção inválida.")

class Administrador(Usuario):
     def __init__(self, nome, email, senha, idade, acesso):
          super().__init__(nome, email, senha, idade)
          self.acesso = acesso

     def Gerenciar_Plataforma(self):
          senha = input("Digite a senha do administrador para ter acesso: ")
          if senha == self.acesso:
               print("Bem vindo!")
               editar = int(input("Digite 1 adicionar/remover um usuário | Digite 2 para adicionar/remover um filme ou série | Digite 3 para validar uma avaliação \nDigite sua opção: "))
               if editar == 1:
                    editar_user = input("Deseja adicionar ou remover um usuário?(adicionar/remover): ").lower()
                    if editar_user == "adicionar":
                         name = input("Digite o nome do usuário: ")
                         print(f"{name} adicionado!")
                    elif editar_user == "remover":
                         name = input("Digite o nome do usuário existente: ")
                         print(f"{name} foi removido!")
                    else:
                         ("Opção cancelada.")
               elif editar == 2:
                    editar_catalogo = input("Digite se é um filme ou série(filme/série): ").lower()
                    if editar_catalogo == "filme":
                         editar_filme = input("Deseja adicionar ou remover um filme?(adicionar/remover): ").lower()
                         if editar_filme == "adicionar":
                              name = input("Digite o nome do filme: ")
                              print(f"'{name}' foi adicionado!")
                         elif editar_filme == "remover":
                              name = input("Digite o nome do filme existente no catálogo: ")
                              print(f"'{name}' foi removido!")
                         else:
                              print("Opção cancelada.")
                    elif editar_catalogo == "série":
                         editar_serie = input("Deseja adicionar ou remover uma série?(adicionar/remover): ").lower()
                         if editar_serie == "adicionar":
                              name = input("Digite o nome da série: ")
                              print(f"'{name}' foi adicionada!")
                         elif editar_serie == "remover":
                              name = input("Digite o nome da série existente no catálogo: ")
                              print(f"'{name}' foi removida!")
                         else:
                              print("Opção cancelada.")
                    else:
                         print("Opção inválida.")
               elif editar == 3:
                    validar_av = input("Digite se quer validar a avaliação(sim/não): ").lower()
                    if validar_av == "sim":
                         print("Avaliação validada!")
                    elif validar_av == "não":
                         print("Avaliação não validada!")
                    else:
                         print("Opção inválida.")
               else:
                    print("Opção inválida")
          else:
               print("Senha incorreta!")


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
print()
serie1 = Series("Atlanta", 2022, 16, 4, 5)
serie1.Assistir()
serie1.Avaliar()
serie1.ver_info_serie()
print()
serie2 = Series("Dexter", 2009, 16, 4, 12)
serie2.Assistir()
serie2.Avaliar()
serie2.ver_info_serie()
print()
serie3 = Series("The Boys", 2022, 16, 3, 6)
serie3.Assistir()
serie3.Avaliar()
serie3.ver_info_serie()
print()
user1 = Usuario("Cláudia", "claudia123@gmail.com", "cld231", 21)
user1.Cadastrar()
user1.Logar()
user1.AlterarSenha()
print()
user2 = Assinante("Márcio", "marcio456@gmail.com", "mrc546", 22, "Premium")
user2.Gereniciar_Assinatura()
print()
user3 = Administrador("Ricardo", "ricardo789@gmail.com", "rcrd897", 23, "poliflix.org")
user3.Gerenciar_Plataforma()