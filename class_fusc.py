import sqlite3
from tkinter import *

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
        self.select_lista()

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

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_bd()
        lista = self.cursor.execute('''
            SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC;''')
        
        for i in lista:
            self.listaCli.insert('', END, values = i)
        self.desconecta_bd()

    def busca_cliente(self):
        self.conectar_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute('''
            SELECT cod, nome_cliente, telefone, cidade from clientes
            WHERE nome_cliente LIKE '%s' order by nome_cliente ASC 
                        ''' % nome)
        buscanomeCli = self.cursor.fetchall()

        for i in buscanomeCli:
            self.listaCli.insert('', END, values = i)

        self.limpa_tela()
        self.desconecta_bd()
   