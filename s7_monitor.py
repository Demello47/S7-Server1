
import struct
import time
from s7 import Client

client = Client()

try:
    client.connect("127.0.0.1", 0, 1, tcp_port=1102)
    print("S7 connection established")

    while True:
        data = client.db_read(1, 42, 4)
        pressure = struct.unpack(">f", data)[0]

        print(f"DB1.DBD42 = {pressure:.2f}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Monitoring stopped")

except Exception as error:
    print("Communication error:", error)

finally:
    client.disconnect()
