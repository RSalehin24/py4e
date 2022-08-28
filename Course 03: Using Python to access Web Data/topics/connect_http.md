## Socket

### declaration
```python
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(request)

while True:
  data = my_socket.recv(512)
  if(len(data) < 1):
    break;
  print(data.decode())

my_socket.close()
```

### Beautiful Soup 

> A library which extract required data from http; http as different flows in real implementation by the developer, beautiful soup ca extract despite this flaws, it's not simply possible for a developer to write all the variations which can take forever

