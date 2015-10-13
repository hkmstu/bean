import socket
import pdb
from robots_mod import robots_mod

HOST='0.0.0.0'
PORT=2001

cmd_dic = { '\xff\x00\x01\x00\xff':'m:forward', '\xff\x00\x02\x00\xff':'m:back', \
        '\xff\x00\x03\x00\xff':'m:left', '\xff\x00\x04\x00\xff':'m:right', \
        '\xff\x00\x00\x00\xff':'m:stop'}

def set_socket():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    return s

def make_motion(rm, info_str):

    if info_str not in cmd_dic:
        return 
    part, cmd = cmd_dic[info_str].split(':')
    if  part == 'm':
        rm.action_m(cmd)
    elif part == 's':
        rm.action_s(cmd)

def main():

    #pdb.set_trace()
    # 1. init socket server.
    s = set_socket()
    # 2. init motors and servos.
    rm = robots_mod()
    # 3. execute command.
    while True:
        conn, _ = s.accept()
        while True:
            data = conn.recv(1024)
            if data not in cmd_dic:
                break
            make_motion(rm, data)
        conn.close()

if __name__ == '__main__':
    main()
