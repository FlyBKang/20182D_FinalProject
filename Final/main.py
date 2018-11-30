import random
import math
from  globalParamiter import*
from framework import *


elapsed_time = 0.00
hide_cursor()

import sys
print("Memory Locate: " + str((sys.getsizeof(Global) + sys.getsizeof(Texture) + sys.getsizeof(Timer))) + "Byte")

while(True):
    elapsed_time = get_time()
    clear_canvas()
    Input()
    Draw()
    update_canvas()
    Timer.Time_Frame = get_time() - elapsed_time
    if(Global.pause == False):
        Timer.Sec_Per_Frame += Timer.Time_Frame
        if(Timer.Sec_Per_Frame > Timer.IntTime + 1):
            Timer.IntTime += 1
    else:
        Timer.Time_Start += Timer.Time_Frame
        Timer.Time_Frame = 0

    #print(Timer.Sec_Per_Frame)
    #print(Timer.IntTime)
    #print(Timer.Time_Frame)
    #print(get_time() - Timer.Time_Start)



