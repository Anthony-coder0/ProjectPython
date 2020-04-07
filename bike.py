# bike.py
# Definimos la Clase Bike
class Bike:
    # Cuerpo de la clase Bike
    def __init__(self, colour, frame_material): # Método __init__ es el inicializador que configura los objetos con los valores color y material de marco 
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")

# Instancias creadas con los atributos
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# inspeccionemos los objetos que tenemos, instancias de la clase Bike.
print(red_bike.colour)  # Mostramos en pantalla: Rojo
print(red_bike.frame_material)  # Mostramos en pantalla: Fibra de carbón
print(blue_bike.colour)  # Mostramos en pantalla: Azul
print(blue_bike.frame_material)  # Mostramos en pantalla: Acero

# Vamos a frenar :)
red_bike.brake()  # Mostramos en pantalla: Frenado!
