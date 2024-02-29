import requests
from tkinter import *

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()

def cotacao_euro():
    cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
    
    texto_resposta['text'] = f'Euro: {cotacao_euro:.2f}'
    
def cotacao_btc():
    cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])
    
    texto_resposta['text'] = f'BTC: {cotacao_btc:.2f}'
    
def cotacao_dolar():
    cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
    
    texto_resposta['text'] = f'Dólar: {cotacao_dolar:.2f}'
    
def pegar_cotacoes():
    cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
    cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])
    cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])

    texto_resposta['text'] = f'''Euro: {cotacao_euro:.2f}\nDólar: {cotacao_dolar:.2f}\nBTC: {cotacao_btc:.2f}'''

janela = Tk()
janela.configure(background='#042527') 
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas", font='Arial', fg='#c2ff01', bg='#042527')
texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

botao = Button(janela, text="Buscar todas cotações", command=pegar_cotacoes, font='Arial', fg='#c2ff01', bg='#042527')
botao.grid(row=1, column=0, padx=10)

botao_euro = Button(janela, text="Buscar Euro", command=cotacao_euro, font='Arial', fg='#c2ff01', bg='#042527')
botao_euro.grid(row=1, column=1, padx=10)

botao_btc = Button(janela, text="Buscar BTC", command=cotacao_btc, font='Arial', fg='#c2ff01', bg='#042527')
botao_btc.grid(row=1, column=2, padx=10)

botao_dolar = Button(janela, text="Buscar Dólar", command=cotacao_dolar, font='Arial', fg='#c2ff01', bg='#042527')
botao_dolar.grid(row=1, column=3, padx=10)

texto_resposta = Label(janela, text="", font='Arial', fg='#c2ff01', bg='#042527')
texto_resposta.grid(row=2, column=0, columnspan=4, pady=10)

botao_fechar = Button(janela, text="Fechar", command=janela.destroy, font='Arial', fg='#c2ff01', bg='#042527')
botao_fechar.grid(row=3, column=0, columnspan=4, pady=10)


janela.mainloop()