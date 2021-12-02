from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceStocks(ResourceAbstract):
    __endpoint: str = "/stocks"
    __client: Client

    def __init__(self, client: Client) -> None:
        super().__init__()
        self.__client = client

    def get_resource_endpoint(self):
        return self.__endpoint

    def get_stocks(self, params: dict = None) -> dict:
        """get_stocks returns a dict with stock objects"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint, params),
            self.__client.get_basic_headers_for_json()
        )

    def get_stock(self, stock_id: str) -> dict:
        """get_stock returns the referenced (id) stock object"""

        return self.__client.call(
            "GET",
            Helper.create_request_url_from_params(self.__endpoint + "/" + stock_id),
            self.__client.get_basic_headers_for_json()
        )

    def create_stock(self, payload: dict) -> dict:
        """create_stock returns the stock model as dict on success with the data from the passed payload"""

        return self.__client.call(
            "POST",
            Helper.create_request_url_from_params(self.__endpoint),
            self.__client.get_basic_headers_for_json(),
            payload
        )
