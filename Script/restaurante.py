import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

# O desafio consiste em criar uma (ou mais telas) para um sistemas de pedido do restaurante do Ederson.
# Para começar o sistema, é solicitado que ele digite um usuário e uma senha, a senha deve ser confirmada em um campo com confirmação de senha e deve seguir as mesmas normas do exercício anterior.
# Depois do login deve ser possível ao usuário entrar na tela inicial onde ele pode começar o processo para fazer seus pedidos, na tela inicial deve conter a mensagem "Olá, {nome_usuário}" e abaixo as opções do restaurante, as opções possíveis são: entradas, pratos principais, bebidas, bebidas alcoólicas, sobremesas, menu do chef.
# Cada botão que a pessoa clicar deve redirecionar a tela para o campo com opções variadas de produtos (no mínimo 5) para ser selecionada pelo usuário, a pessoa pode adicionar tudo no pedido dela clicando em um botão para adicionar ao pedido (use a criatividade para criar esse botão) e ao final da tela deve ter a opção de finalizar o pedido para que a pessoa possa visualizar tudo o que foi colocado no carrinho até agora e confirme se está tudo certo, caso esteja ela envia o pedido a cozinha, e finaliza o sistema com uma imagem divertida, caso não ela deve ter a opção de acrescentar mais itens ao pedido ou retirar os mesmos que já estejam lá.

LARGEFONT =("Verdana", 35)
entryFont =("Verdana", 25)
titleEntryFont = ("Verdana", 15)
class tkinterApp(tk.Tk):
	
	def __init__(self, *args, **kwargs): 
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self,background='#1e272e') 
		self.geometry("800x600")
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {} 

		for F in (StartPage, Page1, Page2):

			frame = F(container, self)
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
	
	def login(self, login, senha, confirmarSenha):		
		loginCheck = login.get()
		senhaCheck = senha.get()
		senhaConfirmCheck = confirmarSenha.get()		
		if loginCheck == "":
			messagebox.showerror("Erro", "Login está vazio")
			return
			
		if senhaCheck == "":
			messagebox.showerror("Erro", "Senha está vazio")
			return
		
		if senhaConfirmCheck != senhaCheck:
			messagebox.showerror("Erro", "Senha não é igual a confirmação de senha")
			return
		
		if senhaCheck == loginCheck:
			messagebox.showerror("Erro", "Login e senha não podem ser os mesmos")
			return
		
		if loginCheck != "suporte":
			messagebox.showerror("Erro", "Conta não achada.")
			return
		if senhaCheck != "senha":
			messagebox.showerror("Erro", "Conta não achada.")
			return
		if senhaConfirmCheck != "senha":
			messagebox.showerror("Erro", "Conta não achada.")
			return
					
		
		tkinterApp.show_frame(self,Page1)

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		tituloLogin = ttk.Label(self, text ="Login", font = titleEntryFont,anchor="center",justify='center',background='#1e272e',foreground='white')		
		tituloLogin.pack(anchor='center')
		login = ttk.Entry(self,font=entryFont)
		login.pack(anchor='center')

		tituloSenha = ttk.Label(self, text ="Senha", font = titleEntryFont,anchor="center",justify='center',background='#1e272e',foreground='white')		
		tituloSenha.pack(anchor='center')
		senha = ttk.Entry(self,font=entryFont)
		senha.pack(anchor='center')

		tituloConfirmarSenha = ttk.Label(self, text ="Confirme a senha", font = titleEntryFont,anchor="center",justify='center',background='#1e272e',foreground='white')		
		tituloConfirmarSenha.pack(anchor='center')
		confirmarSenha = ttk.Entry(self,font=entryFont)
		confirmarSenha.pack(anchor='center')

		button1 = ttk.Button(self, text ="Login",
		command = lambda : controller.login(login, senha, confirmarSenha))
		button1.pack(anchor='center',pady=10)

		# button2 = ttk.Button(self, text ="Page 2",
		# command = lambda : controller.show_frame(Page2))	
		# button2.pack(anchor='center')
		


# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))	
		button2.pack(anchor='center')




# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))	
		button2.pack(anchor='center')


# Driver Code
app = tkinterApp()
app.mainloop()
