from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import string
import random
import os

# Cores
cor0 = "#444466"  # Preto
cor1 = "#feffff"  # Branco
cor3 = "#f05a43"  # Vermelho

# Função principal que inicia a janela principal
def abrir_janela_principal():
    splash.destroy()  # Fecha a tela de introdução
    janela = Tk()
    janela.title("Gerador de Senhas")
    janela.geometry("295x360")
    janela.configure(bg=cor1)

    # Estilo
    estilo = ttk.Style(janela)
    estilo.theme_use("clam")

    # Dividindo a janela
    frame_cima = Frame(janela, width=295, height=50, bg=cor1, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=295, height=310, bg=cor1, relief="flat")
    frame_baixo.grid(row=1, column=0, sticky=NSEW)

    # Imagem no frame superior
    if os.path.exists("password.png"):
        img = Image.open("password.png")
        img = img.resize((50, 50), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        app_logo = Label(frame_cima, image=img, bg=cor1, relief="flat")
        app_logo.image = img
        app_logo.place(x=0, y=-1)
    else:
        app_logo = Label(frame_cima, text="🔒", font=("Ivy 30 bold"), bg=cor1)
        app_logo.place(x=10, y=0)

    # Título e linha
    app_nome = Label(frame_cima, text="GERADOR DE SENHAS", font=("Ivy 16 bold"), bg=cor1, fg=cor0)
    app_nome.place(x=60, y=10)

    app_linha = Label(frame_cima, text="", width=295, height=1, bg=cor3)
    app_linha.place(x=0, y=40)

    # Função para gerar senha
    def criar_senha():
        global senha_gerada
        caracteres = ""
        if estado_1.get() == "True":
            caracteres += string.ascii_uppercase
        if estado_2.get() == "True":
            caracteres += string.ascii_lowercase
        if estado_3.get() == "True":
            caracteres += string.digits
        if estado_4.get() == "True":
            caracteres += string.punctuation

        tamanho = var.get()
        if tamanho == 0 or not caracteres:
            messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere e defina o tamanho maior que zero.")
            return

        senha_gerada = "".join(random.sample(caracteres, tamanho))
        app_senha["text"] = senha_gerada

    # Função para copiar senha
    def copiar_senha():
        if app_senha["text"] != "- - -":
            janela.clipboard_clear()
            janela.clipboard_append(app_senha["text"])
            janela.update()
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Gere uma senha antes de copiá-la.")

    # Frame inferior - senha gerada
    app_senha = Label(
    frame_baixo,
    text="- - -",
    width=25,  # Aumentar a largura para acomodar até 20 caracteres
    height=2,
    relief="solid",
    font=("Ivy 10 bold"),  # Fonte menor para evitar excesso de espaço ocupado
    bg=cor1,
    fg=cor0,
    anchor="center"  # Centralizar o texto
)
    app_senha.grid(row=0, column=0, columnspan=2, pady=10)


    # Frame inferior - configurações
    app_info = Label(frame_baixo, text="Número total de caracteres na senha", font=("Ivy 10 bold"), bg=cor1, fg=cor0)
    app_info.grid(row=1, column=0, columnspan=2)

    var = IntVar(value=8)
    spin = Spinbox(frame_baixo, from_=1, to=20, textvariable=var, width=5)
    spin.grid(row=2, column=0, pady=8)

    frame_caracteres = Frame(frame_baixo, bg=cor1)
    frame_caracteres.grid(row=3, column=0, columnspan=2)

    # Configuração dos tipos de caracteres
    estado_1 = StringVar(value="False")
    estado_2 = StringVar(value="False")
    estado_3 = StringVar(value="False")
    estado_4 = StringVar(value="False")

    Checkbutton(frame_caracteres, text="ABC Maiúsculas", variable=estado_1, onvalue="True", offvalue="False", bg=cor1).grid(row=0, column=0, sticky=W)
    Checkbutton(frame_caracteres, text="abc Minúsculas", variable=estado_2, onvalue="True", offvalue="False", bg=cor1).grid(row=1, column=0, sticky=W)
    Checkbutton(frame_caracteres, text="123 Números", variable=estado_3, onvalue="True", offvalue="False", bg=cor1).grid(row=2, column=0, sticky=W)
    Checkbutton(frame_caracteres, text="!@# Símbolos", variable=estado_4, onvalue="True", offvalue="False", bg=cor1).grid(row=3, column=0, sticky=W)

    # Botões
    botao_gerar = Button(frame_baixo, text="Gerar Senha", command=criar_senha, bg=cor3, fg=cor1, font=("Ivy 10 bold"))
    botao_gerar.grid(row=4, column=0, columnspan=2, pady=10)

    botao_copiar = Button(frame_baixo, text="Copiar", command=copiar_senha, bg=cor1, fg=cor0, font=("Ivy 10 bold"))
    botao_copiar.grid(row=0, column=1, sticky=E, padx=10)

    janela.mainloop()

# Splash Screen
splash = Tk()
splash.title("Bem-vindo")
splash.geometry("300x200")
splash.configure(bg=cor1)

Label(splash, text="Bem-vindo ao Gerador de Senhas!", font=("Ivy 14 bold"), bg=cor1, fg=cor0).pack(expand=True)
splash.after(3000, abrir_janela_principal)  # Abre a janela principal após 3 segundos

splash.mainloop()
