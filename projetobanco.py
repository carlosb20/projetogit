from cliente.pessoas import Pessoas
from tkinter import *
from PIL import Image,ImageTk
from typing import List
from tkinter import messagebox

lista:List[Pessoas] = []


class JanelaPro:
    def __init__(self,master,original):
        self.root = master
        self.tela()
        self.imagem3()
        self.deposita_na_conta()
        self.deposia_agencia()
        self.deposia_dinheiro()
        self.botaopay()
        self.btn_cancela()
        self.original = original

    def tela(self):
        self.root.geometry('900x500+200+100')
        self.root.title('DEPOSITO')
        self.root.iconbitmap()
        self.root.state('zoomed')
        self.root['bg'] = 'yellow'
        self.labeltext = Label(self.root,text=' DEPOSITO ',bg='yellow')
        self.labeltext.config(font='Arial 20 bold')
        self.labeltext.place(relx=0.40,rely=0.08)

    def imagem3(self):
        self.imagem2 = Image.open('bra1.png')
        self.tamanho = self.imagem2.resize((100,100),Image.ANTIALIAS)
        self.origem = ImageTk.PhotoImage(self.tamanho)

        self.ver = Label(self.root,image=self.origem,bg='yellow',bd=4,relief=GROOVE)
        self.ver.place(relx=0.01,rely=0.02)

        self.linha = Label(self.root,text='_'*272,bg='yellow')
        self.linha.place(relx=0.00,rely=0.24)

    def deposita_na_conta(self):
        self.label_senha = Label(self.root,text='CONTA',padx=10)
        self.label_senha.configure(font='Arial 15 bold')
        self.label_senha.configure(bd=4)
        self.label_senha.configure(relief=GROOVE)
        self.label_senha.place(relx=0.20,rely=0.40)

        self.entry_senha = Entry(self.root,text='CONTA')
        self.entry_senha.configure(font='Arial 15 bold')
        self.entry_senha.configure(bd=4)
        self.entry_senha.configure(relief=GROOVE)
        self.entry_senha.place(relx=0.35,rely=0.40)

    def deposia_agencia(self):
        self.label_agencia = Label(self.root,text='AGENCIA')
        self.label_agencia.configure(font='Arial 15 bold')
        self.label_agencia.configure(bd=4)
        self.label_agencia.configure(relief=GROOVE)
        self.label_agencia.place(relx=0.20,rely=0.50)

        self.entry_agencia = Entry(self.root)
        self.entry_agencia.configure(font='Arial 15 bold')
        self.entry_agencia.configure(bd=4)
        self.entry_agencia.configure(relief=GROOVE)
        self.entry_agencia.place(relx=0.35,rely=0.50)


    def deposia_dinheiro(self):
        self.label_deposito = Label(self.root,text='VALOR:')
        self.label_deposito.configure(font='Arial 15 bold')
        self.label_deposito.configure(bd=4)
        self.label_deposito.configure(relief=GROOVE)
        self.label_deposito.place(relx=0.20,rely=0.60)

        self.entry_deposito = Entry(self.root)
        self.entry_deposito.configure(font='Arial 15 bold')
        self.entry_deposito.configure(bd=4)
        self.entry_deposito.configure(relief=GROOVE)
        self.entry_deposito.place(relx=0.35,rely=0.60)

    def botaopay(self):
        self.btn2 = Button(self.root, text='CONFIMA', command=self.res)
        self.btn2.configure(font="Arial 10 bold")
        self.btn2.configure(width=18)
        self.btn2.config(bg='#0000CD')
        self.btn2.config(fg='white')
        self.btn2.configure(height=2)
        self.btn2.place(relx=0.50,rely=0.80)


    def pega_senha_agencia(self,a,b):
        p: Pessoas = None
        for x in lista:
            if x.senha == a and x.agencia == b:
                p = x
        return p

    def btn_cancela(self):
        self.btn_can = Button(self.root, text='CANCELA', command=self.cancela)
        self.btn_can.configure(font="Arial 10 bold")
        self.btn_can.configure(width=18)
        self.btn_can.config(bg='#0000CD')
        self.btn_can.config(fg='white')
        self.btn_can.configure(height=2)
        self.btn_can.place(relx=0.20,rely=0.80)

    def cancela(self):
        self.original.deiconify()
        self.root.destroy()  



    def res(self):
        if self.entry_senha.get() != '' and self.entry_agencia.get() != '' and self.entry_deposito.get() != '':
            loga: Pessoas = self.pega_senha_agencia(self.entry_senha.get(),self.entry_agencia.get())
            if loga:
                loga.deposito = float(self.entry_deposito.get())
            print(loga)  
            
        self.original.deiconify()
        self.root.destroy()
        


class Contas:
    def __init__(self,master,orig):
        self.janelaC = master
        self.tela_janelaC()
        self.imagem2()
        self.label_e_entry_cadastra_nome()
        self.label_e_entry_cadastra_cpf()
        self.label_e_entry_cadastra_senha()
        self.label_e_entry_cadastra_agencia()
        self.botao_janelaC()

        self.origC = orig

    def tela_janelaC(self):
        self.janelaC.geometry('900x500+200+100')
        self.janelaC.state('zoomed')
        self.janelaC.title('CADASTRAMENTO')
        self.janelaC['bg'] = 'yellow'
        self.labeltext = Label(self.janelaC,text=' CADASTRA CONTA ',bg='yellow')
        self.labeltext.config(font='Arial 20 bold')
        self.labeltext.place(relx=0.35,rely=0.08)

    def imagem2(self):
        self.imagem2 = Image.open('bra1.png')
        self.tamanho = self.imagem2.resize((100,100),Image.ANTIALIAS)
        self.origem = ImageTk.PhotoImage(self.tamanho)

        self.ver = Label(self.janelaC,image=self.origem,bg='yellow',bd=4,relief=GROOVE)
        self.ver.place(relx=0.01,rely=0.02)

        self.linha = Label(self.janelaC,text='_'*272,bg='yellow')
        self.linha.place(relx=0.00,rely=0.24)


    def label_e_entry_cadastra_nome(self):
        self.labelnome = Label(self.janelaC,text='Nome',padx=11)
        self.labelnome.config(bd=4)
        self.labelnome.config(relief=GROOVE)
        self.labelnome.config(font='Calibri 18 bold')
        self.labelnome.place(relx=0.01,rely=0.35)

        self.entrynome = Entry(self.janelaC)
        self.entrynome.config(bd=4)
        self.entrynome.config(relief=GROOVE)
        self.entrynome.config(font='Calibri 18 bold')
        self.entrynome.place(relx=0.12,rely=0.35)

    def label_e_entry_cadastra_cpf(self):
        self.labelcpf = Label(self.janelaC, text='Cpf',padx=24)
        self.labelcpf.config(bd=4)
        self.labelcpf.config(relief=GROOVE)
        self.labelcpf.config(font='Calibri 18 bold')
        self.labelcpf.place(relx=0.01, rely=0.45)

        self.entrycpf = Entry(self.janelaC)
        self.entrycpf.config(bd=4)
        self.entrycpf.config(relief=GROOVE)
        self.entrycpf.config(font='Calibri 18 bold')
        self.entrycpf.place(relx=0.12, rely=0.45)

    def label_e_entry_cadastra_senha(self):
        self.labelsenha = Label(self.janelaC, text='Senha',padx=11)
        self.labelsenha.config(bd=4)
        self.labelsenha.config(relief=GROOVE)
        self.labelsenha.config(font='Calibri 18 bold')
        self.labelsenha.place(relx=0.01, rely=0.55)

        self.entrysenha = Entry(self.janelaC)
        self.entrysenha.config(bd=4)
        self.entrysenha.config(relief=GROOVE)
        self.entrysenha.config(font='Calibri 18 bold')
        self.entrysenha.place(relx=0.12, rely=0.55)

    def label_e_entry_cadastra_agencia(self):
        self.labelagencia = Label(self.janelaC, text='Agencia')
        self.labelagencia.config(bd=4)
        self.labelagencia.config(relief=GROOVE)
        self.labelagencia.config(font='Calibri 18 bold')
        self.labelagencia.place(relx=0.01, rely=0.65)

        self.entryagencia = Entry(self.janelaC)
        self.entryagencia.config(bd=4)
        self.entryagencia.config(relief=GROOVE)
        self.entryagencia.config(font='Calibri 18 bold')
        self.entryagencia.place(relx=0.12, rely=0.65)

    def botao_janelaC(self):
        self.passou = Button(self.janelaC, text='CONFIRMA')
        self.passou.bind('<Button>',self.destruir)
        self.passou.config(width=15)
        self.passou.config(height=1)
        self.passou.config(font='Arial 15 bold')
        self.passou.place(relx=0.40,rely=0.80)


    def destruir(self,*res):
        if self.entrynome.get() != '' and self.entrycpf.get() != '' and self.entrysenha.get() != '' and self.entryagencia.get() != '':
            pessoas = Pessoas(self.entrynome.get(),self.entrycpf.get(),self.entrysenha.get(),self.entryagencia.get())
            lista.append(pessoas)

            self.janelaC.destroy()
            self.origC.deiconify()
        else:
            messagebox.showerror('ERRO','preencha o espaço')


class SacarDinheiro:
    def __init__(self,master,origem):
        self.saque = master
        self.tela_sacar()

        self.btnsaque = Button(self.saque,text='wdwdd',command=self.funcao_des)
        self.btnsaque.pack()

        self.origem = origem

    def tela_sacar(self):
        self.saque.geometry('900x500')
        self.saque.state('zoomed')
        

    def funcao_des(self):
        self.saque.destroy()
        self.origem.deiconify()
        


class Principal:
    def __init__(self,master):
        self.janela = master
        self.janela['bg'] = 'yellow'
        self.tela()
        self.botao_deposito()
        self.botao_sacar()
        self.botao_transferencia()
        self.botao_abrir_conta()
        self.imagem()

    def botao_deposito(self):
        self.butao = Button(self.janela,text='DEPOSITO')
        self.butao.configure(width=25)
        self.butao.config(height=2)
        self.butao.config(bg='#0000CD')
        self.butao.config(font='Arial 10')
        self.butao.config(fg='white')
        self.butao.bind('<Button>',self.btn_fucao)
        self.butao.place(relx=0.01,rely=0.32)

    def botao_sacar(self):
        self.sacar = Button(self.janela,text='SACAR')
        self.sacar.configure(width=25)
        self.sacar.config(height=2)
        self.sacar.config(bg='#0000CD')
        self.sacar.config(font='Arial 10')
        self.sacar.config(fg='white')
        self.sacar.bind('<Button>',self.funcaoSacar)
        self.sacar.place(relx=0.01,rely=0.50)

    def botao_transferencia(self):
        self.trans = Button(self.janela,text='TRANSFERENCIA')
        self.trans.configure(width=25)
        self.trans.config(height=2)
        self.trans.config(bg='#0000CD')
        self.trans.config(font='Arial 10')
        self.trans.config(fg='white')
        #self.sacar.bind('<Button>',self.btn_fucao)
        self.trans.place(relx=0.01,rely=0.70)

    def botao_abrir_conta(self):

        self.butaoabrir = Button(self.janela,text='ABRIR CONTA')
        self.butaoabrir.config(bg='blue')
        self.butaoabrir.config(fg='white')
        self.butaoabrir.bind('<Button>',self.abrir_conta_do_usuario)
        self.butaoabrir.place(relx=0.90,rely=0.03)

    def tela(self):
        self.janela.state('zoomed')
        self.janela.geometry('1410x700+0+1')
        self.janela.title('BANCO DO BRASIL ')

    def imagem(self):
        self.imagem2 = Image.open('bra1.png')
        self.tamanho = self.imagem2.resize((100,100),Image.ANTIALIAS)
        self.origem = ImageTk.PhotoImage(self.tamanho)

        self.ver = Label(self.janela,image=self.origem,bg='yellow',bd=4,relief=GROOVE)
        self.ver.place(relx=0.01,rely=0.02)

        self.linha = Label(self.janela,text='_'*272,bg='yellow')
        self.linha.place(relx=0.00,rely=0.24)

    def abrir_conta_do_usuario(self,*res):
        self.janela.withdraw()
        self.janela3 = Toplevel(self.janela)
        Contas(self.janela3,self.janela)

    def funcaoSacar(self,*tr):
        self.janela.withdraw()
        self.pega = Toplevel(self.janela)
        SacarDinheiro(self.pega,self.janela)

    def btn_fucao(self,*v):
        if len(lista) > 0:
            self.janela.withdraw()
            self.janela02 = Toplevel(self.janela)
            JanelaPro(self.janela02,self.janela)
        else:
            ress = messagebox.askyesno('NÃO A CONTA CADASTRADA','CADASTRA UMA CONTA')
            if ress == TRUE:
                self.abrir_conta_do_usuario()


root = Tk()
Principal(root)
root.mainloop()