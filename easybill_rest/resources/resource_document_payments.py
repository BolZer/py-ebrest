from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceDocumentPayments(ResourceAbstract):
    _endpoint: str = "/document-payments"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_document_payments(self, params: dict = None) -> dict:
        """get_document_payments returns a dict with document payments objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_document_payment(self, document_payment_id: str) -> dict:
        """get_document_payment returns the referenced (id) document payment"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_payment_id),
            self._client.get_basic_headers_for_json()
        )

    def create_document_payment(self, payload: dict) -> dict:
        """create_document_payment returns the document payment model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def delete_document_payment(self, document_payment_id: str) -> None:
        """delete_document_payment returns None on success and raises an exception if the document payment couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_payment_id),
            self._client.get_basic_headers()
        )
