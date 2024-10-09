import unittest
from unittest import mock

from httpx import HTTPStatusError

from easybill_rest import Client
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
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestClient(unittest.TestCase, EasybillRestTestCaseAbstract):

    def test_client_version(self) -> None:
        self.assertEqual('0.6.0', Client('')._version)

    def test_client_base_url(self) -> None:
        self.assertEqual('https://api.easybill.de', Client('')._base_url)

    def test_api_key_on_client(self) -> None:
        client = Client('test')
        self.assertTrue(hasattr(client, 'api_key'))
        self.assertEqual('test', client.api_key)

    def test_client_attributes(self) -> None:
        self.assertTrue(hasattr(Client(''), '_httpx'))
        self.assertTrue(hasattr(Client(''), '_version'))
        self.assertTrue(hasattr(Client(''), '_base_url'))
        self.assertTrue(hasattr(Client(''), 'api_key'))

    def test_client_basic_headers(self) -> None:
        headers = Client("test").get_basic_headers()
        self.assertEqual("Bearer test", headers["Authorization"])

    def test_client_json_headers(self) -> None:
        headers = Client("test").get_basic_headers_for_json()
        self.assertEqual("Bearer test", headers["Authorization"])
        self.assertEqual("application/json", headers["Content-type"])

    def test_client_pdf_headers(self) -> None:
        headers = Client("test").get_basic_headers_for_pdf()
        self.assertEqual("Bearer test", headers["Authorization"])
        self.assertEqual("application/pdf", headers["Content-type"])

    def test_client_call_api_success(self) -> None:
        client = Client("Test")

        response_mock = mock.Mock()
        response_mock.status_code = mock.Mock(return_value=200)
        response_mock.json = mock.Mock(return_value={"test": "test"})

        client._httpx = mock.Mock()
        client._httpx.request = mock.Mock(return_value=response_mock)

        result = client.call("", "", {})
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(bool(result))
        self.assertEqual("test", result["test"])

    def test_client_call_api_client_exceptions(self) -> None:
        client = Client("Test")

        response_mock = mock.Mock()
        response_mock.status_code = mock.Mock(return_value=500)
        response_mock.content = bytes('{"msg": "exception"}', 'utf-8')
        response_mock.raise_for_status = mock.Mock(
            side_effect=HTTPStatusError(
                "test exception",
                request=mock.Mock(),
                response=mock.Mock()))

        client._httpx = mock.Mock()
        client._httpx.request = mock.Mock(return_value=response_mock)
        self.assertRaises(HTTPStatusError, client.call, "", "", {})

    def test_client_call_using_right_format(self) -> None:
        client = Client("Test")
        client._httpx = mock.Mock()

        header = {
            'Authorization': 'Bearer Test',
            'User-Agent': 'py-ebrest 0.6.0',
            'Content-type': 'application/json'
        }

        with mock.patch.object(Client, 'call', wraps=client.call) as clientMock:
            client.documents().update_document("1", {"is_archive": True})
            clientMock.assert_called_once_with(
                'PUT',
                '/rest/v1/documents/1',
                header,
                {"is_archive": True}
            )

        with mock.patch.object(Client, 'call', wraps=client.call) as clientMock:
            client.documents().create_document({"is_archive": True})
            clientMock.assert_called_once_with(
                'POST',
                '/rest/v1/documents',
                header,
                {"is_archive": True}
            )

        with mock.patch.object(Client, 'call', wraps=client.call) as clientMock:
            client.documents().get_document("2")
            clientMock.assert_called_once_with(
                'GET',
                '/rest/v1/documents/2',
                header,
            )

        with mock.patch.object(Client, 'call', wraps=client.call) as clientMock:
            client.documents().get_documents({"page": 2})
            clientMock.assert_called_once_with(
                'GET',
                '/rest/v1/documents?page=2',
                header,
            )

    def test_get_documents_resource(self) -> None:
        self.assertTrue(isinstance(Client('').documents(), ResourceDocuments))

    def test_get_customers_resource(self) -> None:
        self.assertTrue(isinstance(Client('').customers(), ResourceCustomers))

    def test_get_positions_resource(self) -> None:
        self.assertTrue(isinstance(Client('').positions(), ResourcePositions))

    def test_get_document_payments_resource(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').document_payments(),
                ResourceDocumentPayments))

    def test_get_logins_resource(self) -> None:
        self.assertTrue(isinstance(Client('').logins(), ResourceLogins))

    def test_get_pdf_templates_resource(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').pdf_templates(),
                ResourcePdfTemplates))

    def test_get_post_boxes_resource(self) -> None:
        self.assertTrue(isinstance(Client('').post_boxes(), ResourcePostBoxes))

    def test_get_customer_groups_resource(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').customer_groups(),
                ResourceCustomerGroups))

    def test_get_position_groups_resource(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').position_groups(),
                ResourcePositionGroups))

    def test_get_projects_resource(self) -> None:
        self.assertTrue(isinstance(Client('').projects(), ResourceProjects))

    def test_get_tasks_resource(self) -> None:
        self.assertTrue(isinstance(Client('').tasks(), ResourceTasks))

    def test_get_stocks_resource(self) -> None:
        self.assertTrue(isinstance(Client('').stocks(), ResourceStocks))

    def test_get_serial_numbers_resource(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').serial_numbers(),
                ResourceSerialNumbers))

    def test_get_sepa_payments(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').sepa_payments(),
                ResourceSepaPayments))

    def test_get_webhooks(self) -> None:
        self.assertTrue(isinstance(Client('').webhooks(), ResourceWebhooks))

    def test_get_contacts(self) -> None:
        self.assertTrue(isinstance(Client('').contacts(), ResourceContacts))

    def test_get_text_templates(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').text_templates(),
                ResourceTextTemplates))

    def test_get_discount_positions(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').discount_positions(),
                ResourceDiscountPositions))

    def test_get_discount_position_groups(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').discount_position_groups(),
                ResourceDiscountPositionGroups))

    def test_get_attachments(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').attachments(),
                ResourceAttachments))

    def test_get_time_trackings(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').time_trackings(),
                ResourceTimeTrackings))

    def test_get_document_versions(self) -> None:
        self.assertTrue(
            isinstance(
                Client('').document_versions(),
                ResourceDocumentVersions))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestClient, [
            'test_client_version',
            'test_client_base_url',
            'test_api_key_on_client',
            'test_client_attributes',
            'test_client_basic_headers',
            'test_client_json_headers',
            'test_client_pdf_headers',
            'test_client_call_using_right_format',
            'test_client_call_api_success',
            'test_client_call_api_client_exceptions',
            'test_get_documents_resource',
            'test_get_customers_resource',
            'test_get_positions_resource',
            'test_get_document_payments_resource',
            'test_get_logins_resource',
            'test_get_pdf_templates_resource',
            'test_get_post_boxes_resource',
            'test_get_customer_groups_resource',
            'test_get_position_groups_resource',
            'test_get_projects_resource',
            'test_get_tasks_resource',
            'test_get_stocks_resource',
            'test_get_serial_numbers_resource',
            'test_get_webhooks',
            'test_get_contacts',
            'test_get_text_templates',
            'test_get_discount_positions',
            'test_get_serial_numbers_resource',
            'test_get_sepa_payments',
            'test_get_webhooks',
            'test_get_contacts',
            'test_get_text_templates',
            'test_get_discount_positions',
            'test_get_discount_position_groups',
            'test_get_attachments',
            'test_get_time_trackings',
            'test_get_document_versions'
        ]))
