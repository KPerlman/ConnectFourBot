import time
import board
import busio
from adafruit_pca9685 import PCA9685


offsets = [1, 6, 10, 6, 15, 2, 0, 9]  
servo_count = len(offsets)
pca = None
# Setup I2C

def servo_setup():
    global pca
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = PCA9685(i2c)
    pca.frequency = 50  
    for n in range(servo_count):
        set_angle(n, 0)

def set_angle(channel, angle):
    corrected_angle = angle + offsets[channel]

    
    if corrected_angle < 0:
        corrected_angle = 0
    if corrected_angle > 180:
        corrected_angle = 180

    pulse_min = 450
    pulse_max = 2550

    pulse = pulse_min + (corrected_angle / 180.0) * (pulse_max - pulse_min)
    duty = int(pulse / 20000 * 65535)

    pca.channels[channel].duty_cycle = duty
    
def power_off_servos():
    for ch in range(servo_count):  
        pca.channels[ch].duty_cycle = 0
        
def human_move(move):
    print("Human move")
    set_angle(move, 90)
    time.sleep(1)
    set_angle(move, 0)
    time.sleep(1)
    
def computer_move(move):
    print("Computer move")
    set_angle(move, 90)  # example difference
    time.sleep(3)
    set_angle(move, 0)
    time.sleep(1)
