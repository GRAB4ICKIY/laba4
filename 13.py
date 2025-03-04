import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    
    x = 1.9
    a = - 0.9
    



    w = np.power(x , 2) * np.sqrt(np.abs(a + x))
    z = np.cos(2 * a + np.power(w , 2))
    y = a * np.power(z , 7) + np.sin(2 * w) 
    
    
    
    w_text = ft.Text(f'w = {w:.2f}', size=20)
    z_text = ft.Text(f'z = {z:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)
    
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                w_text,
                z_text,
                y_text,
            ], 
            spacing=20,
        )
    )        
ft.app(main)