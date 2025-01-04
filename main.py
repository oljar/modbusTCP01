import os
import time

from pyModbusTCP.client import ModbusClient

# init modbus client
c = ModbusClient(host='192.168.0.8', port=56789, unit_id=1, auto_open=True)

# main read loop
while True:
    # read 10 bits (= coils) at address 0, store result in coils list

    a = c.read_holding_registers(660)# digital_variable

    coils_l = c.read_holding_registers(658,1) #analog_variable
    coils_l = coils_l[0]/256

    print(a)
    print(coils_l)