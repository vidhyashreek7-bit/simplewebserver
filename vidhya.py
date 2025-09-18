from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>device description</title>
    </head>
    <body>
        <h2 align="center">Device decription-25008027</h2>
        <table border="3">
            <tr>
                <th>S.NO</th>
                <th>Device specification</th>
                <th>description</th>
            </tr>
            <tr>
                <td>1</td>
                <td>storage</td>
                <td>954</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Graphics card</td>
                <td>128GB</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>16.0</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Processor</td>
                <td>Intel(R)core(TM) ultra 5 125H</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Device name</td>
                <td>Laptop-S2BBCOQ4</td>                
                
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()