import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    b = 7
    x = 2
    

   

    c = np.log(np.abs(b))
    a = np.power(b + x , 3)
    y = np.power(c , 2) + np.sqrt(np.abs(a))
    
    
    
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