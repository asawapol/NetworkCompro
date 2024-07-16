import socket
import select
import errno

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 1234))
sock.setblocking(0)

data = 'foobar\n' * 10 * 1024 * 1024 #70 MB of data
data_size = len(data)
print('Bytes to send: ', len(data))# True

total_sent = 0
while len(data):
    try:
        sent = sock.send(data.encode())
        total_sent += sent
        data = data[sent:]
        print ('Sending data')

    except socket.error as e:
        if e.errno != errno.EAGAIN:
            raise e
        print ('Blocking with', len(data), 'remaining')
        select.select([], [sock], [])

        assert total_sent == data_size