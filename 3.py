from manim import *

class CubeScene(ThreeDScene):
    def construct(self):
        # Crear un sistema de ejes 3D
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )
        
        label3d = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        # Crear un cubo
        cube = Cube()
        
        cube.move_to(ORIGIN)
        
        # Añadir los ejes y el cubo a la escena
        self.add(axes, label3d, cube)
        
        # Establecer la vista inicial de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Esperar para visualizar la configuración inicial
        self.wait(1)

        # X =  RIGHT
        # Y =  UP
        # Z =  OUT
        
        # Rotar el cubo 30° grados al eje Y (UP)
        self.play(Rotate(cube, angle=PI/6, axis=UP))
        self.wait(1)
        
        self.play(Rotate(cube, angle=PI/4, axis=RIGHT))
        self.wait(1)



        # Trasladar el cubo a lo largo del eje X
        #self.play(cube.animate.shift(RIGHT * 2))
        #self.wait(1)
        
        
        # Secuencia de animaciones: rotación y traslación
        """self.play(Succession(
            cube.animate.rotate(PI/4, axis=UP),
            cube.animate.shift(RIGHT * 2),
            cube.animate.rotate(-PI/4, axis=DOWN)
        ))
        self.wait(1)"""