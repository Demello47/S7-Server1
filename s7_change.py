
import struct
from s7 import Client

client = Client()

try:
    client.connect("127.0.0.1", 0, 1, tcp_port=1102)

    value = float(input("New pressure: "))

    data = bytearray(struct.pack(">f", value))

    client.db_write(1, 42, data)

    result = client.db_read(1, 42, 4)
    actual = struct.unpack(">f", result)[0]

    print(f"Server pressure: {actual:.2f}")

finally:
    client.disconnect()
