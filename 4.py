import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    x = 2.7
    t = -6

   

    a = np.log(x)
    b = np.sqrt(np.power(x , 2) + np.power(t , 2))
    y = 5 * np.sqrt(np.abs(a - b * x))
    
    
    
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