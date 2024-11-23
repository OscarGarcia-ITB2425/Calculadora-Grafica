import tkinter as tk
from math import sqrt, pow

class CalculadoraGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Gráfica")
        self.root.geometry("400x550")
        self.root.configure(bg="#282c34")  # Fondo oscuro

        # Entrada principal
        self.entrada = tk.Entry(
            self.root, width=20, font=("Arial", 24), bd=0, relief=tk.FLAT, justify="right", bg="#abb2bf", fg="#282c34"
        )
        self.entrada.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('x²', 5, 1)
        ]

        colores = {
            "C": "#e06c75",
            "=": "#98c379",
            "√": "#61afef",
            "x²": "#d19a66",
            "/": "#56b6c2",
            "*": "#56b6c2",
            "-": "#56b6c2",
            "+": "#56b6c2",
        }

        for texto, fila, col in botones:
            color_fondo = colores.get(texto, "#e5e5e5")
            color_texto = "#ffffff" if texto in colores else "#282c34"
            boton = tk.Button(
                self.root,
                text=texto,
                width=5,
                height=2,
                font=("Arial", 16, "bold"),
                bg=color_fondo,
                fg=color_texto,
                relief=tk.FLAT,
                command=lambda t=texto: self.interactuar(t),
            )
            boton.grid(row=fila, column=col, padx=10, pady=10)

    def interactuar(self, texto):
        if texto == "=":
            self.calcular()
        elif texto == "C":
            self.limpiar()
        elif texto == "√":
            self.raiz()
        elif texto == "x²":
            self.cuadrado()
        else:
            self.agregar_texto(texto)

    def agregar_texto(self, texto):
        self.entrada.insert(tk.END, texto)

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def raiz(self):
        try:
            valor = float(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(sqrt(valor)))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def cuadrado(self):
        try:
            valor = float(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(pow(valor, 2)))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGrafica(root)
    root.mainloop()
