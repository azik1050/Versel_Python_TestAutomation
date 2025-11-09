import typing
import httpx
from httpx import Auth, Request, Response


class BasicAuth(Auth):
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        request.headers['Authorization'] = httpx.BasicAuth(
            self.__username,
            self.__password
        )._auth_header
        yield request
