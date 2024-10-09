import unittest

from easybill_rest.tests.test_abstract_resource import TestAbstractResource
from easybill_rest.tests.test_attachments import TestResourceAttachments
from easybill_rest.tests.test_client import TestClient
from easybill_rest.tests.test_contacts import TestResourceContacts
from easybill_rest.tests.test_customer_groups import TestResourceCustomerGroups
from easybill_rest.tests.test_customers import TestResourceCustomers
from easybill_rest.tests.test_discount_position_groups import TestResourceDiscountPositionGroups
from easybill_rest.tests.test_discount_positions import TestResourceDiscountPositions
from easybill_rest.tests.test_document_payments import TestResourceDocumentPayments
from easybill_rest.tests.test_documents import TestResourceDocuments
from easybill_rest.tests.test_helper import TestHelper
from easybill_rest.tests.test_logins import TestResourceLogins
from easybill_rest.tests.test_pdf_templates import TestResourcePdfTemplates
from easybill_rest.tests.test_position_groups import TestResourcePositionGroups
from easybill_rest.tests.test_positions import TestResourcePositions
from easybill_rest.tests.test_post_boxes import TestResourcePostBoxes
from easybill_rest.tests.test_projects import TestResourceProjects
from easybill_rest.tests.test_sepa_payments import TestResourceSepaPayments
from easybill_rest.tests.test_serial_numbers import TestResourceSerialNumbers
from easybill_rest.tests.test_stocks import TestResourceStocks
from easybill_rest.tests.test_tasks import TestResourceTasks
from easybill_rest.tests.test_test_case_abstract import TestEaybillTestCaseAbstract
from easybill_rest.tests.test_text_templates import TestResourceTextTemplates
from easybill_rest.tests.test_webhooks import TestResourceWebhooks
from easybill_rest.tests.test_document_versions import TestResourceDocumentVersions


class UnitTestSuite(unittest.TestSuite):

    @staticmethod
    def get_unit_test_suite() -> unittest.TestSuite:
        return unittest.TestSuite([
            TestClient.get_suite(),
            TestHelper.get_suite(),
            TestAbstractResource.get_suite(),
            TestResourceDocuments.get_suite(),
            TestResourceCustomers.get_suite(),
            TestResourcePositions.get_suite(),
            TestResourceAttachments.get_suite(),
            TestResourceContacts.get_suite(),
            TestResourceCustomerGroups.get_suite(),
            TestResourceDiscountPositionGroups.get_suite(),
            TestResourceDiscountPositions.get_suite(),
            TestResourceDocumentPayments.get_suite(),
            TestResourceLogins.get_suite(),
            TestResourcePdfTemplates.get_suite(),
            TestResourcePositionGroups.get_suite(),
            TestResourcePostBoxes.get_suite(),
            TestResourceProjects.get_suite(),
            TestResourceSepaPayments.get_suite(),
            TestResourceSerialNumbers.get_suite(),
            TestResourceStocks.get_suite(),
            TestResourceTasks.get_suite(),
            TestResourceTextTemplates.get_suite(),
            TestResourceWebhooks.get_suite(),
            TestResourceDocumentVersions.get_suite(),
            TestEaybillTestCaseAbstract.get_suite()
        ])


unittest.TextTestRunner(verbosity=2).run(UnitTestSuite.get_unit_test_suite())
