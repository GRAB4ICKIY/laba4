import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    k = 8.2
    x = 5
    

   

    c = np.sqrt(np.abs(x))
    a = np.power(c , 4) + np.power(k ,3)
    y = np.log(3 * a) + np.cos(5 * x)
    
    
    
    c_text = ft.Text(f'c = {c:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                c_text,
                a_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)