import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    x = 1.3
    k = 4

   

    a = np.log10(np.abs(x))
    b = np.exp(2 * x) + a * x
    y = x * np.power(a,3) + np.power(b,2)
    
    
    
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    b_text = ft.Text(f'b = {b:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                b_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)