#!/usr/bin/env python3

import can

can_bus_a = can.Bus('/dev/ttyCH340', bustype='seeedstudio', bitrate=250000)
can_bus_b = can.Bus('vcan0', bustype='socketcan')

print("Bridging",can_bus_a,"to",can_bus_b)

listener_a = can.RedirectReader(can_bus_a)
listener_b = can.RedirectReader(can_bus_b)

timeout = 0.1 # seconds

# Notify each bus on the other bus's listener
notifier_a = can.Notifier(can_bus_a, [listener_b], timeout=timeout)
notifier_b = can.Notifier(can_bus_b, [listener_a], timeout=timeout)

try:
    from time import sleep
    while True:
        sleep(1)

except KeyboardInterrupt:
    pass

finally:
    notifier_a.stop()
    notifier_b.stop()
