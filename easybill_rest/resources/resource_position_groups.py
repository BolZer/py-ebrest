from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourcePositionGroups(ResourceAbstract):
    _endpoint: str = "/position-groups"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_position_groups(self, params: dict = None) -> dict:
        """get_position_groups returns a dict with position group objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_position_group(self, position_group_id: str) -> dict:
        """get_position_group returns the referenced (id) position group"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint + "/" + position_group_id),
            self._client.get_basic_headers_for_json()
        )

    def create_position_group(self, payload: dict) -> dict:
        """create_position_group returns the position group model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def update_position_group(self, position_group_id: str, payload: dict) -> dict:
        """update_position_group updates the reference (id) position group with the given payload. Returns the updated position group model"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(self._endpoint + "/" + position_group_id),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def delete_position_group(self, position_group_id: str) -> None:
        """delete_position_group returns None on success and raises an exception if the position group couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(self._endpoint + "/" + position_group_id),
            self._client.get_basic_headers()
        )
