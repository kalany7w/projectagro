import tkinter as tk
from tkinter import messagebox
import os
import pickle
import subprocess

# Função para verificar o login e abrir o arquivo menu.py
def verificar_login_e_abrir_menu():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if os.path.exists('usuarios.pkl'):
        with open('usuarios.pkl', 'rb') as file:
            usuarios_registrados = pickle.load(file)
            if usuario in usuarios_registrados and usuarios_registrados[usuario] == senha:
                messagebox.showinfo('Sucesso', 'Login bem-sucedido!')
                # Abrir o arquivo menu.py
                subprocess.Popen(['python', 'menu.py'])
            else:
                messagebox.showerror('Erro', 'Usuário ou senha incorretos!')
    else:
        messagebox.showerror('Erro', 'Nenhum usuário registrado.')

# Cria a janela
root = tk.Tk()
root.title('Tela de Login')

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

# Cria o botão de login
login_button = tk.Button(root, text='Login', command=verificar_login_e_abrir_menu)
login_button.pack(pady=10)

root.mainloop()
