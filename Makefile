install_vcan:
	lsmod | grep -q vcan || sudo ip link add dev vcan0 type vcan
	sudo ip link set up vcan0

remove_vcan:
	sudo modprobe -r vcan

view_can:
	python -m can.viewer -i seeedstudio -b 250000 -c /dev/ttyCH340

log_can:
	python -m can.logger -i seeedstudio -b 250000 -c /dev/ttyCH340
