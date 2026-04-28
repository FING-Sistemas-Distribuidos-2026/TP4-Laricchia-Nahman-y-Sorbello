"""
publisher.py — ZeroMQ Pub/Sub  |  SERVIDOR (Python / pyzmq)
TP4 - Sistemas Distribuidos
Laricchia Aida, Nahman Martina y Sorbello Mauro
"""

import zmq
import time

TOPIC = "noticias"
PORT  = 5556


def main():
    context = zmq.Context()
    socket  = context.socket(zmq.PUB)
    socket.bind(f"tcp://*:{PORT}")

    print(f"[Publisher Python] Escuchando en tcp://*:{PORT} | tópico: '{TOPIC}'")
    print("Publicando mensajes cada 1 segundo... (Ctrl+C para detener)\n")

    counter = 0
    try:
        while True:
            counter += 1
            mensaje = f"Mensaje #{counter} — El club deportivo maipú ganó el fin de semana y el pueblo botellero está de fiesta"

            # El frame va: "<TOPIC> <contenido>"
            # ZeroMQ filtra por el prefijo del primer frame
            socket.send_string(f"{TOPIC} {mensaje}")

            print(f"[PUB] {TOPIC} | {mensaje}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[Publisher] Detenido.")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    main()