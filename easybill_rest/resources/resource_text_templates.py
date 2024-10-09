from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceTextTemplates(ResourceAbstract):
    __endpoint: str = "/text-templates"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_text_templates(self, params: dict = {}) -> dict:
        """get_text_templates returns a dict with text templates objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_text_template(self, text_template_id: str) -> dict:
        """get_text_template returns the referenced (id) text template"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                text_template_id),
            self.__client.get_basic_headers_for_json())

    def create_text_template(self, payload: dict) -> dict:
        """create_text_template returns the text template model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_text_template(
            self,
            text_template_id: str,
            payload: dict) -> dict:
        """update_text_template updates the reference (id) task with the given payload. Returns the updated text template model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                text_template_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_text_template(self, text_template_id: str) -> None:
        """delete_text_template returns None on success and raises an exception if the text template couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                text_template_id),
            self.__client.get_basic_headers())
