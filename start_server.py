import os

def start_server():
    os.system('ssh "%s" "%s" "%s"' % ('pi@192.168.2.4', 'python', 'python-libs/RaspberryDrive/driving_server.py'))
    return
