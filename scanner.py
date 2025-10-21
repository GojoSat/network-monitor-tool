import socket
import threading
import time

class PortScanner:
    def __init__(self, host, start_port, end_port, callback):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port
        self.callback = callback

    def scan_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        start_time = time.time()
        try:
            result = s.connect_ex((self.host, port))
            latency = (time.time() - start_time) * 1000
            if result == 0:
                self.callback(port, "Open", latency)
            else:
                self.callback(port, "Closed", None)
        except Exception:
            self.callback(port, "Error", None)
        finally:
            s.close()

    def start(self):
        for port in range(self.start_port, self.end_port + 1):
            t = threading.Thread(target=self.scan_port, args=(port,))
            t.daemon = True
            t.start()
