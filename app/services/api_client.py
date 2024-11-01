from enum import Enum

from requests import Response, request


class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class ApiClient:
    def __init__(self):
        ...

    def get(self, url: str, **kwargs) -> Response:
        return self.request(Method.GET, url, **kwargs)

    def post(self, url: str, **kwargs) -> Response:
        return self.request(Method.POST, url, **kwargs)

    def request(self, method: Method, url: str, **kwargs) -> Response:
        response = request(method.value, url, **kwargs)
        return response

    def log_request(self, method: Method, url: str, **kwargs):
        ...

    def log_response(self, method: Method, url: str, **kwargs):
        ...
