from tkinter import Tk, Label, Entry, Button, Frame
from tkinter.messagebox import showinfo, showerror
from tkinter.ttk import Treeview
from mysql.connector import connect
import sys
import random


def centralizar_janela(janela):
    janela.update()
    largura_da_tela = janela.winfo_screenwidth()
    altura_da_tela = janela.winfo_screenheight()

    largura_da_janela = janela.winfo_width()
    altura_da_janela = janela.winfo_height()

    meio_x = largura_da_tela // 2
    meio_y = altura_da_tela // 2

    metade_da_largura = largura_da_janela // 2
    metade_da_altura = altura_da_janela // 2

    x = meio_x - metade_da_largura
    y = meio_y - metade_da_altura

    janela.geometry("+" + str(x) + "+" + str(y))

# Objeto crido para o Banco de Dados
class BancoLogin: # um objeto criado para cada janela
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def obter_conexao(self):
        return connect(host = self.host, user = self.user, password = self.password, database = self.database)
    def login_ok(self, email, senha):
        # esta consulta precisa ser alterada para funcionar
        # com o método de criptografia escolhido
        sql = "select nome from usuario where email=%s and senha=SHA2(%s, 256)"
        conexao = self.obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(sql, [email, senha])
        resultado = cursor.fetchall()
        conexao.close()
        # se for encontrado exatamente um usuário
        # com este usuário e senha, retorna o nome
        # desse usuário; senão, retorna None.
        if len(resultado) == 1:
            return resultado[0][0]
        return None

class JanelaLogin:
    # botao para sair da Janela
    def clique_sair(self):
        sys.exit(0)
    def clique_conectar(self):
        usuario = self.campo1.get()
        senha = self.campo2.get()
        print(usuario, senha)
        nome = self.banco.login_ok(usuario, senha)
        if nome is not None:
            showinfo(title="Sucesso", message="Seja bem-vindo(a), " + nome + ".")
            self.janela.destroy()  # fecha a janela de login
            JanelaProduto()  # abre a janela do CRUD de produtos
        else:
            showerror(title="Acesso negado",
                      message="Não foi encontrado um usuário com este e-mail e senha.")

    def __init__(self):
        self.banco = BancoLogin("localhost", "user1405", "poo", "aula0406") #Muadar o banco


    #Gerador de Codigo Alatório
    def clique_cadastrar(self):
        cod = random.randint(0,9999)
        print("Número gerado com sucesso")
        print(str(cod).zfill(4))


    #configurações do servidor do Gmail
        servico_smtp = "smtp.gmail.com"
        porta_smtp = 587
        pessoal = "rgf.lic22@uea.edu.br"
        senha_pessoal = "95301542249"

    def __init__(self):
        janela = Tk()
        janela.title('LOGIN')
        janela.rowconfigure(4) # 4 Linhas
        janela.columnconfigure(3) # 4 colunas

        rotulo1 = Label(janela, text="AUTENTICAÇÃO DE USÚARIO", font="Verdana 18 bold", fg="white", bg="darkblue")
        rotulo1.grid(row=0, column=0, columnspan=4, sticky="wesn")

        rotulo2 = Label(janela, text="E-mail:", font="Verdana 18")
        rotulo2.grid(row=1, column=0,  sticky="wesn")

        rotulo3 = Label(janela, text="Senha:", font="Verdana 18")
        rotulo3.grid(row=2, column=0,  sticky="wesn")

        campo1 = Entry(janela, text='email', font='Verdana 18')
        campo1.grid(row=1, column=1, columnspan=2, sticky="wesn")
        campo1.focus_force()
        self.campo1 = campo1

        campo2 = Entry(janela, text="senha", font="Verdana 18", show='*')
        campo2.grid(row=2, column=1, columnspan=2, sticky="wesn")
        self.campo2 = campo2

        botao1 = Button(janela, text="Conectar", font="Verdana 18", bg="gray", command=self.clique_conectar)
        botao1.grid(row=3, column=0, sticky="wesn")

        botao2 = Button(janela, text="Cadastrar", font="Verdana 18", bg="gray",  command=self.clique_cadastrar)
        botao2.grid(row=3, column=1,  sticky="wesn")

        botao3 = Button(janela, text="Fechar", font="Verdana 18", bg="gray", command=self.clique_sair)
        botao3.grid(row=3, column=2, sticky="wesn")

        centralizar_janela(janela)
        janela.mainloop()

class JanelaProduto:
    def __init__(self):
        janela = Tk()
        janela.title("CRUD - Produtos")
        janela.rowconfigure(6)
        janela.columnconfigure(4)
        fonte = "Helvetica 14"

        rotulo = Label(janela, font=fonte, text="Digite o termo procurado:")
        rotulo.grid(row=0, column=0, columnspan=2, sticky="wesn")

        campo = Entry(janela, font=fonte)
        campo.grid(row=0, column=2, columnspan=2, sticky="wesn")

        rotulo = Label(janela, font=fonte,
                       text="CADASTRO DE PRODUTOS", bg="darkblue", fg="white")
        rotulo.grid(row=1, column=0, columnspan=4, sticky="wesn")

        frame = Frame(janela)
        frame.columnconfigure(2)
        frame.rowconfigure(1)
        # selectmode='browse' (somente uma linha pode ser selecionada)
        # show='headings' (exibe o rótulo das colunas no cabeçalho)
        tabela = Treeview(frame, selectmode="browse",
                          columns=["nome", "categoria", "preco",  "estoque"],
                          show='headings')
        tabela.grid(column=0, row=0, sticky="wesn")
        tabela.heading("nome", text="Nome")
        tabela.heading("categoria", text="Categoria")
        tabela.heading("preco", text="Preço Unit.")
        tabela.heading("estoque", text="Estoque")
        frame.grid(row=2, column=0, columnspan=4, rowspan=3, sticky="wesn")
        # Adicione 20 linhas de teste usando insert('', 'end', values=[])

        botao = Button(janela, font=fonte, text="Novo")
        botao.grid(row=5, column=0, sticky="wesn")

        botao = Button(janela, font=fonte, text="Alterar")
        botao.grid(row=5, column=1, sticky="wesn")

        botao = Button(janela, font=fonte, text="Apagar")
        botao.grid(row=5, column=2, sticky="wesn")

        botao = Button(janela, font=fonte, text="Fechar")
        botao.grid(row=5, column=3, sticky="wesn")



        centralizar_janela(janela)
        janela.mainloop()

janelaLogin = JanelaLogin()








