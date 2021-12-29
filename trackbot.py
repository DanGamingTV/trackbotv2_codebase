from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

""" motors = {
    front: {
        left: Motor(Port.A),
        right: Motor(Port.B)
    },
    back: {
        left: Motor(Port.C),
        right: Motor(Port.D)
    }
} """
stationary_mode = False
motor_front_left = LargeMotor(OUTPUT_A)
motor_front_right = LargeMotor(OUTPUT_B)
motor_back_left = LargeMotor(OUTPUT_C)
motor_back_right = LargeMotor(OUTPUT_D)
global_speed = 360*2 #degrees per second
global_angle_drive_interval = 360*0.65

def stationary_on():
    global stationary_mode
    stationary_mode = True


def stationary_off():
    global stationary_mode
    stationary_mode = False


#front_drive = DriveBase(motor_front_left, motor_front_right, 40, 195)
#back_drive = DriveBase(motor_back_left, motor_back_right, 40, 195)

# Write your program here.




#drive_forward_angle(global_speed, global_angle_drive_interval)
#drive_backwards_angle(global_speed, global_angle_drive_interval)
#drive_left_angle(global_speed, global_angle_drive_interval)
#drive_right_angle(global_speed, global_angle_drive_interval)
#front_drive.turn(360)
#back_drive.turn(360)

def setup(robot_config):
    print('ok')
    #motor_front_left = Motor(Port.A)
    #motor_front_right = Motor(Port.B)
    #motor_back_left = Motor(Port.C)
    #motor_back_right = Motor(Port.D)

    
    drive_forward_angle(global_speed, global_angle_drive_interval)

def drive_forward_angle(speed, angle):
    #motor_front_left.run_angle(speed, angle, Stop.BRAKE, False)
    #motor_front_right.run_angle(speed, angle, Stop.BRAKE, False)
    #motor_back_left.run_angle(speed, -angle, Stop.BRAKE, False)
    #motor_back_right.run_angle(speed, -angle, Stop.BRAKE, False)
    motor_front_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    motor_front_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    motor_back_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    motor_back_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    
def drive_backwards_angle(speed, angle):
    #motor_front_left.run_angle(speed, -angle, Stop.BRAKE, False)
    #motor_front_right.run_angle(speed, -angle, Stop.BRAKE, False)
    #motor_back_left.run_angle(speed, angle, Stop.BRAKE, False)
    #motor_back_right.run_angle(speed, angle, Stop.BRAKE, False)
    motor_front_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    motor_front_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    motor_back_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    motor_back_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    
def drive_right_angle(speed, angle):
    #motor_front_left.run_angle(speed, angle, Stop.BRAKE, False)
    #motor_front_right.run_angle(speed, -angle, Stop.BRAKE, False)
    #motor_back_left.run_angle(speed, -angle, Stop.BRAKE, False)
    #motor_back_right.run_angle(speed, angle, Stop.BRAKE, False)
    motor_front_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    motor_front_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    motor_back_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    motor_back_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    
def drive_left_angle(speed, angle):
    #motor_front_left.run_angle(speed, -angle, Stop.BRAKE, False)
    #motor_front_right.run_angle(speed, angle, Stop.BRAKE, False)
    #motor_back_left.run_angle(speed, angle, Stop.BRAKE, False)
    #motor_back_right.run_angle(speed, -angle, Stop.BRAKE, False)
    motor_front_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)
    motor_front_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    motor_back_left.on_for_degrees(speed=SpeedDPS(global_speed), degrees=angle, brake=True, block=False)
    motor_back_right.on_for_degrees(speed=SpeedDPS(global_speed), degrees=-angle, brake=True, block=False)

def move(args):
    command = args['button']['command']
    print(command, 'lol')
    if (stationary_mode == False):
        if command == 'f':
            drive_forward_angle(global_speed, global_angle_drive_interval)
        elif command == 'b':
            drive_backwards_angle(global_speed, global_angle_drive_interval)
        elif command == 'l':
            drive_left_angle(global_speed, global_angle_drive_interval)
        elif command == 'r':
            drive_right_angle(global_speed, global_angle_drive_interval)