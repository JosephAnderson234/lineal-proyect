from manim import *

class TransformTriangle(Scene):
    def construct(self):
        # Crear el sistema de ejes 2D
        #Usar el formato [x, y, z] en los rangos de cada uno
        axes = Axes(
            x_range=[-2, 8, 1],  
            y_range=[-2, 6, 1],  
            axis_config={"color": GREEN}  # Configurar color de los ejes
        )

        # Etiquetas de los ejes
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Puntos del triangulo
        A_cartesian = [1, 2] 
        B_cartesian = [3, 1]  
        C_cartesian = [2, 4] 

        # Volver a puntos relativos del plano "axes" generados
        A = axes.coords_to_point(*A_cartesian)
        B = axes.coords_to_point(*B_cartesian) #"*" los desempaqueta, y puedan pasarse así 3,1 y ya no [3,1]
        C = axes.coords_to_point(*C_cartesian)

        # Creación del trigangulo con los puntos relatvios
        triangle = Polygon(A, B, C, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.5)

        # Mostrar la escena con los ejes y el triangulo
        self.play(Create(axes), Create(labels))
        self.play(Create(triangle))
        self.wait(1)  

        # Definimos el origen
        origin = axes.coords_to_point(0, 0) 

        # Rotacion
        # No encontré forma de usar la matriz porque lo rotaba en sentido horario TuT
        triangle_rotated = triangle.copy()
        
        self.play(Create(triangle_rotated))
        self.play(triangle_rotated.animate.rotate(angle=PI / 4, about_point=origin), run_time=2)
        self.wait(1) 

        # Creamos el vector de translación
        translation_vector = axes.coords_to_point(2, 1) - origin  
        #punto final - punto inicial
        
        triangle_moved = triangle_rotated.copy()
        #lo animamos
        self.play(Create(triangle_moved))
        self.play(triangle_moved.animate.shift(translation_vector), run_time=2)

        # 9. Pausa final para observar el triángulo trasladado
        self.wait()

