import struct

from s7 import Client

client = Client()
client.connect("127.0.0.1", 0, 1, tcp_port=1102)

heartbeat_data = client.db_read(1, 0, 2)
heartbeat = struct.unpack(">h", heartbeat_data)[0]

pressure_data = client.db_read(1, 42, 4)
pressure = struct.unpack(">f", pressure_data)[0]

print("Heartbeat:", heartbeat)
print("Air Pressure:", pressure)

client.disconnect()