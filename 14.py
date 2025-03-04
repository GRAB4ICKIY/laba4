import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    b = 6
    k = 3.4
    



    t = np.power(b , 2) + np.power(k , 3)
    a = np.sqrt(b + t)
    y = np.sin(4 * np.power(a , 2) + np.power(b , 2)) 
    
    
    
    t_text = ft.Text(f't = {t:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                t_text,
                a_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)