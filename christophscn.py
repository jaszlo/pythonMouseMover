import pynput.mouse as m,time
c=m.Controller()
d=1,1
r=1918,1078
while 1:c.move(*d);time.sleep(1e-3);d=[d[i]if 0<c.position[i]<r[i]else -d[i]for i in[0,1]]