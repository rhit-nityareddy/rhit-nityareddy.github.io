
import socket
import time
import signal
import traceback

# Live coding:
# 0. Show how you load this into your IDE.
# 1. Walk through the parts of handling a HTTP request.
# 2. Run and connect to this server in the browser.
# 3. Create a file called hello.html containing the message, "Hello, World!".
# 4. Set the response body to the read-in contents of hello.html.
#       Use "rb" for the open() mode.
#       Now you should be able to change hello.html and refresh the browser to see the changes, without restarting the server!


def main():

    server = create_connection(port = 8080)

    while True:
        # 1. Wait for the browser to send a HTTP Request
        connection_to_browser = accept_browser_connection_to(server)

        # 2. Read the HTTP Request from the browser
        reader_from_browser = connection_to_browser.makefile(mode='rb')
        try:
            request_line = reader_from_browser.readline().decode("utf-8") # decode converts from bytes to text
            print()
            print('Request:')
            print(request_line)
        except Exception as e:
            print("Error while reading HTTP Request:", e)
            traceback.print_exc() # Print what line the server crashed on.
            shutdown_connection(connection_to_browser)
            continue
        
        if(get_requested_filename(request_line) == "./shutdown"):
            print("Server shutting down")
            shutdown_connection(connection_to_browser)
            exit()
       
        # 3. Write the HTTP Response back to the browser
        writer_to_browser = connection_to_browser.makefile(mode='wb')
        try:
            # TODO: read "Hello, World!" from an HTML file instead of this encoded string.
            path = get_requested_filename(request_line)
            
            file_type = get_file_type(path)
            content = get_content_type(file_type)
            with(open(path, "rb") as fd):
                response_body = fd.read()
            content_type = content

            response_headers = "\r\n".join([
                'HTTP/1.1 200 OK',
                f'Content-Type: {content_type}',
                f'Content-length: {len(response_body)}',
                'Connection: close',
                '\r\n'
            ]).encode("utf-8") # encode converts strings to raw bytes

            # These lines just PRINT the HTTP Response to your Terminal.
            print()
            print('Response headers:')
            print(response_headers)
            print()
            print('Response body:')
            print(response_body)
            print()

            # These lines do the real work; they WRITE the HTTP Response to the Browser.
            writer_to_browser.write(response_headers)
            writer_to_browser.write(response_body)
            writer_to_browser.flush()
        except Exception as e:
            print("Error while writing HTTP Response:", e)
            traceback.print_exc() # print what line the server crashed on
    
        shutdown_connection(connection_to_browser)



# Don't worry about the details of the rest of the code below.
# It is VERY low-level code for creating the underlying connection to the browser.

def create_connection(port):
    addr = ("", port)  # "" = all network adapters; usually what you want.
    server = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True) # prevent rare IPV6 softlock on localhost connections
    server.settimeout(2)
    print(f'Server started on port {port}. Try: http://localhost:{port}/index.html')
    return server

def accept_browser_connection_to(server):
    while True:
        try:
            (conn, address) = server.accept()
            conn.settimeout(2)
            return conn
        except socket.timeout:
            print(".", end="", flush=True)
        except KeyboardInterrupt:
            exit(0)

def shutdown_connection(connection_to_browser):
    connection_to_browser.shutdown(socket.SHUT_RDWR)
    connection_to_browser.close()

def get_requested_filename(request_line):
    parts = request_line.split()
    path = "./" + parts[1]
    return path

def get_file_type(requested_filename):
    if(requested_filename.endswith('.png')):
        return '.png'
    if(requested_filename.endswith('.html')):
        return '.html'
    if(requested_filename.endswith('.jpeg')):
        return '.jpeg'
    if(requested_filename.endswith('.ico')):
        return '.ico'
    if(requested_filename.endswith('.js')):
        return '.js'
    if(requested_filename.endswith('.css')):
        return '.css'
    
    
def get_content_type(requested_file_extension):
    if(requested_file_extension == '.png'):
        return 'image/png'
    if(requested_file_extension == '.html'):
        return 'text/html; charset=utf-8'
    if(requested_file_extension == '.jpeg'):
        return 'image/jpeg'
    if(requested_file_extension == '.ico'):
        return 'image/x-icon'
    if(requested_file_extension == '.js'):
        return 'text/javascript; charset=utf-8'
    if(requested_file_extension == '.css'):
        return 'text/css; charset=utf-8'
    

if __name__ == "__main__":
    print()
    main()