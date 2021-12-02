from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceContacts(ResourceAbstract):
    __endpoint: str = "/customers"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_contacts(self, customer_id: str, params: dict = None) -> dict:
        """get_contacts returns a dict with contact objects for the referenced customer"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_id +
                "/" +
                "contacts",
                params),
            self.__client.get_basic_headers_for_json())

    def get_contact(self, customer_id: str, contact_id: str) -> dict:
        """get_contact returns the referenced (id) contact for the referenced customer"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_id +
                "/" +
                "contacts" +
                "/" +
                contact_id),
            self.__client.get_basic_headers_for_json())

    def create_contact(self, customer_id: str, payload: dict) -> dict:
        """create_contact returns the contact model as dict on success with the data from the passed payload for the referenced customer"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_id +
                "/" +
                "contacts"),
            self.__client.get_basic_headers_for_json(),
            payload)

    def update_contact(
            self,
            customer_id: str,
            contact_id: str,
            payload: dict) -> dict:
        """update_contact updates the reference (id) contact with the given payload. Returns the updated contact model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_id +
                "/" +
                "contacts" +
                "/" +
                contact_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_contact(self, customer_id: str, contact_id: str) -> None:
        """delete_contact returns None on success and raises an exception if the contact couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                customer_id +
                "/" +
                "contacts" +
                "/" +
                contact_id),
            self.__client.get_basic_headers())
