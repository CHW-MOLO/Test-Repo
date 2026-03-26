#!/usr/bin/env python3
import http.server
import socket
import sys


HOST = ""
PORT_CANDIDATES = [5173, 5174, 5175, 5176]


def can_bind(port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((HOST, port))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def main() -> None:
    chosen_port = None
    for port in PORT_CANDIDATES:
        if can_bind(port):
            chosen_port = port
            break

    if chosen_port is None:
        print("Kunne ikke finde en ledig port i listen:", PORT_CANDIDATES)
        sys.exit(1)

    if chosen_port != PORT_CANDIDATES[0]:
        print(
            f"Port {PORT_CANDIDATES[0]} er optaget, bruger fallback-port {chosen_port} i stedet."
        )
    else:
        print(f"Bruger ønsket port {chosen_port}.")

    server = http.server.ThreadingHTTPServer((HOST, chosen_port), http.server.SimpleHTTPRequestHandler)
    print(f"Server kører på http://localhost:{chosen_port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
