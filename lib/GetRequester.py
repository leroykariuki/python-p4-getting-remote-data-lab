import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error sending GET request: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body is not None:
            try:
                json_data = json.loads(response_body)
                return json_data
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None

if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    
    response_body = requester.get_response_body()
    print("Response Body:")
    print(response_body)

    json_data = requester.load_json()
    print("\nJSON Data:")
    print(json_data)
