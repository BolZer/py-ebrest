from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceSepaPayments(ResourceAbstract):
    _endpoint: str = "/sepa-payments"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_sepa_payments(self, params: dict = None) -> dict:
        """get_sepa_payments returns a dict with sepa payments objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_sepa_payment(self, sepa_payment_id: str) -> dict:
        """get_sepa_payment returns the referenced (id) sepa payment"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint + "/" + sepa_payment_id),
            self._client.get_basic_headers_for_json()
        )

    def create_sepa_payment(self, payload: dict) -> dict:
        """create_sepa_payment returns the sepa payment model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def update_sepa_payment(self, sepa_payment_id: str, payload: dict) -> dict:
        """update_sepa_payment updates the reference (id) sepa payment with the given payload. Returns the updated sepa payment model"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(self._endpoint + "/" + sepa_payment_id),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def delete_sepa_payment(self, sepa_payment_id: str) -> None:
        """delete_sepa_payment returns None on success and raises an exception if the sepa payment couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(self._endpoint + "/" + sepa_payment_id),
            self._client.get_basic_headers()
        )
