from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceCustomerGroups(ResourceAbstract):
    __endpoint: str = "/customer-groups"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_customer_groups(self, params: dict = {}) -> dict:
        """get_customer_groups returns a dict with customer groups objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_customer_group(self, customer_group_id: str) -> dict:
        """get_customer_group returns the referenced (id) customer group"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_group_id),
            self.__client.get_basic_headers_for_json())

    def create_customer_group(self, payload: dict) -> dict:
        """create_customer_group returns the customer group model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_customer_group(
            self,
            customer_group_id: str,
            payload: dict) -> dict:
        """update_customer_group updates the reference (id) customer group with the given payload. Returns the updated customer group model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_group_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_customer_group(self, customer_group_id: str) -> None:
        """delete_customer_group returns None on success and raises an exception if the customer-group couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_group_id),
            self.__client.get_basic_headers())
