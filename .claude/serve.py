import http.server
import os

os.chdir('/Users/takagiyuki/Desktop/CladeCode/pianotane')
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', 8765), handler)
httpd.serve_forever()
