from roqaba.settings import environ
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from stem import Signal
from stem.control import Controller


def new_tor_identity():
    with Controller.from_port(port=environ["TOR_CONTROL_PORT"]) as controller:
        controller.authenticate(password=environ["TOR_CONTROL_PASSWORD"])
        controller.signal(Signal.NEWNYM)


class ProxyMiddleware(HttpProxyMiddleware):
    def process_response(self, request, response, spider):
        # Get a new identity depending on the response
        if response.status != 200:
            new_tor_identity()
            return request
        return response

    def process_request(self, request, spider):
        # Set the Proxy
        # A new identity for each request
        # Comment out if you want to get a new Identity only through process_response
        new_tor_identity()
        request.meta["proxy"] = f"http://127.0.0.1:{environ['PRIVOXY_PORT']}"
