import tkinter as tk
from tkinter import messagebox

def show_services():
    messagebox.showinfo("Услуги и цены", "Выберите услугу:")
def make_buttons():
    root = tk.Tk()
    root.title("Пример кнопок")

    # Создание главной кнопки "Услуги и цены"
    services_button = tk.Button(root, text="Услуги и цены", command=show_services)
    services_button.pack(pady=20)

    # Создание дополнительных кнопок, которые будут показаны после нажатия "Услуги и цены"
    walk_button = tk.Button(root, text="Выгул")
    walk_button.pack()

    boarding_button = tk.Button(root, text="Передержка")
    boarding_button.pack()

    pet_sitting_button = tk.Button(root, text="Зоо-няня")
    pet_sitting_button.pack()

    root.mainloop()