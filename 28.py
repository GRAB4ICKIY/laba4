import flet as ft
import numpy as np

def  main(page: ft.Page):
    page.title = "Практическая работа №4"

    b = 2.19
    k = 1.7


    c = np.power(k,2) + np.sqrt(b)
    a = b + np.power(c,2) * np.exp(c)
    y = np.power(np.cos(np.power(a,3) + b),4)

    c_text = ft.Text(f'c = {c: .2f}', size=20)
    a_text = ft.Text(f'a = {a: .2f}', size=20)
    y_text = ft.Text(f'y = {y: .2f}', size=20)



    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                a_text,
                c_text,
            ],
            spacing=20
        )
    )

ft.app(target=main)