import flet as ft
import numpy as np

def  main(page: ft.Page):
    page.title = "Практическая работа №4"

    b = 0.3
    x = 5.2


    c = x * np.power(b,2) + np.sqrt(x)
    a = np.log10(np.abs(c * x + np.power(b,2)))
    y = (np.power(np.log10(1),a + b)) + (np.power(a,2)) / a + c


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