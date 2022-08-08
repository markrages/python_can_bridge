# python_can_bridge
* bridge two [python-can](https://python-can.readthedocs.io/en/master/) interfaces *

This is a simple script to bridge two Python-can buses, transferring
all data from one bus to the other and vice-versa.

Why would you want to do this? See the [Makefile](Makefile). I have a
cheap CH341-based CAN interface that I wanted to use with a program
written against the Linux
[SocketCAN](https://www.kernel.org/doc/html/latest/networking/can.html)
API.  The solution?  Set up a SocketCAN `vcan` virtual CAN interface
and point the program there. Then run this program to bridge the
python-can `seeedstudio` driver. The virtual CAN interface copies
writes to all readers. (This is how CAN works, after all. Each device
on the bus sees every frame.)

In other words, this allows a Python userspace CAN driver to be used
from the SocketCAN interface.

If you have a different interface edit the script (it's very simple).

The [Makefile](Makefile) contains all the set up commands so that I
don't have to remember them. Default target does everything: it sets
up the virtual interface and runs the bridge.

Copy `99-ch340.rules` to `/etc/udev/rules.d` to have the CH340-based
device at the stable name `/dev/ttyCH340` rather than some random
index based on when you connected the device. (If you have more than
one CH340 device, you're on your own.)
