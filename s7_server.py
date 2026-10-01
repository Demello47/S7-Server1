import struct
import time

from s7.server import Server
from s7.type import SrvArea

db = bytearray(320)

struct.pack_into(">h", db, 4, 0)
struct.pack_into(">h", db, 10, 12)
struct.pack_into(">f", db, 42, 1.50)

db[58:71] = b"LAB-ESP32-001"

server = Server()
server.register_area(SrvArea.DB, 1, db)
server.start(tcp_port=1102)

print("S7 Server started on port 1102")

heartbeat = 0

try:
    while True:
        heartbeat = 1 - heartbeat
        struct.pack_into(">h", db, 0, heartbeat)

        print("Heartbeat:", heartbeat)
        time.sleep(1)

except KeyboardInterrupt:
    server.stop()