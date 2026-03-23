import tkinter as tk
import math
from tkinter import messagebox

# ---------------- FUNÇÕES ---------------- #

def obter_valor(entry):
    try:
        return float(entry.get())
    except:
        messagebox.showerror("Erro", "Digite apenas números válidos!")
        return None

def mostrar_resultado(valor):
    resultadoLabel.config(text=f"Resultado: {valor:.2f}")
    messagebox.showinfo("Resultado", f"O resultado é {valor:.2f}")

def area_triangulo():
    base = obter_valor(valor1Entry)
    altura = obter_valor(valor2Entry)
    if base is not None and altura is not None:
        mostrar_resultado((base * altura) / 2)

def area_retangulo():
    base = obter_valor(valor1Entry)
    altura = obter_valor(valor2Entry)
    if base is not None and altura is not None:
        mostrar_resultado(base * altura)

def area_quadrado():
    lado = obter_valor(valor1Entry)
    if lado is not None:
        mostrar_resultado(lado ** 2)

def area_circulo():
    raio = obter_valor(valor1Entry)
    if raio is not None:
        mostrar_resultado(math.pi * (raio ** 2))

# ---------------- INTERFACE ---------------- #

janela = tk.Tk()
janela.title("Calculadora de Áreas")
janela.geometry("420x420")
janela.config(bg="#1e1e2f")  # fundo escuro moderno

# Título
titulo = tk.Label(
    janela,
    text="📐 Calculadora de Áreas",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
titulo.pack(pady=15)

# Frame inputs
frame = tk.Frame(janela, bg="#1e1e2f")
frame.pack()

tk.Label(frame, text="Valor 1 (base/lado/raio):", bg="#1e1e2f", fg="white").grid(row=0, column=0, pady=5)
valor1Entry = tk.Entry(frame, bg="#2a2a40", fg="white", insertbackground="white")
valor1Entry.grid(row=0, column=1)

tk.Label(frame, text="Valor 2 (altura):", bg="#1e1e2f", fg="white").grid(row=1, column=0, pady=5)
valor2Entry = tk.Entry(frame, bg="#2a2a40", fg="white", insertbackground="white")
valor2Entry.grid(row=1, column=1)

# Frame botões
botoes_frame = tk.Frame(janela, bg="#1e1e2f")
botoes_frame.pack(pady=20)

def criar_botao(texto, comando, linha, coluna):
    tk.Button(
        botoes_frame,
        text=texto,
        width=15,
        command=comando,
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        font=("Arial", 10, "bold"),
        relief="flat"
    ).grid(row=linha, column=coluna, padx=8, pady=8)

criar_botao("Triângulo", area_triangulo, 0, 0)
criar_botao("Retângulo", area_retangulo, 0, 1)
criar_botao("Quadrado", area_quadrado, 1, 0)
criar_botao("Círculo", area_circulo, 1, 1)

# Resultado
resultadoLabel = tk.Label(
    janela,
    text="Resultado:",
    font=("Arial", 13, "bold"),
    bg="#1e1e2f",
    fg="#00ffcc"
)
resultadoLabel.pack(pady=20)

janela.mainloop()