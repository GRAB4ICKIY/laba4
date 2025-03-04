import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    x = 2.8
    b = 1.3
    

   

    a = np.power(b , 3) + np.log(b)
    c = np.power(a , 2) + np.sqrt(b)
    y = np.exp(x) + np.exp(5.8)
    
    
    
    a_text = ft.Text(f'a = {x:.2f}', size=20)
    c_text = ft.Text(f'c = {c:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                c_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)