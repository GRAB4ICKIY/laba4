import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    x = 2.1 
    p = 1

   

    b = np.sin(np.power(p , 2) + np.power(x , 3))
    a = np.exp(np.sqrt(np.abs(x)))
    y = np.power(a , 3) / np.power(b , 2)
    
    
    
    b_text = ft.Text(f'b = {b:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                b_text,
                a_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)