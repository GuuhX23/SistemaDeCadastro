import tkinter as tk
from tkinter import ttk, messagebox

# Função para adicionar o produto
def adicionar_produto():
    nome_produto = entrada_nome.get()
    preco_produto = entrada_preco.get()
    quantidade_produto = entrada_quantidade.get()

    if nome_produto == "" or preco_produto == "" or quantidade_produto == "":
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos!")
    else:
        # Adiciona produto na lista
        lista_produtos.insert(tk.END, f"Produto: {nome_produto}, Preço: R${preco_produto}, Quantidade: {quantidade_produto}")
        # Limpa os campos de entrada
        entrada_nome.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Produtos")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

# Título da janela
titulo = tk.Label(janela, text="Cadastro de Produtos", font=("Arial", 16), bg="#F0F0F0")
titulo.pack(pady=10)

# Entrada de Nome do Produto
label_nome = tk.Label(janela, text="Nome do Produto:", bg="#F0F0F0")
label_nome.pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Entrada de Preço do Produto
label_preco = tk.Label(janela, text="Preço do Produto:", bg="#F0F0F0")
label_preco.pack()
entrada_preco = tk.Entry(janela, width=40)
entrada_preco.pack(pady=5)

# Entrada de Quantidade do Produto
label_quantidade = tk.Label(janela, text="Quantidade do Produto:", bg="#F0F0F0")
label_quantidade.pack()
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack(pady=5)

# Botão para adicionar o produto
botao_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
botao_adicionar.pack(pady=10)

# Lista para exibir os produtos cadastrados
lista_produtos = tk.Listbox(janela, width=50, height=10)
lista_produtos.pack(pady=10)

# Executa a interface
janela.mainloop()