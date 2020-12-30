# miezikatz
! Early development state!

Miezikatz is a portable network scanner on your Raspberry Pi. It 

  - runs network scans and
  - saves them to text files

You don't need to grab out your laptop. Just plug-in your Raspberry Pi via an ethernet cable to a switch/router/etc in the network you want to scan and use the E-Paper display to command miezikatz.


### Overview
The display used is a [Waveshare 2.7 inch](https://www.waveshare.com/2.7inch-e-paper-hat.htm) E-Paper display hat. No soldering is needed. Just put the display entity on your RPi using the GPIO pins. A powerbank is recommended.

You can simply initiate scans and shutdown the Raspberry Pi with the 4 buttons integrated on the display hat.

### Installation
Make sure, you have Python installed on your Raspberry Pi and install all dependencies with the install script.

```sh
$ git clone https://github.com/buu-huu/miezikatz
$ cd miezikatz
$ ./install.sh
```

The miezikatz process starts automatically when you power on the Raspberry Pi. By pressing button 4, the whole RPi will shutdown. 