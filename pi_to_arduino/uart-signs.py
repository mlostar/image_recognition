#diode should be added to Rasperry PI's RX pin
import serial
import time
from recognize_func import *
from Uart_Transmit_and_Receive import *
sign_result=bytes(7)
TRAFFIC_SIGN_BYTES=b'\xAA\x44\x1C\x12\x01'
def _Pi_Serial_Catch():
    current_step=0
    current_byte=0
    while(1):
        current_byte=serial0.read()
        print(current_byte)
        if(current_step==len(TRAFFIC_SIGN_BYTES)):
            sign_result=which_sign(int(current_byte))
            message = b'\xAA\x44\x1C\x12\x01'+sign_result
            #print(message)
            current_step=0
        if current_byte==TRAFFIC_SIGN_BYTES[current_step]:
            current_step += 1
        else:
            current_step=0
_Pi_Serial_Catch()