import flet as ft
import numpy as np

def  main(page: ft.Page):
    page.title = "Практическая работа №4"

    x = 8.52
    b = 9


    c = x + np.power(b,2)
    a = np.power(np.sqrt(c + b),3)
    y = np.power(np.cos(c),2) + c * np.power(np.cos(np.power(a,2)),4)


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