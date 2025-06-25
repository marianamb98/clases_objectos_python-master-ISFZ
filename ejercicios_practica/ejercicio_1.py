# IMPORTANTE: NO borrar los comentarios

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def obtener_puntaje(self):
        return self.puntaje

    def cargar_puntaje(self, nuevo_puntaje):
        self.puntaje = nuevo_puntaje

    def sumar_puntaje(self, puntos):
        self.puntaje += puntos

if __name__ == "__main__":
    print("Comencemos a practicar con objetos")
    # Alumno:
    # En este archivo ya tiene una clase creada
    # para representar a un Jugador. Esta clase posee:
    # --> el nombre del jugador
    # --> el puntaje inicial del jugador
    # --> un método para obtener el puntaje del jugador

    # 1) Deberá crear un jugador (un variable) a partir de esta clase
    # Al momento de crear el objeto debe indicar un nombre
    # para el jugador
    
    jugador1 = Jugador("Alejandro Fabian")
    jugador1.cargar_puntaje(100)
    jugador1.sumar_puntaje(25)
        
    # 2) Utilice el método "obtener_puntaje"
    # para leer el puntaje actual del jugador
    # Almacene el puntaje obtenido del método
    # en una variable llamada "puntaje"
    puntaje = jugador1.obtener_puntaje()
    # Este valor de puntaje debe ser 125
    # Ya que hemos agregado 100 y 25 puntos
    
    # Imprimir en pantalla la variable "puntaje"
    print("Puntaje del jugador:", puntaje)
    print("Ejercicio Finalizado.")
