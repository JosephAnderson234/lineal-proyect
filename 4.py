from manim import *
import math

class RotacionConMatriz(Scene):
    def construct(self):
        # Crear un sistema de ejes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )
        
        # Crear un cuadrado
        square = Square(color=RED)
        
        # Añadir los ejes y el cuadrado a la escena
        self.add(axes, square)
        self.wait(1)  

        # Definimos el origen
        origin = axes.coords_to_point(0, 0) 

        # Rotacion
        square_rotated = square.copy()
        matriz_rotacion = [[math.cos(math.pi / 3), -math.sin(math.pi / 3)], 
                           [math.sin(math.pi / 3), math.cos(math.pi / 3)]]
        
        self.play(Create(square_rotated))
        self.play(square_rotated.animate.apply_matrix(matriz_rotacion), run_time=2)
        self.wait(1) 
        
        matriz_rotacion_invertida = np.linalg.inv(matriz_rotacion)
        
        self.play(square_rotated.animate.apply_matrix(matriz_rotacion_invertida), run_time=2)
        self.wait(1)

        """
        # Creamos el vector de translación
        translation_vector = axes.coords_to_point(2, 1) - origin  
        #punto final - punto inicial
        """