import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    b = 2.2
    c = 3.7
    

   

    a = np.sin(b)
    x = a + np.power(b + c , 3)
    y = 7 * np.exp(np.sqrt(np.abs(x))) + np.cos(4 * x)
    
    
    
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    x_text = ft.Text(f'a = {x:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                x_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)