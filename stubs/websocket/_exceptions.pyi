# Stubs for websocket._exceptions (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class WebSocketException(Exception): ...
class WebSocketProtocolException(WebSocketException): ...
class WebSocketPayloadException(WebSocketException): ...
class WebSocketConnectionClosedException(WebSocketException): ...
class WebSocketTimeoutException(WebSocketException): ...
class WebSocketProxyException(WebSocketException): ...

class WebSocketBadStatusException(WebSocketException):
    status_code: Any = ...
    def __init__(self, message, status_code) -> None: ...

class WebSocketAddressException(WebSocketException): ...