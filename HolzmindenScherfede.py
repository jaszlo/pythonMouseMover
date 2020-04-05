import pynput.mouse as m,time
c,d,r=m.Controller(),[1,1],[1918,1078]
while 1:
    c.move(*d)
    time.sleep(1e-9)
    d=[-d[i]if c.position[i]in[0,r[i]]else d[i]for i in[0,1]]
