from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceTasks(ResourceAbstract):
    _endpoint: str = "/tasks"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_tasks(self, params: dict = None) -> dict:
        """get_tasks returns a dict with task objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_task(self, task_id: str) -> dict:
        """get_task returns the referenced (id) task"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint + "/" + task_id),
            self._client.get_basic_headers_for_json()
        )

    def create_task(self, payload: dict) -> dict:
        """create_task returns the task model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def update_task(self, task_id: str, payload: dict) -> dict:
        """update_task updates the reference (id) task with the given payload. Returns the updated task model"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(self._endpoint + "/" + task_id),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def delete_task(self, task_id: str) -> None:
        """delete_task returns None on success and raises an exception if the task couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(self._endpoint + "/" + task_id),
            self._client.get_basic_headers()
        )
