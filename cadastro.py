import tkinter as tk
from tkinter import messagebox
import os
import pickle

# Função para registrar um novo usuário
def registrar_usuario():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario and senha:
        if os.path.exists('usuarios.pkl'):
            with open('usuarios.pkl', 'rb') as file:
                usuarios_registrados = pickle.load(file)
                if usuario in usuarios_registrados:
                    messagebox.showerror('Erro', 'Usuário já existe!')
                else:
                    usuarios_registrados[usuario] = senha
                    with open('usuarios.pkl', 'wb') as file:
                        pickle.dump(usuarios_registrados, file)
                    messagebox.showinfo('Sucesso', 'Usuário registrado com sucesso!')
        else:
            usuarios_registrados = {usuario: senha}
            with open('usuarios.pkl', 'wb') as file:
                pickle.dump(usuarios_registrados, file)
            messagebox.showinfo('Sucesso', 'Usuário registrado com sucesso!')
    else:
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')

# Cria a janela
root = tk.Tk()
root.title('Cadastro de Usuário')

# Define o tamanho da janela
root.geometry('400x300')

# Define um plano de fundo
background_image = tk.PhotoImage(file='background.png') if os.path.exists('background.png') else None
if background_image:
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
else:
    root.configure(bg='white')

# Cria campos de usuário e senha
label_usuario = tk.Label(root, text='Usuário:')
label_senha = tk.Label(root, text='Senha:')
entry_usuario = tk.Entry(root)
entry_senha = tk.Entry(root, show='*')

label_usuario.pack(pady=10)
entry_usuario.pack(pady=10)
label_senha.pack(pady=10)
entry_senha.pack(pady=10)

# Cria o botão de registro
registrar_button = tk.Button(root, text='Registrar', command=registrar_usuario)
registrar_button.pack(pady=10)

root.mainloop()
