import os
import requests
import csv
import tkinter as tk
from tkinter import messagebox

def executar_codigo():
    # Endereço da API
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

    # Chamada à API
    resposta = requests.get(url)

    # Decodificação da resposta
    dados = resposta.json()

    try:
        # Obter o caminho da área de trabalho
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

        # Criação do arquivo CSV na área de trabalho
        with open(os.path.join(desktop_path, "dados.csv"), "w", newline="") as arquivo:
            # Escrita dos dados no arquivo CSV
            escritor = csv.writer(arquivo)
            escritor.writerow(["success", "deck_id", "remaining", "shuffled"])

            # Adicionando dados ao arquivo CSV
            escritor.writerow([dados["success"], dados["deck_id"], dados["remaining"], dados["shuffled"]])

        messagebox.showinfo("Concluído", "Código executado com sucesso! Dados salvos em dados.csv na área de trabalho")

        # Fechar a janela após a mensagem de sucesso
        root.destroy()

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Executar Código")

# Botão para executar o código
botao_executar = tk.Button(root, text="Executar Código", command=executar_codigo)
botao_executar.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
