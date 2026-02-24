import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/samuel/Roboticaclase/ultrason_ws/scr/install/obstaculo'
