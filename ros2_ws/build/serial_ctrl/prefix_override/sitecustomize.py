import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/my_new_project/ros2_ws/install/serial_ctrl'
