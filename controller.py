<<<<<<< HEAD
#!/usr/bin/env python

import time, sys, serial
import wx
from joystick import*
import datetime

# Commander definitions
BUT_R1 = 1
BUT_R2 = 2
BUT_R3 = 4
BUT_L4 = 8
BUT_L5 = 16
BUT_L6 = 32
BUT_RT = 64
BUT_LT = 128

width = 300

# class Commander(wx.Frame):
#     TIMER_ID = 100

#     def __init__(self, parent, ser, debug = False):  
#         wx.Frame.__init__(self, parent, -1, "ArbotiX Commander", style = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
#         self.ser = ser    

#         sizer = wx.GridBagSizer(10,10)

#         self.drive = wx.Panel(self,size=(width,width-20))
#         self.drive.SetBackgroundColour('WHITE')
#         self.drive.Bind(wx.EVT_MOTION, self.onMove)  
#         wx.StaticLine(self.drive, -1, (width/2, 0), (1,width), style=wx.LI_VERTICAL)
#         wx.StaticLine(self.drive, -1, (0, width/2), (width,1))
#         sizer.Add(self.drive,(0,0),wx.GBSpan(2,1),wx.EXPAND|wx.ALL,5)
#         self.forward = 0
#         self.turn = 0

#         # Selection for horizontal movement
#         horiz = wx.StaticBox(self, -1, 'Horizontal Movement')
#         horiz.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
#         horizBox = wx.StaticBoxSizer(horiz,orient=wx.VERTICAL) 

#         self.selTurn = wx.RadioButton(self, -1, 'Turn', style=wx.RB_GROUP)
#         horizBox.Add(self.selTurn)        
#         self.selStrafe = wx.RadioButton(self, -1, 'Strafe')
#         horizBox.Add(self.selStrafe)        
#         sizer.Add(horizBox, (0,1), wx.GBSpan(1,1), wx.EXPAND|wx.TOP|wx.RIGHT,5)

#         # Body rotations
#         body = wx.StaticBox(self, -1, 'Body Movement')
#         body.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
#         bodyBox = wx.StaticBoxSizer(body,orient=wx.VERTICAL) 
#         bodySizer = wx.GridBagSizer(5,5)

#         bodySizer.Add(wx.StaticText(self, -1, "Pan:"),(0,0), wx.GBSpan(1,1),wx.ALIGN_CENTER_VERTICAL)
#         self.pan = wx.Slider(self, -1, 0, -100, 100, wx.DefaultPosition, (200, -1), wx.SL_HORIZONTAL | wx.SL_LABELS)
#         bodySizer.Add(self.pan,(0,1))
#         bodySizer.Add(wx.StaticText(self, -1, "Tilt:"),(1,0), wx.GBSpan(1,1),wx.ALIGN_CENTER_VERTICAL)
#         self.tilt = wx.Slider(self, -1, 0, -100, 100, wx.DefaultPosition, (200, -1), wx.SL_HORIZONTAL | wx.SL_LABELS)
#         bodySizer.Add(self.tilt,(1,1))
#         bodySizer.Add(wx.StaticText(self, -1, "Roll:"),(2,0), wx.GBSpan(1,1),wx.ALIGN_CENTER_VERTICAL)
#         self.roll = wx.Slider(self, -1, 0, -100, 100, wx.DefaultPosition, (200, -1), wx.SL_HORIZONTAL | wx.SL_LABELS)
#         self.roll.Disable()
#         bodySizer.Add(self.roll,(2,1))
#         bodyBox.Add(bodySizer) 
        
#         sizer.Add(bodyBox, (1,1), wx.GBSpan(1,1), wx.EXPAND|wx.BOTTOM|wx.RIGHT,5)

#         # timer for output
#         self.timer = wx.Timer(self, self.TIMER_ID)
#         self.timer.Start(33)
#         wx.EVT_CLOSE(self, self.onClose)
#         wx.EVT_TIMER(self, self.TIMER_ID, self.onTimer)

#         self.SetSizerAndFit(sizer)
#         self.Show(True)

#     def onClose(self, event):
#         self.timer.Stop()
#         # self.sendPacket(128,128,128,128,0)
#         self.Destroy()

#     def onMove(self, event=None):
#         if event.LeftIsDown():        
#             pt = event.GetPosition()
#             self.forward = ((width/2)-pt[1])/2
#             self.turn = (pt[0]-(width/2))/2           
#         else:
#             self.forward = 0
#             self.turn = 0
#             pass

#     def onTimer(self, event=None):
#         # configure output
#         Buttons = 0
#         if self.selStrafe.GetValue():
#             Buttons = BUT_LT
#         # self.sendPacket(self.tilt.GetValue(), self.pan.GetValue(), self.forward, self.turn, Buttons, turret_motor)
#         while self.ser.inWaiting() > 0:
#             print self.ser.read(),
#         self.timer.Start(50)
        
#     def sendPacket(self, right_vertical, right_horizontal, left_vertical, left_horizontal, Buttons, turret_motor):
#         # send output
#         # print(left_vertical,left_horizontal)
#         # print(Buttons)
#         self.ser.write('\xFF')
#         self.ser.write(chr(right_vertical+128))
#         self.ser.write(chr(right_horizontal+128))
#         self.ser.write(chr(left_vertical+128))
#         self.ser.write(chr(left_horizontal+128))
#         self.ser.write(chr(Buttons))
#         self.ser.write(chr(turret_motor))
#         self.ser.write(chr(255 - ((right_vertical+right_horizontal+left_vertical+left_horizontal+Buttons)%256)))


ser = serial.Serial()

def sendPacket(right_vertical, right_horizontal, left_vertical, left_horizontal, Buttons, butts):
        # send output
        # print(left_vertical,left_horizontal)
        # print(Buttons)
        ser.write('\xFF')
        ser.write(chr(right_vertical+128))
        ser.write(chr(right_horizontal+128))
        ser.write(chr(left_vertical+128))
        ser.write(chr(left_horizontal+128))
        ser.write(chr(Buttons))
        ser.write(chr(butts))
        # ser.write(chr(255))
        ser.write(chr(255 - ((right_vertical+right_horizontal+left_vertical+left_horizontal+Buttons)%256)))
            
if __name__ == "__main__":

    ser.baudrate = 38400
    try:
        ser.port = sys.argv[1]
    except:
        print "Can't find serial port :'("
        sys.exit()

    # ser.port = "COM3"
    ser.timeout = 0.5
    ser.open()
    
    # app = wx.PySimpleApp()
    # app.MainLoop()

    # frame = Commander(None, ser, True)

    buttonDict = {"startButton":0}
    count = 0

    while buttonDict["startButton"] != 1:
    	# turret_motor = 1
        axisDict = updateAxes()
        buttonDict = updateButtons()
        time.sleep(0.05);
        power = 90
        left_vertical = int(axisDict['Y-Axis1']*power)
        left_horizontal = int(axisDict['X-Axis1']*power)
        right_vertical = int(axisDict['Y-Axis2']*power)
        right_horizontal = int(axisDict['X-Axis2']*power)

        # L1 + L2 + R2 + R1 + x + sq + tri + cir
        butts = int((str(buttonDict['leftBumper']) + 
        				str(buttonDict['leftTrigger']) + 
        				str(buttonDict['rightTrigger']) +
        				str(buttonDict['rightBumper']) +
        				str(buttonDict['xButton']) +
        				str(buttonDict['squareButton']) +
        				str(buttonDict['triangleButton']) +
        				str(buttonDict['circleButton'])), 2)


        print right_vertical, right_horizontal, left_vertical, left_horizontal, butts
        # if turret_motor == 0:
        # 	turret_motor = 1
        # else:
        # 	turret_motor = 0
        sendPacket(right_vertical, right_horizontal, left_vertical, left_horizontal, 128, butts)
        # if count == 100:
       	# 	buttonDict["xButton"] = 1
       	# else :
       	# 	count += 1

=======
#!/usr/bin/env python

import time, sys, serial
import wx
from joystick import*

# Commander definitions
BUT_R1 = 1
BUT_R2 = 2
BUT_R3 = 4
BUT_L4 = 8
BUT_L5 = 16
BUT_L6 = 32
BUT_RT = 64
BUT_LT = 128

width = 300

class Commander(wx.Frame):
    TIMER_ID = 100

    def __init__(self, parent, ser, debug = False):  
        wx.Frame.__init__(self, parent, -1, "ArbotiX Commander", style = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.ser = ser    

        sizer = wx.GridBagSizer(10,10)

        self.drive = wx.Panel(self,size=(width,width-20))
        self.drive.SetBackgroundColour('WHITE')
        self.drive.Bind(wx.EVT_MOTION, self.onMove)  
        wx.StaticLine(self.drive, -1, (width/2, 0), (1,width), style=wx.LI_VERTICAL)
        wx.StaticLine(self.drive, -1, (0, width/2), (width,1))
        sizer.Add(self.drive,(0,0),wx.GBSpan(2,1),wx.EXPAND|wx.ALL,5)
        self.forward = 0
        self.turn = 0

        # Selection for horizontal movement
        horiz = wx.StaticBox(self, -1, 'Horizontal Movement')
        horiz.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        horizBox = wx.StaticBoxSizer(horiz,orient=wx.VERTICAL) 

        self.selTurn = wx.RadioButton(self, -1, 'Turn', style=wx.RB_GROUP)
        horizBox.Add(self.selTurn)        
        self.selStrafe = wx.RadioButton(self, -1, 'Strafe')
        horizBox.Add(self.selStrafe)        
        sizer.Add(horizBox, (0,1), wx.GBSpan(1,1), wx.EXPAND|wx.TOP|wx.RIGHT,5)

        # Body rotations
        body = wx.StaticBox(self, -1, 'Body Movement')
        body.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        bodyBox = wx.StaticBoxSizer(body,orient=wx.VERTICAL) 
        bodySizer = wx.GridBagSizer(5,5)

        bodySizer.Add(wx.StaticText(self, -1, "Pan:"),(0,0), wx.GBSpan(1,1),wx.ALIGN_CENTER_VERTICAL)
        self.pan = wx.Slider(self, -1, 0, -100, 100, wx.DefaultPosition, (200, -1), wx.SL_HORIZONTAL | wx.SL_LABELS)
        bodySizer.Add(self.pan,(0,1))
        bodySizer.Add(wx.StaticText(self, -1, "Tilt:"),(1,0), wx.GBSpan(1,1),wx.ALIGN_CENTER_VERTICAL)
        self.tilt = wx.Slider(self, -1, 0, -100, 100, wx.DefaultPosition, (200, -1), wx.SL_HORIZONTAL | wx.SL_LABELS)
        bodySizer.Add(self.tilt,(1,1))
        bodySizer.Add(wx.StaticText(self, -1, "Roll:"),(2,0), wx.GBSpan(1,1),wx.ALIGN_CENTER_VERTICAL)
        self.roll = wx.Slider(self, -1, 0, -100, 100, wx.DefaultPosition, (200, -1), wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.roll.Disable()
        bodySizer.Add(self.roll,(2,1))
        bodyBox.Add(bodySizer) 
        
        sizer.Add(bodyBox, (1,1), wx.GBSpan(1,1), wx.EXPAND|wx.BOTTOM|wx.RIGHT,5)

        # timer for output
        self.timer = wx.Timer(self, self.TIMER_ID)
        self.timer.Start(33)
        wx.EVT_CLOSE(self, self.onClose)
        wx.EVT_TIMER(self, self.TIMER_ID, self.onTimer)

        self.SetSizerAndFit(sizer)
        self.Show(True)

    def onClose(self, event):
        self.timer.Stop()
        self.sendPacket(128,128,128,128,0)
        self.Destroy()

    def onMove(self, event=None):
        if event.LeftIsDown():        
            pt = event.GetPosition()
            self.forward = ((width/2)-pt[1])/2
            self.turn = (pt[0]-(width/2))/2           
        else:
            self.forward = 0
            self.turn = 0
            pass

    def onTimer(self, event=None):
        # configure output
        Buttons = 0
        if self.selStrafe.GetValue():
            Buttons = BUT_LT
        self.sendPacket(self.tilt.GetValue(), self.pan.GetValue(), self.forward, self.turn, Buttons)
        while self.ser.inWaiting() > 0:
            print self.ser.read(),
        self.timer.Start(50)
        
    def sendPacket(self, right_vertical, right_horizontal, left_vertical, left_horizontal, Buttons):
        # send output
        # print(left_vertical,left_horizontal)
        # print(Buttons)
        self.ser.write('\xFF')
        self.ser.write(chr(right_vertical+128))
        self.ser.write(chr(right_horizontal+128))
        self.ser.write(chr(left_vertical+128))
        self.ser.write(chr(left_horizontal+128))
        self.ser.write(chr(Buttons))
        self.ser.write(chr(0))
        self.ser.write(chr(255 - ((right_vertical+right_horizontal+left_vertical+left_horizontal+Buttons)%256)))
            
if __name__ == "__main__":

    ser = serial.Serial()
    ser.baudrate = 38400
    try:
        ser.port = sys.argv[1]
    except:
        print "Can't find serial port :'("
        sys.exit()

    # ser.port = "COM3"
    ser.timeout = 0.5
    ser.open()
    
    app = wx.PySimpleApp()
    app.MainLoop()

    frame = Commander(None, ser, True)

    buttonDict = {"xButton":0}

    while buttonDict["xButton"] != 1:
        axisDict = updateAxes()
        buttonDict = updateButtons()
        time.sleep(0.05);
        power = 90
        left_vertical = int(axisDict['Y-Axis1']*power)
        left_horizontal = int(axisDict['X-Axis1']*power)
        right_vertical = int(axisDict['Y-Axis2']*power)
        right_horizontal = int(axisDict['X-Axis2']*power)
        print right_vertical, right_horizontal, left_vertical, left_horizontal, 128
        frame.sendPacket(right_vertical, right_horizontal, left_vertical, left_horizontal, 128)

>>>>>>> 93e2a7256e586e9d1a57ab3f275c94e8b20b77ff
