import flet as ft
import numpy as np

def  main(page: ft.Page):
    page.title = "Практическая работа №4"

    x = 1.4
    p = 1.6


    c = np.power(x,4) + np.log10(np.power(p,3))
    a = np.log10(np.abs(x))
    y = np.power(np.sin(a * x),3) + np.sqrt(c) * np.cos(np.power(x,2))


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