from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
import time

def read_register(client, address, count, slave_id):
    res = client.read_input_registers(address=address, count=count, unit=slave_id)
    decoder = BinaryPayloadDecoder.fromRegisters(res.registers, Endian.Big, wordorder=Endian.Little)
    reading = decoder.decode_32bit_float()
    return reading

# Modbus TCP settings
adapter_addr = '192.168.0.7'
adapter_port = 502
slave_id = 1

# Create a Modbus TCP client
client = ModbusTcpClient(adapter_addr, port=adapter_port, framer=ModbusFramer)

while True:
    if client.connect():  # Trying to connect to the Modbus server/slave
        try:
                
            ########### HOBUT MFM 850 LTHN  Register Map####
            # 0x0006 = v1
            # 0x0008 = v2
            # 0x000A = v3
            # 0x000C = I1
            # 0x000E = I2
            # 0x0010 = I3
            # 0x0012 = kW sum
            # 0x001E = Hz
            #########################
            
            # Read v1 register (0x0006)
            v1 = read_register(client, address=0x0006, count=4, slave_id=slave_id)
            print("Lv1:", v1)

            print("-------------------------")

            time.sleep(2)

        except Exception as e:
            print("Error:", e)

        finally:
            client.close()

    else:
        print('Cannot connect to the Modbus server/slave')
        time.sleep(10)
