import tkinter as tk
import requests

def buscar_cep():
    cep = entrada_cep.get()

    # Faz a requisição à API ViaCEP
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            resultado.config(text=f"CEP: {dados['cep']}\n"
                                  f"Endereço: {dados['logradouro']}\n"
                                  f"Complemento: {dados['complemento']}\n"
                                  f"Bairro: {dados['bairro']}\n"
                                  f"Cidade: {dados['localidade']}\n"
                                  f"Estado: {dados['uf']}")
        else:
            resultado.config(text="CEP não encontrado.")
    else:
        resultado.config(text="Erro ao fazer a requisição.")

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Consulta de CEP")

# Criação dos widgets
label_cep = tk.Label(janela, text="Digite o CEP")
label_cep.pack()
entrada_cep = tk.Entry(janela)
entrada_cep.pack()

botao_buscar = tk.Button(janela, text="Buscar", command=buscar_cep)
botao_buscar.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

botao_sair = tk.Button(janela, text="Fechar", command=janela.destroy)
botao_sair.pack()

janela.mainloop()
