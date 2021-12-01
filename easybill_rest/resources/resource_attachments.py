from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceAttachments(ResourceAbstract):
    _endpoint: str = "/attachments"
    _client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_attachments(self, params: dict = None) -> dict:
        """get_attachments returns a dict with attachment objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_attachment(self, attachment_id: str) -> dict:
        """get_attachment returns the referenced (id) attachment"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(
                self._endpoint + "/" + attachment_id),
            self._client.get_basic_headers_for_json())

    def create_attachment(self, payload: bytes) -> dict:
        """create_attachment returns the attachment model as dict on success with the data from the passed payload"""

        return self._client.upload(
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers(),
            payload
        )

    def update_attachment(self, attachment_id: str, payload: dict) -> dict:
        """update_attachment updates the reference (id) attachment with the given payload. Returns a part of the updated attachment model"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self._endpoint +
                "/" +
                attachment_id),
            self._client.get_basic_headers_for_json(),
            payload)

    def delete_attachment(self, attachment_id: str) -> None:
        """delete_attachment returns None on success and raises an exception if the attachment couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self._endpoint +
                "/" +
                attachment_id),
            self._client.get_basic_headers())

    def get_content(self, attachment_id: str, headers: dict = None) -> bytes:
        """get_content returns None on success and raises an exception if the attachment couldn't be deleted"""

        return self._client.download(
            Helper.create_request_url_from_params(
                self._endpoint + "/" + attachment_id),
            self._client.get_basic_headers())
