from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
from pathlib import Path


# Using Path for across OS's
certfile = Path("Insert/cert/file/path")

# Handles the HTTPServer Address and port
httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
# Makes sure to add certfile=certfile to call the file
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, server_side=True)
httpd.serve_forever()
