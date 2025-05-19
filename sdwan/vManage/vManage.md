# vManage
## Authentication
https://developer.cisco.com/docs/sdwan/authentication/

Different from DNAC or ISE.
SD-WAN vManage access control is based on sessions. The user enters a session after successful login. The following are typical steps for a user to consume the API:
1) Log in with a username and password to establish a session: POST /j_security_check 
    ```
    POST https://{vmanage-ip-address}/j_security_check
    Content-Type: application/x-www-form-urlencoded
    HTTP Body: "j_username={admin}&j_password={credential}"
    ```
    The token is in the cookie JSESSIONID={session hash}

