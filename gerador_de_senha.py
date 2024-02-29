import tkinter as tk
import random
import pyperclip

def gerar_senha():
    tamanho_senha = int(entrada_tamanho_senha.get())
    senha = minu + mai + num + simb
    gerador = random.sample(senha, tamanho_senha)
    senha_gerada = ''.join(gerador)
    resultado.config(text="Senha: " + senha_gerada)
    pyperclip.copy(senha_gerada)  

janela = tk.Tk()
janela.geometry("400x150")
janela.title("Gerador de senha")

minu = "abcdefghijklmnopqrstuvwxyz"
mai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
simb = "!@#$%&"

label_senha = tk.Label(janela, text="Quantidade de dígitos:")
label_senha.pack()
entrada_tamanho_senha = tk.Entry(janela)
entrada_tamanho_senha.pack()

botao_gerar = tk.Button(janela, text="Gerar senha", command=gerar_senha)
botao_gerar.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

botao_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
botao_fechar.pack()

janela.mainloop()