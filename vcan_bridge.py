#!/usr/bin/env python3

import can
from time import sleep

can_bus_a = can.Bus('/dev/ttyCH340', bustype='seeedstudio', bitrate=250000)
can_bus_b = can.Bus('vcan0', bustype='socketcan')

listener_a = can.RedirectReader(can_bus_a)
listener_b = can.RedirectReader(can_bus_b)

notifier_a = can.Notifier(can_bus_a, [listener_b])
notifier_b = can.Notifier(can_bus_b, [listener_a])

try:
    while True:
        sleep(1)

except KeyboardInterrupt:
    print("\nProgram Ended")

finally:
    notifier_a.stop()
    notifier_b.stop()
