import serial
import time


#defining functions
def wait_ms(sleeping):
    time.sleep(sleeping/1000)

def send_string_msg():
    print("message sent\n")
    serial0.write(str.encode("Hello\r\n"))
    wait_ms(1000)

def send_hex_d6_HIGH():
    print("message sent\n")
    message = b'\xAA\x44\x1C\x01\x02\x06\x01'
    serial0.write(message)
    wait_ms(1000)

def send_hex_d6_LOW():
    print("message sent\n")
    message = b'\xAA\x44\x1C\x01\x02\x06\x00'
    serial0.write(message)
    wait_ms(1000)

#initialize serial port
serial0 = serial.Serial(
     port='/dev/serial0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=1
)
