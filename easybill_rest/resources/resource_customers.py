from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceCustomers(ResourceAbstract):
    __endpoint: str = "/customers"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_customers(self, params: dict = {}) -> dict:
        """get_customers returns a dict with customer objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_customer(self, customer_id: str) -> dict:
        """get_customer returns the referenced (id) customer"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + customer_id),
            self.__client.get_basic_headers_for_json())

    def create_customer(self, payload: dict) -> dict:
        """create_customer returns the customer model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_customer(self, customer_id: str, payload: dict) -> dict:
        """update_customer updates the reference (id) customer with the given payload. Returns the updated customer model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_customer(self, customer_id: str) -> None:
        """delete_document returns None on success and raises an exception if the customer couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + customer_id),
            self.__client.get_basic_headers())
