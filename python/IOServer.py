#_*_ coding:utf-8 _*_
import socket,select
s = socket.socket()
#host = socket.gethostname()
port = 1234
#s.bind((host,port))
s.bind(('localhost',port))
s.listen(5)
inputs = [s]
while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr = s.accept()
            print '获取连接来自：',addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print r.getpeername(),'disconnected'
                inputs.remove(r)
            else:
                print data
        