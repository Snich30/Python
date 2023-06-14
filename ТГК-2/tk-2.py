import tkinter as tk

root = tk.Tk()
root.title("Rainbow")

def add_color(color_code, color_name):
    text.insert("end", color_code)
    label.config(text=color_name)

red_button = tk.Button(root, text="Красный", command=lambda: add_color("#ff0000", "Красный"), bg="#ff0000", fg="white")
orange_button = tk.Button(root, text="Оранжевый", command=lambda: add_color("#ff7d00", "Оранжевый"), bg="#ff7d00")
yellow_button = tk.Button(root, text="Желтый", command=lambda: add_color("#ffff00", "Желтый"), bg="#ffff00")
green_button = tk.Button(root, text="Зеленый", command=lambda: add_color("#00ff00", "Зеленый"), bg="#00ff00")
blue_button = tk.Button(root, text="Голубой", command=lambda: add_color("#007dff", "Голубой"), bg="#007dff", fg="white")
indigo_button = tk.Button(root, text="Синий", command=lambda: add_color("#0000ff", "Синий"), bg="#0000ff", fg="white")
violet_button = tk.Button(root, text="Фиолетовый", command=lambda: add_color("#7d00ff", "Фиолетовый"), bg="#7d00ff", fg="white")

text = tk.Text(root, height=1)
label = tk.Label(root, text="Выберите цвет")

red_button.pack(fill="both", expand=True)
orange_button.pack(fill="both", expand=True)
yellow_button.pack(fill="both", expand=True)
green_button.pack(fill="both", expand=True)
blue_button.pack(fill="both", expand=True)
indigo_button.pack(fill="both", expand=True)
violet_button.pack(fill="both", expand=True)
text.pack(fill="both", expand=True)
label.pack()

root.mainloop()