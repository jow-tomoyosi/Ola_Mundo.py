import tkinter as tk
from math import sqrt

def adicionar_caractere(caractere):
    entrada.insert(tk.END, caractere)

def limpar():
    entrada.delete(0, tk.END)
    resultado.config(text="Resultado: ")

def calcular():
    try:
        expressao = entrada.get()
        resultado_calculo = eval(expressao)
        resultado.config(text=f"Resultado: {resultado_calculo}")
    except Exception as e:
        resultado.config(text="Erro!")

janela = tk.Tk()
janela.title("Calculadora")
janela.resizable(False, False)

# Definir estilo para os botões
botao_estilo = {
    "padx": 16,
    "pady": 8,
    "width": 3,
    "font": ("Arial", 12)
}

# Criação dos widgets
entrada = tk.Entry(janela, font=("Arial", 14), width=15, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botao_7 = tk.Button(janela, text="7", **botao_estilo, command=lambda: adicionar_caractere("7"))
botao_7.grid(row=1, column=0)

botao_8 = tk.Button(janela, text="8", **botao_estilo, command=lambda: adicionar_caractere("8"))
botao_8.grid(row=1, column=1)

botao_9 = tk.Button(janela, text="9", **botao_estilo, command=lambda: adicionar_caractere("9"))
botao_9.grid(row=1, column=2)

botao_divisao = tk.Button(janela, text="/", **botao_estilo, command=lambda: adicionar_caractere("/"))
botao_divisao.grid(row=1, column=3)

botao_4 = tk.Button(janela, text="4", **botao_estilo, command=lambda: adicionar_caractere("4"))
botao_4.grid(row=2, column=0)

botao_5 = tk.Button(janela, text="5", **botao_estilo, command=lambda: adicionar_caractere("5"))
botao_5.grid(row=2, column=1)

botao_6 = tk.Button(janela, text="6", **botao_estilo, command=lambda: adicionar_caractere("6"))
botao_6.grid(row=2, column=2)

botao_multiplicacao = tk.Button(janela, text="X", **botao_estilo, command=lambda: adicionar_caractere("*"))
botao_multiplicacao.grid(row=2, column=3)

botao_1 = tk.Button(janela, text="1", **botao_estilo, command=lambda: adicionar_caractere("1"))
botao_1.grid(row=3, column=0)

botao_2 = tk.Button(janela, text="2", **botao_estilo, command=lambda: adicionar_caractere("2"))
botao_2.grid(row=3, column=1)

botao_3 = tk.Button(janela, text="3", **botao_estilo, command=lambda: adicionar_caractere("3"))
botao_3.grid(row=3, column=2)

botao_subtracao = tk.Button(janela, text="-", **botao_estilo, command=lambda: adicionar_caractere("-"))
botao_subtracao.grid(row=3, column=3)

botao_0 = tk.Button(janela, text="0", **botao_estilo, command=lambda: adicionar_caractere("0"))
botao_0.grid(row=4, column=1)

botao_ponto = tk.Button(janela, text=".", **botao_estilo, command=lambda: adicionar_caractere("."))
botao_ponto.grid(row=4, column=0)

botao_raiz_quadrada = tk.Button(janela, text="√", **botao_estilo, command=lambda: adicionar_caractere("sqrt("))
botao_raiz_quadrada.grid(row=4, column=2)

botao_soma = tk.Button(janela, text="+", **botao_estilo, command=lambda: adicionar_caractere("+"))
botao_soma.grid(row=4, column=3)

botao_limpar = tk.Button(janela, text="C", **botao_estilo, command=limpar)
botao_limpar.grid(row=5, column=0)

botao_porcentagem = tk.Button(janela, text="%", **botao_estilo, command=lambda: adicionar_caractere("%"))
botao_porcentagem.grid(row=5, column=1)

botao_igual = tk.Button(janela, text="=", **botao_estilo, command=calcular)
botao_igual.grid(row=5, column=2)

resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12), anchor="e")
resultado.grid(row=5, column=3, padx=10, pady=10)

janela.mainloop()
