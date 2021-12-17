from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    queue = []

    def do_GET(self):
       
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print(self.queue)
        for i in self.queue:
            self.wfile.write(i.encode()+" ".encode())
        
   
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        if len(self.queue) < 5:
            self.queue.append(str(body.decode()))
        else:
            self.queue.pop(0)
            self.queue.append(str(body.decode()))

        self.wfile.write(response.getvalue())
        print(self.queue)

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()