# Friends who haven't met yet (and who live in different places)

## Concept

I'm working on an interaction model that gives two strangers in different public spaces the opportunity engage each other in a friendly, positive way.

The basic idea is that they each approach a kiosk in their separate spaces. They see a keyboard and are invited by some signage to type something. They go for it, and as soon as they hit enter a receipt printer mounted to the kiosk spits out what they've written, in a sort of typical text-message speech bubble.

What they don't know is that another receipt printer, on an identical kiosk somewhere else, has also spit out the same thing.

Ideally, next, a person on the far side of the system sees the words spitting out and approaches their typewriter and responds. A conversation starts. Once this has begun, the system invites both users to solve a puzzle or game that requires both of their cooperation. If they complete it, they are each invited to smile for the camera, and a picture of themselves and their conversation partner will print on the receipt, which then gets cut by the printer so they can take it home with them as a momento.

## Execution

Each kiosk has a Raspberry Pi 3, a USB keyboard, a Raspberry Pi camera, and an Epson TM-120 receipt printer. In this repo I'm working on the software that each is running (written in Python 3).

As of this writing (March 7th 2017) I've been able to use [python-escpos](https://github.com/python-escpos/python-escpos) to get the printer to spit out text and images, which was a far buggier process than anticipated.

A partial list of to-dos:
* implement two-way communication via internet connection; towards this I'm contemplating using
    - websockets, 
    - HTTP GET or POST requests,
    - OSC over internet, or
    - some commercial web connectivity service
* better define the interaction flow
* add support for the camera locally
* use VNC for troubleshooting and remote updates
* successful, reliable autolaunch on machine startup