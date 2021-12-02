from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourcePostBoxes(ResourceAbstract):
    __endpoint: str = "/post-boxes"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_post_boxes(self, params: dict = None) -> dict:
        """get_post_boxes returns a dict with post box objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_post_box(self, post_box_id: str) -> dict:
        """get_post_box returns the referenced (id) post box"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + post_box_id),
            self.__client.get_basic_headers_for_json())

    def delete_post_box(self, post_box_id: str) -> None:
        """delete_post_box returns None on success and raises an exception if the post box couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + post_box_id),
            self.__client.get_basic_headers())
