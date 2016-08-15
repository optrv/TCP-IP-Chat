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
    ssocket = socket.socket()
    ssocket.connect(('', 8080))
    # Send your name
    ssocket.send(urname.encode('utf-8'))
    # Receive its name
    itsname = ssocket.recv(1024)
    itsname = itsname.decode("utf-8")
    print("You start the chat with " + itsname.upper() + "!")

    while True:
        msg = input("YOU: ")
        ssocket.send(msg.encode('utf-8'))
        print("*Waiting for %s...*" % itsname.upper())
        data = ssocket.recv(16000)
        data = data.decode("utf-8")
        print(itsname.upper() + ": " + data)
        if not data:
            break

    ssocket.close()

def main():
    conn()

if __name__ == '__main__':
    main()
