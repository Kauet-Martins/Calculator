import tkinter as tk

def adicionar_numero(num,):
    valor_atual = entry.get

    novo_valor = valor_atual + str(num)

    entry.delete(0, tk.END)

    entry.insert(tk.END, novo_valor)

root = tk.Tk()

root.title("Calculator App")

root.geometry('300x400')

frm = tk.Frame(root)

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=7, insertwidth=2, justify='right')

entry.grid(row=0, column=0, columnspan=4)

botao_1 = tk.Button(root, text='1', padx=20, pady=20, command=lambda: adicionar_numero(1))

botao_1.grid(row=1, column=0)

root.mainloop()