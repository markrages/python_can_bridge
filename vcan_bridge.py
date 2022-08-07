#!/usr/bin/env python3

import can
from time import sleep

can_bus_a = can.Bus('/dev/ttyCH340', bustype='seeedstudio', bitrate=250000)
can_bus_b = can.Bus('vcan0', bustype='socketcan')

try:
    for message in can_bus_a:
        can_bus_b.send(message)

    while True:
        sleep(1)

except KeyboardInterrupt:
    print("\nProgram Ended")
    exit(0)
