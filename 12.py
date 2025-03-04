import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    q = 2
    b = 1.8
    

   

    t = np.power(b , 3) + np.exp(np.sqrt(4))
    x = np.power(t , 3) + np.power(b , 2)
    y = np.arctan(2 * np.abs(x))
    
    
    
    t_text = ft.Text(f't = {t:.2f}', size=20)
    x_text = ft.Text(f'x = {x:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                t_text,
                x_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)