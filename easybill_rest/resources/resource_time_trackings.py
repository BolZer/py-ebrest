from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceTimeTrackings(ResourceAbstract):
    _endpoint: str = "/time-trackings"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_time_trackings(self, params: dict = None) -> dict:
        """get_time_tracking returns a dict with time tracking objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_time_tracking(self, time_tracking_id: str) -> dict:
        """get_time_tracking returns the referenced (id) time tracking"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint + "/" + time_tracking_id),
            self._client.get_basic_headers_for_json()
        )

    def create_time_tracking(self, payload: dict) -> dict:
        """create_time_tracking returns the time tracking model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def update_time_tracking(self, time_tracking_id: str, payload: dict) -> dict:
        """update_task updates the reference (id) time tracking with the given payload. Returns the updated time tracking model"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(self._endpoint + "/" + time_tracking_id),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def delete_time_tracking(self, task_id: str) -> None:
        """delete_time_tracking returns None on success and raises an exception if the time tracking couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(self._endpoint + "/" + task_id),
            self._client.get_basic_headers()
        )
