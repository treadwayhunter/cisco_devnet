import requests
from constants import USERNAME, PASSWORD, json_print
from authentication import Authentication
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from getpass import getpass

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

    def create_user(self, userName: str):
        password: str = getpass('User Password: ')
        confirm_password: str = getpass('Confirm Password: ')

        if password != confirm_password:
            print('Passwords do not match!')
            exit()

        data = {
            "userName": userName,
            "password": password,
            "group": ["netadmin"],
            "description": "A new user",
            "locale": "en_US"
        }

        api = '/dataservice/admin/user/'
        url = self.base_url + api
        response = requests.post(url, headers=self.headers, cookies=self.cookies, json=data, verify=False)
        print(response.status_code)
        print(response.text)


    def delete_user(self, userName: str):
        api = f'/dataservice/admin/user/{userName}'
        url = self.base_url + api
        response = requests.delete(url, headers=self.headers, cookies=self.cookies, verify=False)
        print(response.status_code)
        print(response.text)

    def print_users(self):
        if self.users:
            for user in self.users:
                print(user['userName'])

if __name__ == '__main__':
    base_url = 'https://10.10.20.90'
    print('administration.py')
    administration = Administration(base_url)
    print('Get All Users')
    print('----------------------------')
    administration.get_users()
    print('----------------------------')
    print('Create User')
    print('----------------------------')
    administration.create_user('treadwayh')
    print('----------------------------')
    print('Get All Users')
    print('----------------------------')
    administration.get_users()
    print('----------------------------')
    print('Delete User')
    print('----------------------------')
    administration.delete_user('treadwayh')
    print('----------------------------')
    print('Get All Users')
    print('----------------------------')
    administration.get_users()


    