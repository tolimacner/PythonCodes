

from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # Get the client's IP address
    client_ip = request.remote_addr

    # Resolve the hostname from the IP address
    try:
        client_hostname = socket.gethostbyaddr(client_ip)[0]
    except socket.herror:
        client_hostname = "Hostname not found"

    # Create the HTML response
    html_content = f'''
    <html>
    <head>
        <title>Server Info</title>
    </head>
    <body>
        <h1>"Hello and welcome to my website lab"</h1>
        <p>This request came from pod:</p>
        <p>Hostname: {client_hostname}</p>
        <p>IP Address: {client_ip}</p>
    </body>
    </html>
    '''
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
