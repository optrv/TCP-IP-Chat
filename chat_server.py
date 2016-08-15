import socket

def input_urname(fn):
    def welcome(*urname):
        urname = input('Please, input your name: ')
        if urname != '':
            fn(urname)
        fn(*urname)
    return welcome

@input_urname
def conn(urname = 'Anonymous'):
    print('Hello, ' + urname.upper() + '!')
    print('Welcome to Chat!')
    print('*Waiting for connection...*')
    ssocket = socket.socket()
    # For debug
    try:
        ssocket.bind(('', 8080))
    except OSError:
        ssocket.close()
        ssocket.bind(('', 9090))
    ssocket.listen(1)
    connect, address = ssocket.accept()
    # Receive its name
    itsname = connect.recv(1024)
    itsname = itsname.decode("utf-8")
    print (itsname + " is connected!")
    print("*Waiting for %s...*" % itsname.upper())
    # Send your name
    urname = urname.encode("utf-8")
    connect.send(urname)

    while True:
        data = connect.recv(1024)
        data = data.decode("utf-8")
        print(itsname.upper() + ": " + data)
        msg = input("YOU: ")
        msg = msg.encode("utf-8")
        connect.send(msg)
        print("*Waiting for %s...*" % itsname.upper())
        if not data:
            break

    connect.close()

def main():
    conn()

if __name__ == '__main__':
    main()