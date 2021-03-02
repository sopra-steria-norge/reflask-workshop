#  Simplified solution adapted from Andrew Hyndman. 
#  https://medium.com/@fingon.aj/hot-reloading-with-react-and-flask-b5dae60d9898

from requests import get

# Simple reverse proxy for use with webpack-dev-server.
def proxyRequest(host, path):
    response = get(host + path)

    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    ]
    headers = {
        name: value
        for name, value in response.raw.headers.items()
        if name.lower() not in excluded_headers
    }
    return (response.content, response.status_code, headers)