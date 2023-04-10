class Cliente:
    def __init__(self, nombre, apellido, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def realizar_compra(self, producto):
        print(f"{self.nombre} {self.apellido} ha comprado {producto}")

    def mostrar_informacion(self):
        print(f"Información del cliente:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Dirección: {self.direccion}")