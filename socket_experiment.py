import socket

def raw_http_get(host, path="/", port=80):
    """
    TODO: 
    1. Create a socket object
    2. Connect it to (host, port)
    3. Build the HTTP GET request string (see format above)
    4. Send it, encoded as bytes
    5. Receive the response in a loop until there's nothing left
    6. Decode and return the full response as a string
    GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n
    """

    socket_obj = socket.socket()
    socket_obj.connect((host, port))

    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    socket_obj.send(request.encode())

    chunks = []

    while True:
        chunk = socket_obj.recv(4096)
        if not chunk:
            break
        chunks.append(chunk)

    chunks = b"".join(chunks)
    chunks = chunks.decode()
    
    return chunks

    pass    


if __name__ == "__main__":
    response = raw_http_get("info.cern.ch")
    print(response)