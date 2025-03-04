import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    a = 5.5
    p = 4

    



    b = np.abs(a) + np.sqrt(a + np.power(p ,2))
    x = np.exp(b)
    y = np.cos(3 * x + np.abs(a))
    
    
    
    b_text = ft.Text(f'b = {b:.2f}', size=20)
    x_text = ft.Text(f'x = {x:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                b_text,
                x_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)