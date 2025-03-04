import flet as ft
import numpy as np

def  main(page: ft.Page):
    page.title = "Практическая работа №4"

    b = 8.1
    t = 2


    c = np.sqrt(b + np.power(t,2))
    a = np.power(np.cos(b),2) + np.power(np.sin(c),2)
    y = np.power(a,2) + np.power(np.sqrt(np.abs(a)),3)

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