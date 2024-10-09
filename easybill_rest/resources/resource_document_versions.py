from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceDocumentVersions(ResourceAbstract):
    __endpoint: str = "/documents"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_document_versions(self, document_id: str, params: dict = {}) -> dict:
        """get_document_versions returns a dict with version items for the requested document"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/" +
                "versions",
                params),
            self.__client.get_basic_headers_for_json())

    def get_document_version(self, document_id: str, document_version_id: str) -> dict:
        """get_document_version returns a dict with the request document version for the document"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/" +
                "versions" +
                "/" +
                document_version_id),
            self.__client.get_basic_headers_for_json())

    def download_document_version_item(
            self,
            document_id: str,
            document_version_id: str,
            document_version_item_id: str,
    ) -> bytes:
        """download_document_version_item downloads the request document version item as bytes. This may be a pdf,
        XML or PDF containing a XML file"""

        return self.__client.download(
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                document_id +
                "/" +
                "versions" +
                "/" +
                document_version_id +
                "/items/" +
                document_version_item_id +
                "/download"),
            self.__client.get_basic_headers_for_pdf(),
        )
