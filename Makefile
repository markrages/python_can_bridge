default: install_vcan
	./vcan_bridge.py

install_vcan:
	lsmod | grep -q vcan || sudo ip link add dev vcan0 type vcan
	sudo ip link set up vcan0
	# rate limit from https://github.com/mguentner/cannelloni
	sudo tc qdisc add dev vcan0 root tbf rate 150kbit latency 100ms burst 1000 || true

remove_vcan:
	sudo modprobe -r vcan

view_can:
	python -m can.viewer -i seeedstudio -b 250000 -c /dev/ttyCH340

log_can:
	python -m can.logger -i seeedstudio -b 250000 -c /dev/ttyCH340
