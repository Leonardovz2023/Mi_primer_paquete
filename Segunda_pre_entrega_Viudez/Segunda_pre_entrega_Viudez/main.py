from mi_paquete.cliente import Cliente
from mi_paquete.primera_entrega import registrar_usuario

# Crear instancia de la clase Cliente
cliente = Cliente("Juan", "Pérez", 30, "Calle 123, Ciudad")
# Llamar al método realizar_compra
cliente.realizar_compra("producto1")

# Llamar a la función registrar_usuario de la clase primera_entrega
registrar_usuario("usuario1", "contrasena1", {"usuario1": "contrasena1"})
