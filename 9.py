import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    k = 1
    m = 1.8
    

   

    x = np.exp(m * k)
    c = np.cos(2 * m) + np.power(k , 2)
    y = np.power(np.sqrt(np.power(x , 2) + np.power(c , 2)) , 3)
    
    
    
    x_text = ft.Text(f'x = {x:.2f}', size=20)
    c_text = ft.Text(f'c = {c:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                x_text,
                c_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)