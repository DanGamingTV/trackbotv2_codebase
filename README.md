# trackbotv2_codebase
Code for my EV3 4wd bot running on remo.

## Physical setup
I have a total of 4 large EV3 motors, 2 in the front (facing forwards)
And 2 in the back (facing backwards)

Port layout:
Port A - Front left motor
Port B - Front right motor
Port C - Back left motor
Port D - Back right motor

## Prerequisites
Install ev3dev on your EV3 (I used LEGO's official micropython image)

Clone the remo.tv controller somewhere on your computer, then open in vscode.

Install the [ev3dev visual studio code extension](https://marketplace.visualstudio.com/items?itemName=ev3dev.ev3dev-browser)

Download the trackbot.py file into the hardware directory of the controller.

Copy controller.sample.conf to controller.conf, and edit according to instructions [here](https://github.com/remotv/controller#configure-the-controller) - but disable video and audio.

Changes to be made for EV3:
```ini
[robot]
type=trackbot

[camera]
# Disable video
no_camera=true

# Disable mic
no_mic=true


# Specify the audio / video encoder you are using here. Currently ffmpeg,
# ffmpeg-arecord and none. Note: Only robots with Raspberry Pi's or other Linux
# based controllers  should use ffmpeg-arecord. All others should use ffmpeg or 
# none.
type=none
```

Connect to your brick through the ev3dev device browser

Download your workspace to the EV3.

### On the EV3

Get an SSH connection to your EV3 (Instructions [Here](https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh))

Get your EV3 connected to the internet (Instructions [Here](https://www.ev3dev.org/docs/networking))

Install pip3
```sh
sudo apt install python-pip3
```

Go into the controller directory (or whatever it's named)
```sh
cd controller
```

Install required pip modules
```sh
sudo pip3 -r ./requirements.txt
```
## Starting the controller

Make sure you're in the controller directory

Run this command
```sh
brickrun -- python3 controller.py
```

Enter your password when prompted

It has a tendency to just stop on the first run, so you may have to repeat the above command until it works.

# Getting video to remo
How you do this is completely up to you, the reason you can't send video or audio from the EV3 is because it isn't powerful enough to handle encoding video.

## How I do it
My setup has an iPhone mounted on my bot, running the DroidCam App.
I have a computer (windows) running the droidcam reciever (making the phone's video feed available as a webcam device), then I use this FFMPEG command to stream it to remo.
(edit this accordingly)
```sh
ffmpeg -f dshow -video_size 640x480 -i video="DroidCam Source 3" -f mpegts -codec:v mpeg1video -b:v 1000k -bf 0 -muxdelay 0.001  -headers "Authorization: Bearer APIKEY" http://remo.tv:1567/transmit?name=CHANNELID-video
```
APIKEY is the api key you get from remo for your robot
CHANNELID is the ID of the channel on the remo website. To get this, go to your robot's channel and at the end the ID will look something like rbot-f2735305-7e81-4173-a8da-928ba35659c4