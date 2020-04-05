import pynput.mouse as p
import time as t
m,x,y=p.Controller(),1,1
while 1:
    m.move(x,y)
    t.sleep(1e-9)
    x=-x if m.position[0] in[1918,0] else x
    y=-y if m.position[1] in[1198,0] else y