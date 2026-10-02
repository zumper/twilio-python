import unittest

from twilio.base.page import Page


class LoadPageTestCase(unittest.TestCase):
    RECORDS = [{'phone_number': '+15625684337'}]

    def load(self, payload):
        return Page.__new__(Page).load_page(payload)

    def test_without_signalwire_filter_keys(self):
        payload = {'uri': '/x', 'available_phone_numbers': self.RECORDS}
        self.assertEqual(self.RECORDS, self.load(payload))

    def test_with_signalwire_filter_keys(self):
        payload = {
            'uri': '/x',
            'filters': {'AreaCode': '562'},
            'ignored_parameters': [],
            'available_phone_numbers': self.RECORDS,
        }
        self.assertEqual(self.RECORDS, self.load(payload))
