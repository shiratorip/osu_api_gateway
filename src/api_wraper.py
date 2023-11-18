from typing import Union

import requests
from requests import Response

from src.schemes.User import UserCompact

BASE_URL = "https://osu.ppy.sh"


class ApiWrapper(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls._instance = super(ApiWrapper, cls).__new__(cls)
        return cls._instance

    def __init__(self, client_id, client_secret):
        self.refresh_token = None
        self.__client_id: int = client_id
        self.__client_secret: str = client_secret
        self.api_token: Union[None, str] = self.get_access_token(
            {"grant_type": "client_credentials",
             "scope": "public"}
        )

    def _check_token(func):
        def wrapper(self, *args, **kwargs) -> Response:
            print('Before')
            result: Response = func(*args, **kwargs)

            if result.status_code == 401:
                self.api_token = self.get_access_token(
                    {"grant_type": "refresh_token",
                     "refresh_token": self.refresh_token
                     }
                )
                result: Response = func(*args, **kwargs)
            return result

        return wrapper

    def get_access_token(self, params) -> Union[str, None]:
        url = "https://osu.ppy.sh/oauth/token"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        body = {
            "client_id": self.__client_id,
            "client_secret": self.__client_secret,
            **params
        }

        response = requests.post(url=url, headers=headers, data=body)
        access_token = response.json().get("access_token")
        self.refresh_token = response.json().get("refresh_token")
        if not access_token:
            exit("unable to get access token")

        return access_token


    @_check_token
    def search_users(self, query: str) -> list[UserCompact]:
        users = []
        url = f"{BASE_URL}/api/v2/search"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}"
        }
        parameters = {
            "mode": "user",
            "query": query,
            "page": 1
        }
        response = requests.get(url=url, headers=headers, params=parameters)

        print(response.status_code)
        for user in response.json()["user"]["data"]:
            users.append(UserCompact(**user))

        return users
