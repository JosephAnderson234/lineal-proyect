from manim import *
import numpy as np

# Definir la matriz M
M = np.array([[1.000, 0.500, -0.500, -1.000, -0.500, 0.500, 0.840, 0.315, -0.210, -0.360, -0.210, 0.315],
              [-0.800, -0.800, -0.800, -0.800, -0.800, -0.800, -0.400, 0.125, 0.650, 0.800, 0.650, 0.125],
              [0.000, -0.866, -0.866, 0.000, 0.866, 0.866, 0.000, -0.546, -0.364, 0.000, 0.364, 0.546]])

# Convertir los puntos de M en coordenadas 3D
def crear_puntos(M):
    return [np.array([M[0, i], M[1, i], M[2, i]]) for i in range(M.shape[1])]

# Funcion que cambia los ejes y con z
def Acomodar_Matriz(M):
    M_modificada = M.copy()
    M_modificada[1] = M[2]
    M_modificada[2] = M[1]
    return M_modificada

class Ejercicio8(ThreeDScene):
    def construct(self):
        texto = MathTex("M =")
        matriz = Matrix(M, v_buff=0.8, h_buff=1.8)
        matriz.scale(0.45)
        matriz.shift(0.5*RIGHT)
        texto.next_to(matriz, LEFT)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.set_color(BLUE)

        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)
        self.remove(expresion_completa)

        # Configuracion de la Camara
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5, focal_distance=100)
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(Text("x").scale(1), Text("y").scale(1), Text("z").scale(1))
        axes.shift(2.5*RIGHT, 2.5*DOWN)
        labels.shift(2.5*RIGHT, 2.5*DOWN)
        self.play(Create(axes), Create(labels))
        self.wait(2)

        # Crear la figura inicial a partir de la matriz M
        M_modificada = Acomodar_Matriz(M)
        pol = Polyhedron(
            M_modificada.transpose().tolist(),
            [
                [0, 1, 2, 3, 4, 5],
                [5, 0, 6, 11],
                [0, 1, 7, 6],
                [1, 2, 8, 7],
                [2, 3, 9, 8],
                [3, 4, 10, 9],
                [4, 5, 11, 10],
                [6, 7, 8, 10, 11],
                [10, 8, 9]
            ]
        )
        pol.shift(2.5*RIGHT, 2.5*DOWN)
        self.play(Create(pol))
        self.wait(2)

        # a) Escalar por un factor de 0.3 en x y 0.5 en y
        texto = Text("Escalar por 0.3 en x; por 0.5 en y", font_size=24, color=RED_C)
        matriz1 = MathTex("M *")
        matriz2 = Matrix([[0.3, 0, 0],
                        [0, 0.5, 0],
                        [0, 0, 1]])
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5*RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        self.play(pol.animate.apply_matrix([[0.3, 0, 0], [0, 0.5, 0], [0, 0, 1]]))
        self.wait(2)

        self.remove(expresion_completa)

        # b) Rotar 45 grados alrededor del eje x
        texto = Text("Rotar 45 grados alrededor del eje x", font_size=24, color=RED_C)
        matriz1 = MathTex("M *")
        matriz2 = MathTex("\\begin{bmatrix} cos(45°) & -sin(45°) & 0 \\\ sin(45°) & cos(45°) & 0 \\\ 0 & 0 & 1 \\end{bmatrix}")
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5 * RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        angulo_x = 45 * DEGREES
        matriz_rotacion_x = [[1, 0, 0], [0, np.cos(angulo_x), -np.sin(angulo_x)], [0, np.sin(angulo_x), np.cos(angulo_x)]]
        self.play(pol.animate.apply_matrix(matriz_rotacion_x))
        self.wait(2)

        self.remove(expresion_completa)

        # c) Trasladar 1 unidad en la dirección x
        texto = Text("Trasladar 1 unidad en la dirección x", font_size=24, color=RED_C)
        matriz1 = MathTex("M +")
        matriz2 = Matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], h_buff=0.5)
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5 * RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        self.play(pol.animate.shift(RIGHT))
        self.wait(2)

        self.remove(expresion_completa)

        # d) Rotar 35 grados alrededor del eje y
        texto = Text("Rotar 35 grados alrededor del eje y", font_size=24, color=RED_C)
        matriz1 = MathTex("M *")
        matriz2 = MathTex("\\begin{bmatrix} cos(35°) & 0 & -sin(35°) \\\ 0 & 1 & 0 \\\ sin(35°) & 0 & cos(45°) \\end{bmatrix}")
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5 * RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        angulo_y = 35 * DEGREES
        matriz_rotacion_y = [[np.cos(angulo_y), 0, -np.sin(angulo_y)], [0, 1, 0], [np.sin(angulo_y), 0, np.cos(angulo_y)]]
        self.play(pol.animate.apply_matrix(matriz_rotacion_y))
        self.wait(2)

        self.remove(expresion_completa)

        # e) Rotar -45 grados alrededor del eje z
        texto = Text("Rotar -45 grados alrededor del eje z", font_size=24, color=RED_C)
        matriz1 = MathTex("M *")
        matriz2 = MathTex("\\begin{bmatrix} cos(-45°) & -sin(-45°) & 0 \\\ sin(-45°) & cos(-45°) & 0 \\\ 0 & 0 & 1 \\end{bmatrix}")
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5 * RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        angulo_z = -45 * DEGREES
        matriz_rotacion_z = [[np.cos(angulo_z), -np.sin(angulo_z), 0], [np.sin(angulo_z), np.cos(angulo_z), 0], [0, 0, 1]]
        self.play(pol.animate.apply_matrix(matriz_rotacion_z))
        self.wait(2)

        self.remove(expresion_completa)

        # f) Trasladar 1 unidad en la dirección z
        texto = Text("Trasladar 1 unidad en la dirección z", font_size=24, color=RED_C)
        matriz1 = MathTex("M +")
        matriz2 = Matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],  h_buff=0.5)
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5 * RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        self.play(pol.animate.shift(OUT))
        self.wait(2)

        self.remove(expresion_completa)

        # g) Escalar por un factor de 2 en la dirección x
        texto = Text("Escalar por 2 en la dirección x", font_size=24, color=RED_C)
        matriz1 = MathTex("M *")
        matriz2 = Matrix([[2, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]])
        matriz2.scale(0.5)
        matriz1.next_to(matriz2, LEFT)
        matriz = VGroup(matriz1, matriz2)
        matriz.set_color(BLUE)
        texto.next_to(matriz, UP)
        expresion_completa = VGroup(texto, matriz)
        expresion_completa.shift(3.5 * RIGHT)
        self.add_fixed_in_frame_mobjects(expresion_completa)
        self.wait(2)

        self.play(pol.animate.apply_matrix([[2, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.wait(2)

        self.remove(expresion_completa)
# Configurar el archivo de salida
config.frame_width = 12
config.frame_height = 12