
import socket

HOST = '0.0.0.0'
PORT = int(os.environ.get("PORT", 443))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"🔌 Esperando conexión en el puerto {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"✅ Conectado desde {addr}")
        data = conn.recv(1024)
        print("📦 Datos recibidos:")
        print(data.decode(errors='ignore'))
