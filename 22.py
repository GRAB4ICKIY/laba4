import flet as ft
import numpy as np

def  main(page: ft.Page):
    page.title = "Практическая работа №4"

    m = 5.7
    p = 4

    c = np.sin(np.power(m,3))
    a = np.power(p,2) + c
    y = np.power(np.log10(np.abs(a + c)),4)



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