import unittest
import requests
import settings

class TestMagnificent(unittest.TestCase):

    def test_response_code(self):
        try:
            r = requests.get(settings.ENVIRONMENT_URL)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            self.fail("Could not connect to server or server did not respond before timeout.")


        self.assertEqual(r.status_code, 200, "The given URL returned an unexpected status code.")


if __name__ == '__main__':
    unittest.main()
