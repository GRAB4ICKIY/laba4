import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    m = 2
    x = 1.1

   

    a = np.sqrt(np.abs(x))
    b = np.power(x , 4) + np.power(m , 2)
    y = np.power(np.sin(a + np.power(np.tan(b),3)),2)
    
    
    
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