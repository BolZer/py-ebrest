from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceDocumentPayments(ResourceAbstract):
    __endpoint: str = "/document-payments"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_document_payments(self, params: dict = {}) -> dict:
        """get_document_payments returns a dict with document payments objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_document_payment(self, document_payment_id: str) -> dict:
        """get_document_payment returns the referenced (id) document payment"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_payment_id),
            self.__client.get_basic_headers_for_json())

    def create_document_payment(self, payload: dict) -> dict:
        """create_document_payment returns the document payment model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def delete_document_payment(self, document_payment_id: str) -> None:
        """delete_document_payment returns None on success and raises an exception if the document payment couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_payment_id),
            self.__client.get_basic_headers())
