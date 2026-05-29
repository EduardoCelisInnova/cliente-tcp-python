#Ejercicio cliente TCP.

print("Ejercicio Cliente TCP")


import socket

# 1. Crear socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(5)

# 2. Conectar a ("time.nist.gov", 13) con timeout. Aqui se indica al servidor
# que se desea conectar para hacer la prueba

try:
    cliente.connect(("time.nist.gov", 13))
    datos = cliente.recv(1024)
    print(f"Conectado: {datos.decode()}")
except Exception as e:
    print(f"Error: {e}")
    
# 3. Cerrar socket
finally:
    cliente.close()
