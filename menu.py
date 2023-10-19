import tkinter as tk
from tkinter import ttk
import pickle
import os

# Lista para armazenar os produtos
produtos = []

# Função para salvar os produtos em um arquivo pkl
def salvar_produtos():
    with open('produtos.pkl', 'wb') as file:
        pickle.dump(produtos, file)
    print("Produtos salvos em produtos.pkl")

# Função para carregar produtos do arquivo pkl ou criar um novo arquivo se ele não existir
def carregar_produtos():
    try:
        if os.path.exists('produtos.pkl'):
            with open('produtos.pkl', 'rb') as file:
                produtos.extend(pickle.load(file))
                print("Produtos carregados de produtos.pkl")
    except (EOFError, FileNotFoundError):
        print("Nenhum arquivo de produtos encontrado ou arquivo vazio. Um novo arquivo 'produtos.pkl' será criado.")

def cadastro():
    def salvar_produto():
        categoria = category_var.get()
        nome = name_var.get()
        produtos.append({"Categoria": categoria, "Nome": nome})
        print("Produto cadastrado:", produtos[-1])
        form.destroy()

    # Função para abrir o formulário de cadastro
    form = tk.Toplevel(root)
    form.title("Cadastro de Produto")

    # Crie um rótulo para a categoria
    category_label = ttk.Label(form, text="Categoria do Produto:")
    category_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Crie uma lista de opções para a categoria
    categories = [
        "Fertilizantes",
        "Herbicidas",
        "Inseticida",
        "Fungicida",
        "Fertilizante Foliar",
        "Bioestimulante",
        "Sementes",
        "Tratamento de Sementes"
    ]
    category_var = tk.StringVar()
    category_var.set(categories[0])
    category_option_menu = ttk.OptionMenu(form, category_var, *categories)
    category_option_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Crie um rótulo para o nome do produto
    name_label = ttk.Label(form, text="Nome do Produto:")
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # Crie uma entrada de texto para o nome do produto
    name_var = tk.StringVar()
    name_entry = ttk.Entry(form, textvariable=name_var)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    # Crie um botão para salvar o produto
    save_button = ttk.Button(form, text="Salvar", command=salvar_produto)
    save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Cria a janela principal
root = tk.Tk()
root.title("Sistema de Estoque")

# Carrega produtos do arquivo pkl ou cria um novo arquivo se ele não existir
carregar_produtos()

# Cria um menu
menu_bar = tk.Menu(root)

# Adiciona o primeiro item de menu (logo)
# Você pode substituir 'file.png' pelo caminho da sua imagem de logo, se tiver uma.
menu_bar.add_command(label="Logo", command=lambda: None)

# Cria a guia "Produtos" com os sub-menus
produtos_menu = tk.Menu(menu_bar, tearoff=0)
produtos_menu.add_command(label="Cadastro", command=cadastro)
produtos_menu.add_command(label="Entrada", command=lambda: None)
produtos_menu.add_command(label="Saída", command=lambda: None)
produtos_menu.add_command(label="Consultar Produtos", command=lambda: None)

menu_bar.add_cascade(label="Produtos", menu=produtos_menu)

# Define o menu na janela
root.config(menu=menu_bar)

# Inicia o loop principal
root.mainloop()
