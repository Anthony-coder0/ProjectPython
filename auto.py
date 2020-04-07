# bike2.py
# Definiremos un clase llamada auto
class Auto:

    def __init__(self, color, placa, estado): # En el inicializador __init__ agregamos propiedades color, placa y estado
        self.color = color # Asignamos los metodos en otras variables con igual nombre
        self.placa = placa
        self.estado = estado


    def Alto(self):
        print("Detente")


blanco_auto = Auto('Blanco', 'P-405', 'Buen estado') # Asignamos los valores a las propiedades


# Mostramos en pantalla un mensaje indicando el color, placa y estado del carro
print("El color del carro es: "+blanco_auto.color+"\ncon No. de placa: "+blanco_auto.placa+"\nse encuentra en "+blanco_auto.estado)
blanco_auto.Alto()
