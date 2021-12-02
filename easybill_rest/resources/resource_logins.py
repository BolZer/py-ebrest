from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceLogins(ResourceAbstract):
    __endpoint: str = "/logins"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_logins(self, params: dict = None) -> dict:
        """get_logins returns a dict with login objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_login(self, login_id: str) -> dict:
        """get_login returns the referenced (id) login"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint + "/" + login_id),
            self.__client.get_basic_headers_for_json()
        )
