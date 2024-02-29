import tkinter as tk

def criar_conta():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    confirmar_senha = entrada_confirmar_senha.get()
    
    if usuario or senha == '':
        mensagem.config(text='Usuário ou senha estão em branco.')

    # Verifica se a senha e a confirmação de senha são iguais
    elif senha == confirmar_senha & senha != '':
        # Armazena os dados em um arquivo de texto simples
        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"{usuario}:{senha}\n")
        mensagem.config(text="Conta criada com sucesso!")
    else:
        mensagem.config(text="As senhas não correspondem!")

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Verifica se os dados de login estão corretos
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            dados = linha.split(":")
            if dados[0] == usuario and dados[1] == senha:
                mensagem.config(text=f"Olá {usuario}, seja bem vindo!")
                return
    mensagem.config(text="Usuário ou senha incorretos!")

janela = tk.Tk()
janela.title("Cadastro e Login")

# Criação dos widgets
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack()
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

label_confirmar_senha = tk.Label(janela, text="Confirmar senha:")
label_confirmar_senha.pack()
entrada_confirmar_senha = tk.Entry(janela, show="*")
entrada_confirmar_senha.pack()

botao_criar_conta = tk.Button(janela, text="Criar Conta", command=criar_conta)
botao_criar_conta.pack()

botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.pack()

mensagem = tk.Label(janela, text="")
mensagem.pack()

janela.mainloop()
