import requests
from constants import USERNAME, PASSWORD
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class Authentication:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_jsessionid(self, username, password):
        api = '/j_security_check'
        url = self.base_url + api
        payload = {
            'j_username': username,
            'j_password': password
        }

        response = requests.post(url, data=payload, verify=False)
        if response.status_code != 200:
            print('Login Failed:', response.status_code)
            exit()
        
        jsessionid = response.cookies.get('JSESSIONID')
        return {"JSESSIONID": jsessionid}
    
    def get_token(self, jsessionid):

        api = '/dataservice/client/token'
        url = self.base_url + api
        response = requests.get(url, cookies=jsessionid, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            return None
    
if __name__ == '__main__':
    Auth = Authentication('https://10.10.20.90')
    jsessionid = Auth.get_jsessionid(USERNAME, PASSWORD)
    print(jsessionid)
    token = Auth.get_token(jsessionid)
    print(token)