from tkinter import *
from tkinter import ttk
from tkinter import tix
from class_fusc import Funsc
from relatorios import Relatorios


root = tix.Tk()


class Application(Funsc, Relatorios):
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
                                font = ('verdana', 8,'bold'), command= self.busca_cliente)
        self.bt_buscar.place(relx = 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        self.balao_buscar = tix.Balloon(self.frame_1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = 'Digite o nome do cliente que deseja pesquisar')


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
        menubar.add_cascade(label = "Relatorios", menu = filemenu2)

        filemenu.add_command(label = 'sair', command= Quit)
        filemenu.add_command(label = 'Limpar cliente', command= self.limpa_tela)
        
        filemenu2.add_command(label = 'Ficha do cliente', command= self.geraRelatCliente)
        



Application()