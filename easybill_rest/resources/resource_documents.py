from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class SendMethod(Enum):
    EMAIL = "email"
    FAX = "fax"
    POST = "post"


class ResourceDocuments(ResourceAbstract):
    _endpoint: str = "/documents"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_documents(self, params: dict = None) -> dict:
        """get_documents returns a dict with document objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_document(self, document_id: str) -> dict:
        """get_document returns the referenced (id) document"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id),
            self._client.get_basic_headers_for_json()
        )

    def create_document(self, payload: dict) -> dict:
        """create_document returns the document model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def update_document(self, document_id: str, payload: dict) -> dict:
        """update_document updates the reference (id) document with the given payload. Returns the updated document"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def delete_document(self, document_id: str) -> None:
        """delete_document returns None on success and raises an exception if the document couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id),
            self._client.get_basic_headers_for_json()
        )

    def finalize_document(self, document_id: str) -> dict:
        """finalize_document returns the finalized document on success"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id + "/done"),
            self._client.get_basic_headers_for_json()
        )

    def cancel_document(self, document_id: str) -> dict:
        """cancel_document returns the canceled document on success"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id + "/cancel"),
            self._client.get_basic_headers_for_json()
        )

    def send_document(self, document_id: str, send_method: SendMethod, payload: dict) -> None:
        """send_document returns None on success and rises exception on failure"""

        self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id + "/send/" + str(send_method)),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def download_document(self, document_id: str) -> bytes:
        """download_document returns the document as bytes on success"""

        return self._client.download(
            Helper.create_request_url_from_params(self._endpoint + "/" + document_id + "/pdf"),
            self._client.get_basic_headers_for_pdf(),
        )
