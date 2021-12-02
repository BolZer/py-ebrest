from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceWebhooks(ResourceAbstract):
    __endpoint: str = "/webhooks"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_webhooks(self, params: dict = None) -> dict:
        """get_webhooks returns a dict with webhook objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_webhook(self, webhook_id: str) -> dict:
        """get_webhook returns the referenced (id) webhook"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + webhook_id),
            self.__client.get_basic_headers_for_json())

    def create_webhook(self, payload: dict) -> dict:
        """create_webhook returns the webhook model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_webhook(self, webhook_id: str, payload: dict) -> dict:
        """update_webhook updates the reference (id) webhook with the given payload. Returns the updated webhook model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                webhook_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_webhook(self, webhook_id: str) -> None:
        """delete_webhook returns None on success and raises an exception if the webhook couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + webhook_id),
            self.__client.get_basic_headers())
