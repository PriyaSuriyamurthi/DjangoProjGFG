import requests

class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)



def compute():
    word = input("Enter the word: ")
    request_url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=d69dfc9b-d8d1-4ce8-8389-c5409ed8c2e3"
    resp = requests.get(request_url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise APIError('GET /tasks/ {}'.format(resp.status_code))
    for todo_item in resp.json():
        print('{}'.format(todo_item))
