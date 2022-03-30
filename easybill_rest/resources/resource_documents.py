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
    __endpoint: str = "/documents"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_documents(self, params: dict = None) -> dict:
        """get_documents returns a dict with document objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_document(self, document_id: str) -> dict:
        """get_document returns the referenced (id) document"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + document_id),
            self.__client.get_basic_headers_for_json())

    def create_document(self, payload: dict) -> dict:
        """create_document returns the document model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_document(self, document_id: str, payload: dict, params: dict = None) -> dict:
        """update_document updates the reference (id) document with the given payload. Returns the updated document"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id,
                params
            ),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_document(self, document_id: str) -> None:
        """delete_document returns None on success and raises an exception if the document couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + document_id),
            self.__client.get_basic_headers())

    def finalize_document(self, document_id: str) -> dict:
        """finalize_document returns the finalized document on success"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/done"),
            self.__client.get_basic_headers_for_json())

    def cancel_document(self, document_id: str) -> dict:
        """cancel_document returns the canceled document on success"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/cancel"),
            self.__client.get_basic_headers_for_json())

    def send_document(
            self,
            document_id: str,
            send_method: SendMethod,
            payload: dict) -> None:
        """send_document returns None on success and rises exception on failure"""

        self.__client.call(
            "POST",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/send/" +
                str(send_method)),
            self.__client.get_basic_headers_for_json(),
            payload)

    def download_document(self, document_id: str) -> bytes:
        """download_document returns the document as bytes on success"""

        return self.__client.download(
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/pdf"),
            self.__client.get_basic_headers_for_pdf(),
        )
