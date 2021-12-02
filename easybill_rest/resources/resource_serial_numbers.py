from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceSerialNumbers(ResourceAbstract):
    __endpoint: str = "/serial-numbers"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_serial_numbers(self, params: dict = None) -> dict:
        """get_serial_numbers returns a dict with serial number objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_serial_number(self, serial_number_id: str) -> dict:
        """get_serial_number returns the referenced (id) serial number"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                serial_number_id),
            self.__client.get_basic_headers_for_json())

    def create_serial_number(self, payload: dict) -> dict:
        """create_serial_number returns the serial number model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def delete_serial_number(self, serial_number_id: str) -> None:
        """delete_serial_number returns None on success and raises an exception if the serial number couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                serial_number_id),
            self.__client.get_basic_headers())
