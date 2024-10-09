from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceProjects(ResourceAbstract):
    __endpoint: str = "/projects"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_projects(self, params: dict = {}) -> dict:
        """get_projects returns a dict with project objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_project(self, project_id: str) -> dict:
        """get_project returns the referenced (id) project"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + project_id),
            self.__client.get_basic_headers_for_json())

    def create_project(self, payload: dict) -> dict:
        """create_project returns the project model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )

    def update_project(self, project_id: str, payload: dict) -> dict:
        """update_project updates the reference (id) project with the given payload. Returns the updated project model"""

        return self.__client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self.__endpoint +
                "/" +
                project_id),
            self.__client.get_basic_headers_for_json(),
            payload)

    def delete_project(self, project_id: str) -> None:
        """delete_project returns None on success and raises an exception if the project couldn't be deleted"""

        self.__client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self.__endpoint + "/" + project_id),
            self.__client.get_basic_headers())
