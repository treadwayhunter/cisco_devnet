import requests
from constants import USERNAME, PASSWORD

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
        try:
            cookies = response.headers['set-cookie']
            jsessionid = cookies.split(';')
            return(jsessionid[0])
        except:
            print('No valid JSESSION ID returned\n')
            exit()
    
    def get_token(self, jsessionid):
        headers = {
            'Cookie': jsessionid
        }
        api = '/dataservice/client/token'
        url = self.base_url + api
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return(response.text)
        else:
            return None
    
if __name__ == '__main__':
    Auth = Authentication('https://10.10.20.90')
    jsessionid = Auth.get_jsessionid(USERNAME, PASSWORD)
    print(jsessionid)
    token = Auth.get_token(jsessionid)
    print(token)