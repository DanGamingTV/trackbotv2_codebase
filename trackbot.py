from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM

# Initialise the EV3 (Our interfaces for using EV3 motors, sensors, etc)
ev3 = EV3Brick()

# Set up our motors
# This assumes a physical configuration like this:
# Front set (facing forward) [motor_front_left] [motor_front_right]
# Back set (facing backward) [motor_back_left]   [motor_back_right]
motor_front_left = LargeMotor(OUTPUT_A)
motor_front_right = LargeMotor(OUTPUT_B)
motor_back_left = LargeMotor(OUTPUT_C)
motor_back_right = LargeMotor(OUTPUT_D)


# Changing Paramaters - These paramaters can be changed over the application lifecycle to change how the robot behaves with commands, etc.
# TODO: Check if movement commands are from server/robot owners, and whitelist commands from said user.
stationary_mode = False # When this is enabled, no robot movement is allowed


global_speed = 360*2 #degrees per second
global_angle_drive_interval = 360*0.65

def stationary_on():
    global stationary_mode
    stationary_mode = True

def stationary_off():
    global stationary_mode
    stationary_mode = False

def setup(robot_config):
    print('Remo.TV Called setup')
    drive_forward_angle(global_speed, global_angle_drive_interval)

def do_robot_drive(front_left, front_right, back_left, back_right): # Each of these paramaters should be defined with a config dictionary, with properties 'speed', 'angle', 'brake', and 'block'
    # Loop over configs for each motor, and prefill any paramaters that were left out
    config_list = [front_left, front_right, back_left, back_right]
    for config in config_list:
        if 'speed' not in config:
            config['speed'] = global_speed
        elif 'brake' not in config:
            config['brake'] = True
        elif 'block' not in config:
            config['block'] = False
    # Run our motors with the paramaters provided
    motor_front_left.on_for_degrees(speed=SpeedDPS(front_left['speed']), degrees=front_left['angle'], brake=True, block=False)    # Front Left Motor
    motor_front_right.on_for_degrees(speed=SpeedDPS(front_right['speed']), degrees=front_right['angle'], brake=True, block=False) # Front Right Motor
    motor_back_left.on_for_degrees(speed=SpeedDPS(back_left['speed']), degrees=back_left['angle'], brake=True, block=False)       # Back Left Motor
    motor_back_right.on_for_degrees(speed=SpeedDPS(back_right['speed']), degrees=back_right['angle'], brake=True, block=False)    # Back Right Motor

def drive_forward_angle(speed, angle):
    do_robot_drive(
        {'degrees': angle},  # Front Left Motor Config
        {'degrees': angle},  # Front Right Motor Config
        {'degrees': -angle}, # Back Left Motor Config
        {'degrees': -angle}  # Back Right Motor Config
    )

    
def drive_backwards_angle(speed, angle):
    do_robot_drive(
        {'degrees': -angle},  # Front Left Motor Config
        {'degrees': -angle},  # Front Right Motor Config
        {'degrees': angle}, # Back Left Motor Config
        {'degrees': angle}  # Back Right Motor Config
    )
    
def drive_right_angle(speed, angle):
    do_robot_drive(
        {'degrees': angle},  # Front Left Motor Config
        {'degrees': -angle},  # Front Right Motor Config
        {'degrees': -angle}, # Back Left Motor Config
        {'degrees': angle}  # Back Right Motor Config
    )
    
def drive_left_angle(speed, angle):
    do_robot_drive(
        {'degrees': -angle},  # Front Left Motor Config
        {'degrees': angle},  # Front Right Motor Config
        {'degrees': angle}, # Back Left Motor Config
        {'degrees': -angle}  # Back Right Motor Config
    )


def move(args):
    command = args['button']['command']
    print(command, 'called from Remo.TV')
    if (stationary_mode == False):
        if command == 'f':
            drive_forward_angle(global_speed, global_angle_drive_interval)
        elif command == 'b':
            drive_backwards_angle(global_speed, global_angle_drive_interval)
        elif command == 'l':
            drive_left_angle(global_speed, global_angle_drive_interval)
        elif command == 'r':
            drive_right_angle(global_speed, global_angle_drive_interval)