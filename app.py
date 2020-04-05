import pynput.mouse as p, time
m,x,y=p.Controller(),1,1
while 1:
    m.move(x,y)
    time.sleep(1e-9)
    x*=1-2*(m.position[0] in[1918,0])    
    y*=1-2*(m.position[1] in[1078,0])
