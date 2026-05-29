# Servidor y Cliente TCP en Python

Comunicación básica entre servidor y cliente usando sockets TCP.

## Cómo funciona

1. El servidor se pone en escucha en `127.0.0.1:8888`
2. El cliente se conecta al servidor
3. El servidor envía `"Hola, Cliente"`
4. El cliente recibe y muestra el mensaje

## Cómo usarlo

### Terminal 1 (Servidor)
```bash
python servidor.py

Servidor esperando conexion en el puerto 8888...
Cliente conectado desde: ('127.0.0.1', 54321)

Mensaje del servidor: Hola, Cliente

Requisitos

    Python 3.x

    Módulo socket (incluido)
