from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funsc():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    
    def conectar_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()
        print('Banco de dados criado')
    
    def desconecta_bd(self):
        self.conn.close()
        print('Banco de dados desconectado')

    def montaTabelas(self):


        self.limpa_tela
        self.conectar_bd(); print('Conectando o banco de dados')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
                );        
    
    ''')
        
        self.conn.commit(); 
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cidade = self.cidade_entry.get()
        self.telefone = self.fone_entry.get()
        self.conectar_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def addcliente(self):
        self.variaveis()
        

        self.cursor.execute('''
            INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)''',(self.nome, self.telefone, self.cidade))
        
        
        self.conn.commit()
        self.desconecta_bd()

        self.limpa_tela()
        
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_bd()
        lista = self.cursor.execute('''
            SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC;''')
        
        for i in lista:
            self.listaCli.insert('', END, values = i)
        self.desconecta_bd()

    def deleta_cliente(self):
        self.variaveis()
        self.conectar_bd()
        self.cursor.execute('''DELETE FROM clientes where cod = ? ''', (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conectar_bd()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? 
                            where cod = ?""",(self.nome, self.telefone, self.cidade, self.codigo))
        
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

class Application(Funsc):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()

        root.mainloop()
        
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#04545c')
        self.root.geometry('780x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width= 600, height= 500)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg='#d3e3e1',
                             highlightbackground= '#2F4F4F',
                              highlightthickness= 4 )
        self.frame_1.place(relx= 0.02, rely= 0.02,
                           relwidth= 0.96, relheight= 0.46)
        
        
        self.frame_2 = Frame(self.root, bd = 4, bg='#d3e3e1',
                             highlightbackground= '#2F4F4F',
                              highlightthickness= 4 )
        self.frame_2.place(relx= 0.02, rely= 0.5,
                           relwidth= 0.96, relheight= 0.46)
        
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text = 'Limpar', bd = 2, bg = '#14838f', fg = 'white',
                                font = ('verdana', 8,'bold'), command = self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        self.bt_buscar = Button(self.frame_1, text = 'Buscar', bd = 2, bg = '#14838f', fg = 'white',
                                font = ('verdana', 8,'bold'))
        self.bt_buscar.place(relx = 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        self.bt_novo = Button(self.frame_1, text = 'Novo', bd = 2, bg = '#14838f', fg = 'white',
                                font = ('verdana', 8,'bold'), command = self.addcliente)
        self.bt_novo.place(relx = 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        self.bt_alterar = Button(self.frame_1, text = 'Alterar', bd = 2, bg = '#14838f', fg = 'white',
                                font = ('verdana', 8,'bold'), command = self.altera_cliente)
        self.bt_alterar.place(relx = 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        self.bt_apagar = Button(self.frame_1, text = 'Apagar', bd = 2, bg = '#14838f', fg = 'white',
                                font = ('verdana', 8,'bold'), command= self.deleta_cliente)
        self.bt_apagar.place(relx = 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        #Criação de Label Código
        self.lbcodigo = Label(self.frame_1, text = 'Código', bg = '#d3e3e1', fg = '#14838f',
                              font=('verdana', 8, 'bold'))
        self.lbcodigo.place(relx = 0.05, rely = 0.1, )
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.05, rely = 0.18, relwidth= 0.1)

        #Criação de Label Nome
        self.lb_nome = Label(self.frame_1, text = 'Nome', bg = '#d3e3e1', fg = '#14838f',
                             font=('verdana', 8, 'bold'))
        self.lb_nome.place(relx = 0.05, rely = 0.4 )
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely = 0.48, relwidth= 0.60)

        #Criação de Label Telefone
        self.lbfone = Label(self.frame_1, text = 'Telefone', bg = '#d3e3e1', fg = '#14838f',
                              font=('verdana', 8, 'bold'))
        self.lbfone.place(relx = 0.05, rely = 0.7, )
        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx = 0.05, rely = 0.78, relwidth= 0.1)

        #Criação de Label cidade
        self.lb_cidade = Label(self.frame_1, text = 'Cidade', bg = '#d3e3e1', fg = '#14838f',
                             font=('verdana', 8, 'bold'))
        self.lb_cidade.place(relx = 0.20, rely = 0.7 )
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx = 0.20, rely = 0.78, relwidth= 0.2)


    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, colum= ('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Codigo')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')
        

        self.listaCli.column('#0', width= 1)
        self.listaCli.column('#1', width= 50)
        self.listaCli.column('#2', width= 200)
        self.listaCli.column('#3', width= 125)
        self.listaCli.column('#4', width= 125)


        self.listaCli.place(relx = 0.01, rely= 0.01, relwidth= 0.95, relheight= 0.85)
        

        self.scrooLista = Scrollbar(self.frame_2, orient= 'vertical')
        self.listaCli.configure(yscroll = self.scrooLista.set)
        self.scrooLista.place(relx= 0.96, rely= 0.01, relwidth= 0.04, relheight= 0.85)
        self.listaCli.bind('<Double-1>', self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        def Quit(): self.root.destroy()

        menubar.add_cascade(label = "Opções", menu = filemenu)
        menubar.add_cascade(label = "Sobre", menu = filemenu2)
        filemenu.add_command(label = 'sair', command= Quit)
        filemenu.add_command(label = 'Limpar cliente', command= self.limpa_tela)

        
        

Application()