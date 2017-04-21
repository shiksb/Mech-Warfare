right_vertical, right_horizontal, left_vertical, left_horizontal, butts = 0,0,0,0,0
from pygame import time
import random 
import Tkinter as tk

master = tk.Tk()
master.mainloop()
x0, y0, x1, y1 = 0,0,0,0
canvas =  tk.Canvas(master, width=100, height=100)
line = canvas.create_line(x0, y0, x1, y1)


# while 1:
# 	time.wait(100)
# 	right_vertical = random.randint(1,100)
# 	right_horizontal = random.randint(1,100)
# 	left_vertical = random.randint(1,100)
# 	left_horizontal = random.randint(1,100)
# 	# butts = random.randint()
# 	print right_vertical, right_horizontal, left_vertical,left_horizontal, butts
