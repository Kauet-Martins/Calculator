import tkinter as tk

def add_number():

    entrada.insert(0, 1)

    

root = tk.Tk()


root.geometry("300x275")

entrada = tk.Entry(root, width=20,justify="center", font=("Arial", 20))
entrada.place(x=0, y=5)

botao_1 = tk.Button(root, text=1, width=10, command=add_number)
botao_1.place(x=20, y=50)

botao_2 = tk.Button(root, text=2, width=10)
botao_2.place(x=110, y=50)

botao_3 = tk.Button(root, text=3, width=10)
botao_3.place(x=200, y=50)

botao_4 = tk.Button(root, text=4, width=10)
botao_4.place(x=20, y=90)

botao_5 = tk.Button(root, text=5, width=10)
botao_5.place(x=110, y=90)

botao_6 = tk.Button(root, text=6, width=10)
botao_6.place(x=200, y=90)

botao_7 = tk.Button(root, text=7, width=10)
botao_7.place(x=20, y=130)

botao_8 = tk.Button(root, text=8, width=10)
botao_8.place(x=110, y=130)

botao_9 = tk.Button(root, text=9, width=10)
botao_9.place(x=200, y=130)

botao_0 = tk.Button(root, text=0, width=10)
botao_0.place(x=110, y=170)

root.mainloop()