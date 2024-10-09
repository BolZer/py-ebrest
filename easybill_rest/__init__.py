import httpx

from easybill_rest.resources.resource_attachments import ResourceAttachments
from easybill_rest.resources.resource_contacts import ResourceContacts
from easybill_rest.resources.resource_customer_groups import ResourceCustomerGroups
from easybill_rest.resources.resource_customers import ResourceCustomers
from easybill_rest.resources.resource_discount_position_groups import ResourceDiscountPositionGroups
from easybill_rest.resources.resource_discount_positions import ResourceDiscountPositions
from easybill_rest.resources.resource_document_payments import ResourceDocumentPayments
from easybill_rest.resources.resource_documents import ResourceDocuments
from easybill_rest.resources.resource_logins import ResourceLogins
from easybill_rest.resources.resource_pdf_templates import ResourcePdfTemplates
from easybill_rest.resources.resource_position_groups import ResourcePositionGroups
from easybill_rest.resources.resource_positions import ResourcePositions
from easybill_rest.resources.resource_post_boxes import ResourcePostBoxes
from easybill_rest.resources.resource_projects import ResourceProjects
from easybill_rest.resources.resource_sepa_payments import ResourceSepaPayments
from easybill_rest.resources.resource_serial_numbers import ResourceSerialNumbers
from easybill_rest.resources.resource_stocks import ResourceStocks
from easybill_rest.resources.resource_tasks import ResourceTasks
from easybill_rest.resources.resource_text_templates import ResourceTextTemplates
from easybill_rest.resources.resource_time_trackings import ResourceTimeTrackings
from easybill_rest.resources.resource_webhooks import ResourceWebhooks
from easybill_rest.resources.resource_document_versions import ResourceDocumentVersions


class Client:
    _version: str = "0.6.0"
    _base_url: str = "https://api.easybill.de"
    _httpx: httpx.Client

    api_key: str = ""
    timeout: int

    def __init__(self, api_key: str, timeout: int = 10) -> None:
        self.timeout = timeout
        self.api_key = api_key
        self._httpx = httpx.Client(timeout=timeout)

    def get_basic_headers(self) -> dict:
        """get_basic_headers returns the basic headers used by the client. Contains auth and
        agent. """

        return {
            "Authorization": "Bearer " + self.api_key,
            "User-Agent": "py-ebrest " + self._version
        }

    def get_basic_headers_for_json(self) -> dict:
        """get_basic_headers_for_json returns the basic headers extended with a
        json content type."""

        return {
            **self.get_basic_headers(),
            **{'Content-type': 'application/json'}
        }

    def get_basic_headers_for_pdf(self) -> dict:
        """get_basic_headers_for_pdf returns the basic headers extended with a pdf content type."""

        return {
            **self.get_basic_headers(),
            **{'Content-type': 'application/pdf'}
        }

    def documents(self) -> ResourceDocuments:
        """documents returns the documents resource which exposes the api documents resource."""

        return ResourceDocuments(self)

    def document_payments(self) -> ResourceDocumentPayments:
        """document_payments returns the document payments resource which exposes the ap
        i document payments resource."""

        return ResourceDocumentPayments(self)

    def customers(self) -> ResourceCustomers:
        """customers returns the customers resource which exposes the api customers resource."""

        return ResourceCustomers(self)

    def customer_groups(self) -> ResourceCustomerGroups:
        """customer_groups returns the customers groups resource which exposes the
         api customer groups resource."""

        return ResourceCustomerGroups(self)

    def positions(self) -> ResourcePositions:
        """positions returns the positions resource which exposes the api positions resource."""

        return ResourcePositions(self)

    def position_groups(self) -> ResourcePositionGroups:
        """position_groups returns the position groups resource which exposes
        the api position groups resource."""

        return ResourcePositionGroups(self)

    def logins(self) -> ResourceLogins:
        """logins returns the logins resource which exposes the api logins resource."""

        return ResourceLogins(self)

    def pdf_templates(self) -> ResourcePdfTemplates:
        """pdf_templates returns the pdf-templates resource which exposes the api
        pdf-templates resource."""

        return ResourcePdfTemplates(self)

    def post_boxes(self) -> ResourcePostBoxes:
        """post_boxes returns the post box resource which exposes the api post-box resource."""

        return ResourcePostBoxes(self)

    def projects(self) -> ResourceProjects:
        """projects returns the projects resource which exposes the api projects resource."""

        return ResourceProjects(self)

    def tasks(self) -> ResourceTasks:
        """tasks returns the tasks resource which exposes the api tasks resource."""

        return ResourceTasks(self)

    def time_trackings(self) -> ResourceTimeTrackings:
        """time_trackings returns the time tracking resource which exposes the
        api time tracking resource."""

        return ResourceTimeTrackings(self)

    def stocks(self) -> ResourceStocks:
        """stocks returns the stocks resource which exposes the api stocks resource."""

        return ResourceStocks(self)

    def serial_numbers(self) -> ResourceSerialNumbers:
        """serial_numbers returns the serial number resource which exposes the api serial number
        resource."""

        return ResourceSerialNumbers(self)

    def sepa_payments(self) -> ResourceSepaPayments:
        """sepa_payments returns the sepa payments resource which exposes the sepa payment
        resource."""

        return ResourceSepaPayments(self)

    def webhooks(self) -> ResourceWebhooks:
        """webhooks returns the webhooks resource which exposes the webhook resource."""

        return ResourceWebhooks(self)

    def contacts(self) -> ResourceContacts:
        """contacts returns the contacts resource which exposes the contact resource."""

        return ResourceContacts(self)

    def text_templates(self) -> ResourceTextTemplates:
        """text_templates returns the text template resource which exposes the text template
        resource."""

        return ResourceTextTemplates(self)

    def discount_positions(self) -> ResourceDiscountPositions:
        """discount_positions returns the position discount resource which exposes the position
        discount resource."""

        return ResourceDiscountPositions(self)

    def discount_position_groups(self) -> ResourceDiscountPositionGroups:
        """discount_position_groups returns the position group discount resource which exposes
        the position group discount resource."""

        return ResourceDiscountPositionGroups(self)

    def attachments(self) -> ResourceAttachments:
        """attachments returns the attachments resource which exposes the attachment resource."""

        return ResourceAttachments(self)

    def document_versions(self) -> ResourceDocumentVersions:
        """document_versions returns the document versions resource which exposes the document
        version resource."""

        return ResourceDocumentVersions(self)

    def call(
            self,
            method: str,
            request_url: str,
            headers: dict,
            passed_payload=None) -> dict:
        """
            call calls the easybill api with the prepared connection.
            :raises: RequestException
        """

        if passed_payload is None:
            passed_payload = {}

        if method == "GET":
            response = self._httpx.request(
                method,
                self._base_url + request_url,
                headers=headers,
                params=passed_payload,
                timeout=self.timeout
            )
            response.raise_for_status()

            return response.json()

        if method in ("PUT", "POST"):
            response = self._httpx.request(
                method,
                self._base_url + request_url,
                headers=headers,
                json=passed_payload,
                timeout=self.timeout
            )
            response.raise_for_status()

            return response.json()

        if method == "DELETE":
            response = self._httpx.request(
                method,
                self._base_url + request_url,
                headers=headers,
                timeout=self.timeout
            )

            response.raise_for_status()
            return {}

        response = self._httpx.request(
            method,
            self._base_url + request_url,
            headers=headers,
            timeout=self.timeout
        )
        response.raise_for_status()

        return response.json()

    def upload(self, request_url: str, headers: dict, file: bytes) -> dict:
        """
            upload calls the easybill api with the prepared connection to upload the
            passed bytes / file.
            :raises: RequestException
        """

        response = self._httpx.post(
            self._base_url + request_url,
            headers=headers,
            timeout=self.timeout,
            files={'file': file}
        )
        response.raise_for_status()

        return response.json()

    def download(self, request_url: str, headers: dict) -> bytes:
        """
            download calls the easybill api with the prepared connection to download the
            referenced attachment.
            :raises: RequestException
        """

        response = self._httpx.get(
            self._base_url + request_url,
            headers=headers,
            timeout=self.timeout)
        response.raise_for_status()

        return response.content
