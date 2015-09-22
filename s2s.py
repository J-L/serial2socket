import serial, time, socket

class s2s:
    
    def __init__(self, serial_port = "COM1", baud_rate= 115200, socket =5252, num_bytes = 64, read_delay= 0.001):
        self.baud_rate = baud_rate
        self.socket = socket
        self.num_bytes = num_bytes
        self.serial_port = serial_port
    def open():
        self.stay_connected = True
        # serial port opening
        self.ser = Serial.Serial()
        self.ser.baud_rate = self.baud_rate
        self.ser.timeout = read_delay
        self.ser.port = self.serial_port
        self.ser.open()
        #socket opening
        self.sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", self.socket))
        self.conn, self.addr = self.sock.accept()
        print 'Connected by', addr
        while self.stay_connected:
            from_socket = self.conn.recv(self.num_bytes)
            self.ser.write(from_socket)
            from_ser = self.ser.read(self.num_bytes)
            self.conn.sendall(from_ser)
            time.sleep(read_delay)
    def close():
        self.ser.close()
        
        
        