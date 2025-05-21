import requests
from constants import USERNAME, PASSWORD, json_print
from authentication import Authentication
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Administration:
    def __init__(self, base_url):
        self.base_url = base_url
        Auth = Authentication(base_url)
        jsessionid = Auth.get_jsessionid(USERNAME, PASSWORD)
        token = Auth.get_token(jsessionid)
        self.headers = {
            'X-XSRF-TOKEN': token,
            'Content-Type': 'application/json'
        }
        self.cookies = jsessionid
        self.users = []

    def get_users(self):
        api = '/dataservice/admin/user'
        url = self.base_url + api
        response = requests.get(url, headers=self.headers, cookies=self.cookies, verify=False)
        if response.status_code != 200:
            print(response.status_code)
            print('Bad request:', url)
            exit()
        users = response.json().get("data", [])
        self.users = users
        self.print_users()

    def print_users(self):
        if self.users:
            for user in self.users:
                print(user['userName'])

    def create_user(self):
        pass

    def delete_user(self):
        pass

if __name__ == '__main__':
    base_url = 'https://10.10.20.90'
    print('administration.py')
    administration = Administration(base_url)
    administration.get_users()
    