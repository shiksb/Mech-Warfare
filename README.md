Folders:

What's this folder called "tools"?
Contains files used by the kinematics engine, ignore it. 

How to test poses?
1. Upload pypose.ino on the ArbotiX.
2. Go to the pypose folder. Run PyPose.py on your computer

What are all these random Python scripts?

joystick.py
A module that reads the joysticks which are connected to your computer, and returns button and joystick values.

controller.py
A module that uses the joystick module to get the joystick values, and then sends it on the serial monitor. Takes 1 command line argument - the port to which ArbotiX is connected.

kinematics.py
A script that generates a folder called "sketch", which contains the files to be uploaded to the ArbotiX. Open the sketch folder and upload sketch.ino to the ArbotiX.