import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

LARGEFONT = ("Verdana", 35)
entryFont = ("Verdana", 25)
titleEntryFont = ("Verdana", 15)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.listaComprasNomes = []
        self.listaComprasPrecos = []
        self.usuario = ""
        container = tk.Frame(self, background="#1e272e")
        self.geometry("1000x800")
        self.state("zoomed")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Add all frames to the application
        for F in (StartPage, Buy, PaginaPrincipal, Entradas, PratosPrincipais, Bebidas, BebidasAlcoolicas, MenuDoChef, Sobremesas):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]

        # Check if the frame is PaginaPrincipal and call update_user_label method
        if cont == PaginaPrincipal:
            frame.update_user_label()

        frame.tkraise()

    def getUser(self):
        return self.usuario

    def buyItem(self, nome, preco):
        self.listaComprasNomes.append(nome)
        self.listaComprasPrecos.append(preco)

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

        # Set the username after successful login
        self.usuario = loginCheck
        print(self.usuario)

        self.show_frame(PaginaPrincipal)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#1e272e")

        titulo = ttk.Label(self, text="Restaurante do Ederson", font=LARGEFONT, anchor="center", justify="center", background="#1e272e", foreground="white")
        titulo.pack(anchor="center")

        tituloLogin = ttk.Label(self, text="Login", font=titleEntryFont, anchor="center", justify="center", background="#1e272e", foreground="white")
        tituloLogin.pack(anchor="center")
        login = ttk.Entry(self, font=entryFont)
        login.pack(anchor="center")

        tituloSenha = ttk.Label(self, text="Senha", font=titleEntryFont, anchor="center", justify="center", background="#1e272e", foreground="white")
        tituloSenha.pack(anchor="center")
        senha = ttk.Entry(self, font=entryFont, show="*")
        senha.pack(anchor="center")

        tituloConfirmarSenha = ttk.Label(self, text="Confirme a senha", font=titleEntryFont, anchor="center", justify="center", background="#1e272e", foreground="white")
        tituloConfirmarSenha.pack(anchor="center")
        confirmarSenha = ttk.Entry(self, font=entryFont, show="*")
        confirmarSenha.pack(anchor="center")

        button1 = ttk.Button(self, text="Login",
                             command=lambda: controller.login(login, senha, confirmarSenha))
        button1.pack(anchor="center", pady=10)

# second window frame page1 
class Buy(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Buy))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(PaginaPrincipal))	
		button2.pack(anchor='center')
class PaginaPrincipal(tk.Frame):
	def __init__(self, parent, controller):
		self.image_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Imagens")  # Caminho atual de aonde as imagens estão.
		tk.Frame.__init__(self, parent, background="#1e272e")
		self.controller = controller

		titulo = ttk.Label(self, text="Restaurante do Ederson", font=LARGEFONT, anchor="center", justify="center", background="#1e272e", foreground="white")
		titulo.pack(anchor="center")

			# Create a label for user greeting but don't set text yet
		self.user_label = ttk.Label(self, text="", font=titleEntryFont, anchor="center", justify="center", background="#1e272e", foreground="white")
		self.user_label.pack(anchor="center")
		
		comidas = tk.Frame(self,background='#1e272e')
		comidas.pack(side = "top", fill = "both", expand = True,anchor='center',padx= 580,pady=200)

		#Entradas
		image_path = os.path.join(self.image_folder, "cuzcuzPaulistaEntradaThumbnail.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgEntradas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgEntradas.image = photo
		imgEntradas.grid(row=0,column=0)
		btEntradas = ttk.Button(comidas, text ="Entradas",
		command = lambda : controller.show_frame(Entradas))
		btEntradas.grid(row=1,column=0)

		#Pratos principais
		image_path = os.path.join(self.image_folder, "harkarlPratosPrincipaisThumbnail.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgPratosPrincipais = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgPratosPrincipais.image = photo
		imgPratosPrincipais.grid(row=0,column=1,padx= 10)
		btPratosPrincipais = ttk.Button(comidas, text ="Pratos Principais",
		command = lambda : controller.show_frame(PratosPrincipais))
		btPratosPrincipais.grid(row=1,column=1)
		
		#Bebibas
		image_path = os.path.join(self.image_folder, "tomatoJuiceBebidasThumbnail.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgBebibas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgBebibas.image = photo
		imgBebibas.grid(row=0,column=2)
		btBebidas = ttk.Button(comidas, text ="Bebidas",
		command = lambda : controller.show_frame(Bebidas))
		btBebidas.grid(row=1,column=2)
		
		#Bebibas Alcoolicas
		image_path = os.path.join(self.image_folder, "wasabiBebibasAlcoolicasThumbnail.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgBebibasAlcoolicas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgBebibasAlcoolicas.image = photo
		imgBebibasAlcoolicas.grid(row=3,column=0)
		btBebidasAlcoolicas = ttk.Button(comidas, text ="Bebidas Alcoólicas",
		command = lambda : controller.show_frame(BebidasAlcoolicas))
		btBebidasAlcoolicas.grid(row=4,column=0)
		
		#Sobremesas
		image_path = os.path.join(self.image_folder, "doceSobremesasThumbnail.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgSobremesas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgSobremesas.image = photo
		imgSobremesas.grid(row=3,column=1,padx= 10)
		btSobremesas = ttk.Button(comidas, text ="Sobremesas",
		command = lambda : controller.show_frame(Sobremesas))
		btSobremesas.grid(row=4,column=1)

		#Menu do chef
		image_path = os.path.join(self.image_folder, "chefThumbnail.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgChef = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgChef.image = photo
		imgChef.grid(row=3,column=2)
		btChef = ttk.Button(comidas, text ="Menu do Chef",
		command = lambda : controller.show_frame(MenuDoChef))
		btChef.grid(row=4,column=2)
            
	def update_user_label(self):
		"""Update the user label with the current user's name."""
		user_name = self.controller.getUser()
		self.user_label.config(text=f"Olá {user_name} !")
# entradas, pratos principais, bebidas, bebidas alcoólicas, sobremesas, menu do chef. 
class Entradas(tk.Frame): 
	def __init__(self, parent, controller):
		
		self.image_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Imagens") # Caminho atual de aonde as imagens estão.
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')
		btVoltar = ttk.Button(self, text ="Voltar",
		command = lambda : controller.show_frame(PaginaPrincipal))
		btVoltar.pack(anchor='center')
		btBuy = ttk.Button(self, text ="Carrinho",
		command = lambda : controller.show_frame(Buy))
		btBuy.pack(anchor='center')
		
		comidas = tk.Frame(self,background='#1e272e')
		comidas.pack(side = "top", fill = "both", expand = True,anchor='center',padx= 580,pady=100)

		#Entradas
		image_path = os.path.join(self.image_folder, "entrada1.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgEntradas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgEntradas.image = photo
		imgEntradas.grid(row=0,column=0)
		btEntradas = ttk.Button(comidas, text ="Purê de Batata com Blueberry e Torrada",
		command = lambda : controller.show_frame(Entradas))
		btEntradas.grid(row=1,column=0)

		#Pratos principais
		image_path = os.path.join(self.image_folder, "entrada2.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgPratosPrincipais = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgPratosPrincipais.image = photo
		imgPratosPrincipais.grid(row=0,column=1,padx= 10)
		btPratosPrincipais = ttk.Button(comidas, text ="Lagosta anã laranja",
		command = lambda : controller.show_frame(PratosPrincipais))
		btPratosPrincipais.grid(row=1,column=1)
		
		#Bebibas
		image_path = os.path.join(self.image_folder, "entrada3.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgBebibas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgBebibas.image = photo
		imgBebibas.grid(row=0,column=2)
		btBebidas = ttk.Button(comidas, text ="Queijo com Queijo e Vermelho",
		command = lambda : controller.show_frame(Bebidas))
		btBebidas.grid(row=1,column=2)
		
		#Bebibas Alcoolicas
		image_path = os.path.join(self.image_folder, "entrada4.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgBebibasAlcoolicas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgBebibasAlcoolicas.image = photo
		imgBebibasAlcoolicas.grid(row=3,column=0)
		btBebidasAlcoolicas = ttk.Button(comidas, text ="Torrada de Tomate e Berinjela",
		command = lambda : controller.show_frame(BebidasAlcoolicas))
		btBebidasAlcoolicas.grid(row=4,column=0)
		
		#Sobremesas
		image_path = os.path.join(self.image_folder, "entrada5.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgSobremesas = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgSobremesas.image = photo
		imgSobremesas.grid(row=3,column=1,padx= 10)
		btSobremesas = ttk.Button(comidas, text ="Bomba de Chocolate",
		command = lambda : controller.show_frame(Sobremesas))
		btSobremesas.grid(row=4,column=1)

		#Menu do chef
		image_path = os.path.join(self.image_folder, "entrada6.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgChef = tk.Label(comidas, image=photo, bg="gray", bd=0)
		imgChef.image = photo
		imgChef.grid(row=3,column=2)
		btChef = ttk.Button(comidas, text ="Coxinha de Frango",
		command = lambda : controller.show_frame(MenuDoChef))
		btChef.grid(row=4,column=2)

class PratosPrincipais(tk.Frame): 
	def __init__(self, parent, controller):
		
		self.image_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Imagens") # Caminho atual de aonde as imagens estão.
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')
		btVoltar = ttk.Button(self, text ="Voltar",
		command = lambda : controller.show_frame(PaginaPrincipal))
		btVoltar.pack(anchor='center')
		btBuy = ttk.Button(self, text ="Carrinho",
		command = lambda : controller.show_frame(Buy))
		btBuy.pack(anchor='center')
		
		comidas = tk.Frame(self,background='#1e272e')
		comidas.pack(side = "top", fill = "both", expand = True,anchor='center',padx= 580,pady=100)

		#Entradas
		image_path = os.path.join(self.image_folder, "pratoprin1.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgEntradas = tk.Label(comidas, image=photo, bg="#1e272e", bd=0)
		imgEntradas.image = photo
		imgEntradas.grid(row=0,column=0)
		btEntradas = ttk.Button(comidas, text ="Ovo Milenar",
		command = lambda : controller.show_frame(Entradas))
		btEntradas.grid(row=1,column=0)

		#Pratos principais
		image_path = os.path.join(self.image_folder, "pratoprin2.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgPratosPrincipais = tk.Label(comidas, image=photo, bg="#1e272e", bd=0)
		imgPratosPrincipais.image = photo
		imgPratosPrincipais.grid(row=0,column=1,padx= 10)
		btPratosPrincipais = ttk.Button(comidas, text ="Banana de Pizza",
		command = lambda : controller.show_frame(PratosPrincipais))
		btPratosPrincipais.grid(row=1,column=1)
		
		#Bebibas
		image_path = os.path.join(self.image_folder, "pratoprin3.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgBebibas = tk.Label(comidas, image=photo, bg="#1e272e", bd=0)
		imgBebibas.image = photo
		imgBebibas.grid(row=0,column=2)
		btBebidas = ttk.Button(comidas, text ="Pizzamburguer",
		command = lambda : controller.show_frame(Bebidas))
		btBebidas.grid(row=1,column=2)
		
		#Bebibas Alcoolicas
		image_path = os.path.join(self.image_folder, "pratoprin4.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgBebibasAlcoolicas = tk.Label(comidas, image=photo, bg="#1e272e", bd=0)
		imgBebibasAlcoolicas.image = photo
		imgBebibasAlcoolicas.grid(row=3,column=0)
		btBebidasAlcoolicas = ttk.Button(comidas, text ="Peixe extremamente venenoso",
		command = lambda : controller.show_frame(BebidasAlcoolicas))
		btBebidasAlcoolicas.grid(row=4,column=0)
		
		#Sobremesas
		image_path = os.path.join(self.image_folder, "pratoprin5.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgSobremesas = tk.Label(comidas, image=photo, bg="#1e272e", bd=0)
		imgSobremesas.image = photo
		imgSobremesas.grid(row=3,column=1,padx= 10)
		btSobremesas = ttk.Button(comidas, text ="Lula Crua",
		command = lambda : controller.show_frame(Sobremesas))
		btSobremesas.grid(row=4,column=1)

		#Menu do chef
		image_path = os.path.join(self.image_folder, "pratoprin6.png")
		img = Image.open(image_path)
		img.thumbnail((250, 250))
		photo = ImageTk.PhotoImage(img)
		imgChef = tk.Label(comidas, image=photo, bg="#1e272e", bd=0)
		imgChef.image = photo
		imgChef.grid(row=3,column=2)
		btChef = ttk.Button(comidas, text ="Lasagna",
		command = lambda : controller.show_frame(MenuDoChef))
		btChef.grid(row=4,column=2)

class Bebidas(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Buy))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(PaginaPrincipal))	
		button2.pack(anchor='center')

class BebidasAlcoolicas(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Buy))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(PaginaPrincipal))	
		button2.pack(anchor='center')

class Sobremesas(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Buy))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(PaginaPrincipal))	
		button2.pack(anchor='center')

class MenuDoChef(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,background='#1e272e')
		
		titulo = ttk.Label(self, text ="Restaurante do Ederson", font = LARGEFONT,anchor="center",justify='center',background='#1e272e',foreground='white')		
		titulo.pack(anchor='center')

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Buy))	
		button1.pack(anchor='center')

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(PaginaPrincipal))	
		button2.pack(anchor='center')







app = tkinterApp()
app.mainloop()
