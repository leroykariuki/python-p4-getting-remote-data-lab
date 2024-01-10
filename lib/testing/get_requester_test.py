import unittest
from GetRequester import GetRequester

class GetRequesterTest(unittest.TestCase):
    '''Class {Classname} in {modulename}.py'''
    URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
    CONVERTED_DATA = [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
                      {'name': 'Joe', 'occupation': 'WiFi Fixer'},
                      {'name': 'Avi', 'occupation': 'DJ'},
                      {'name': 'Howard', 'occupation': 'Mountain Legend'}]

    def test_get_response(self):
        '''get_response_body function returns response.'''
        requester = GetRequester(GetRequesterTest.URL)
        actual_json_data = requester.load_json()

        expected_json_data = GetRequesterTest.CONVERTED_DATA

        self.assertEqual(actual_json_data, expected_json_data)

    def test_load_json(self):
        '''load_json function returns response.'''
        requester = GetRequester(GetRequesterTest.URL)
        self.assertEqual(requester.load_json(), GetRequesterTest.CONVERTED_DATA)

if __name__ == '__main__':
    unittest.main()
