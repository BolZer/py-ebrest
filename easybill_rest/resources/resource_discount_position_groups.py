from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceDiscountPositionGroups(ResourceAbstract):
    __endpoint: str = "/discounts/position-group"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_position_group_discounts(self, params: dict = None) -> dict:
        """get_position_group_discounts returns a dict with position group discount objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_position_group_discount(
            self, position_group_discount_id: str) -> dict:
        """get_position_group_discount returns the referenced (id) position group discount"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                position_group_discount_id),
            self.__client.get_basic_headers_for_json())

    def create_position_group_discount(self, payload: dict) -> dict:
        """create_position_group_discount returns the position group discount model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_position_group_discount(
            self,
            position_group_discount_id: str,
            payload: dict) -> dict:
        """update_position_group_discount updates the reference (id) position group discount with the given payload. Returns the updated position group discount model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                position_group_discount_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_position_group_discount(
            self, position_group_discount_id: str) -> None:
        """delete_position_group_discount returns None on success and raises an exception if the discount couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                position_group_discount_id),
            self.__client.get_basic_headers())
