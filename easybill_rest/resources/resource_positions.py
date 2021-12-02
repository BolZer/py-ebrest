from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourcePositions(ResourceAbstract):
    __endpoint: str = "/positions"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_positions(self, params: dict = None) -> dict:
        """get_positions returns a dict with position objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_position(self, position_id: str) -> dict:
        """get_position returns the referenced (id) position"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + position_id),
            self.__client.get_basic_headers_for_json())

    def create_position(self, payload: dict) -> dict:
        """create_position returns the position model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_position(self, position_id: str, payload: dict) -> dict:
        """update_position updates the reference (id) position with the given payload. Returns the updated position model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                position_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_position(self, position_id: str) -> None:
        """delete_position returns None on success and raises an exception if the position couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + position_id),
            self.__client.get_basic_headers())
