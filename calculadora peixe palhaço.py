import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def abrir_janela_imc():
    def calcular_imc():
        try:
            peso = float(entry_peso.get())
            altura = float(entry_altura.get())
            imc = peso / (altura ** 2)
            resultado.set(f"Seu IMC é: {imc:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    janela_imc = tk.Toplevel(root)
    janela_imc.title("Cálculo de IMC")
    janela_imc.geometry("320x240")
    janela_imc.configure(bg="#ffe6f2")

    ttk.Label(janela_imc, text="Peso (kg):", background="#ffe6f2", font=("Arial", 12)).pack(pady=5)
    entry_peso = ttk.Entry(janela_imc, font=("Arial", 12))
    entry_peso.pack(pady=5)

    ttk.Label(janela_imc, text="Altura (m):", background="#ffe6f2", font=("Arial", 12)).pack(pady=5)
    entry_altura = ttk.Entry(janela_imc, font=("Arial", 12))
    entry_altura.pack(pady=5)

    resultado = tk.StringVar()
    ttk.Label(janela_imc, textvariable=resultado, background="#ffe6f2", font=("Arial", 12, "bold"), foreground="#ff0080").pack(pady=10)

    ttk.Button(janela_imc, text="Calcular", command=calcular_imc).pack(pady=10)

def abrir_janela_calculadora():
    def calcular():
        try:
            resultado.set(eval(entry_calculo.get()))
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida.")

    janela_calc = tk.Toplevel(root)
    janela_calc.title("Calculadora")
    janela_calc.geometry("320x240")
    janela_calc.configure(bg="#ffe6f2")

    ttk.Label(janela_calc, text="Digite a expressão:", background="#ffe6f2", font=("Arial", 12)).pack(pady=5)
    entry_calculo = ttk.Entry(janela_calc, font=("Arial", 12))
    entry_calculo.pack(pady=5)

    resultado = tk.StringVar()
    ttk.Label(janela_calc, textvariable=resultado, background="#ffe6f2", font=("Arial", 12, "bold"), foreground="#ff0080").pack(pady=10)

    ttk.Button(janela_calc, text="Calcular", command=calcular).pack(pady=10)

def abrir_janela_regra3():
    def calcular_regra3():
        try:
            numero1 = float(entry_numero1.get())
            numero2 = float(entry_numero2.get())
            numero3 = float(entry_numero3.get())
            resultado.set(f"Resultado: {(numero3 * numero2) / numero1:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    janela_regra3 = tk.Toplevel(root)
    janela_regra3.title("Regra de 3")
    janela_regra3.geometry("320x240")
    janela_regra3.configure(bg="#ffe6f2")

    ttk.Label(janela_regra3, text="Número 1:", background="#ffe6f2", font=("Arial", 12)).pack(pady=5)
    entry_numero1 = ttk.Entry(janela_regra3, font=("Arial", 12))
    entry_numero1.pack(pady=5)

    ttk.Label(janela_regra3, text="Número 2:", background="#ffe6f2", font=("Arial", 12)).pack(pady=5)
    entry_numero2 = ttk.Entry(janela_regra3, font=("Arial", 12))
    entry_numero2.pack(pady=5)

    ttk.Label(janela_regra3, text="Número 3:", background="#ffe6f2", font=("Arial", 12)).pack(pady=5)
    entry_numero3 = ttk.Entry(janela_regra3, font=("Arial", 12))
    entry_numero3.pack(pady=5)

    resultado = tk.StringVar()
    ttk.Label(janela_regra3, textvariable=resultado, background="#ffe6f2", font=("Arial", 12, "bold"), foreground="#ff0080").pack(pady=10)

    ttk.Button(janela_regra3, text="Calcular", command=calcular_regra3).pack(pady=10)

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Peixe Palhaço")
root.geometry("350x350")
root.configure(bg="#ffccff")

label_titulo = ttk.Label(root, text="Calculadora Peixe Palhaço", font=("Arial", 18, "bold"), background="#ffccff", foreground="#ff0066")
label_titulo.pack(pady=20)

btn_imc = ttk.Button(root, text="IMC", command=abrir_janela_imc)
btn_imc.pack(pady=10)

btn_calculadora = ttk.Button(root, text="Calculadora", command=abrir_janela_calculadora)
btn_calculadora.pack(pady=10)

btn_regra3 = ttk.Button(root, text="Regra de 3", command=abrir_janela_regra3)
btn_regra3.pack(pady=10)

root.mainloop()
