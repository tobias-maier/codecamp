from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body style='background-color:powderblue;'>", "utf-8"))
        self.wfile.write(bytes("<h1>Hallo Sidney,hallo Spenc</h1>", "utf-8"))
        self.wfile.write(bytes("<h1>Hallo Sidney,hallo Spenc</h1>", "utf-8"))
        self.wfile.write(bytes("<h2>fffghgsdfgfdgh</h2>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")