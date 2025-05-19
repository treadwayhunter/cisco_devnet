from creds import get_auth_token
import requests
import time
import json

def json_print(json_data):
    print(json.dumps(json_data, indent=4))

def create_project(name: str):
    url = "https://10.10.20.85/dna/intent/api/v1/template-programmer/project"

    payload = {
        "name": name
    }
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', url, headers=headers, json=payload, verify=False)
    json_print(response.json())

def get_projects():
    url = "https://10.10.20.85/dna/intent/api/v1/template-programmer/project"
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request('GET', url, headers=headers, verify=False)
    #print(response.json())
    projects = response.json()
    return projects

def get_project_by_name(name: str):
    projects = get_projects()
    #target_project = None
    for project in projects:
        #print(project['name'])
        if project['name'] == name:
            print(project['name'])
            return project

def create_template(project_id: str, name: str, desc: str):
    url = f"https://10.10.20.85/dna/intent/api/v1/template-programmer/project/{project_id}/template"
    payload = {
        "name": name,
        "description": desc,
        "language": "JINJA",
        "templateContent": "banner motd {{ BANNER }}",
        "deviceTypes": [
            {
                "productFamily": "Switches and Hubs"
            }
        ],
        "softwareType": "IOS-XE",
        "softwareVariant": "",
    }
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers=headers, json=payload, verify=False)
    print(response.json())
    task = response.json()
    return task # an async task is returned that must be polled

def poll_task(task: str, max_attempts: int = 10):
    print('TASK')
    json_print(task)
    url = 'https://10.10.20.85' + task['response']['url']
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    for attempt in range(max_attempts):
        response = requests.get(url, headers=headers, verify=False)

        if response.status_code == 200:
            task_data = response.json()
            task_response = task_data.get('response', {})
            is_error = task_response.get('isError', False)

            if 'progress' in task_response or 'endTime' in task_response:
                print(f'Task progress: {task_response.get('progress')}')
                if is_error:
                    print("Task failed")
                else:
                    print('Task completed successfully')
                return task_response
            else:
                print(f'Received status: {response.status_code}. Retrying...')

        time.sleep(5)

# url: /dna/intent/api/v1/network-device'
# method: GET
# gets and returns a list of all network devices

def get_network_devices():
    url = 'https://10.10.20.85/dna/intent/api/v1/network-device'
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request('GET', url, headers=headers, verify=False)
    #json_print(response.json())
    device_list = response.json()['response']
    return device_list

# returns a list of templates associated with a project
# url /dna/intent/api/v1/template-programmer/project/{project_id}/template
def get_project_templates(project_id: str):
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    url = f'https://10.10.20.85/dna/intent/api/v1/template-programmer/project/{project_id}/template'
    response = requests.request('GET', url, headers=headers, verify=False)
    #json_print(response.json())
    project_templates = response.json()
    return project_templates

def get_template_by_name():
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    url = 'https://10.10.20.85/dna/intent/api/v1/template-programmer/template'

    response = requests.request('GET', url, headers=headers, verify=False)
    #json_print(response.json())
    templates = response.json()
    for template in templates:
        print(template['name'])

def commit_template(template_id: str):
    print("COMMIT TEMPLATE")
    print(template_id)
    token = get_auth_token()
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    url = f'https://10.10.20.85/dna/intent/api/v1/templates/{template_id}/versions/commit'
    response = requests.request('POST', url, headers=headers, verify=False)
    print(response.text.encode('utf8'))
# These are the network devices
#bfea531c-f8ff-476f-91c7-def7953b7706
#c6cd2772-05e7-41b0-b5cc-e7d1a3a86fc8
#322e2706-3c57-45fb-bb2d-ce91db3e38a6
#19423f63-ee4f-44dc-bbf6-240586297ed2

if __name__ == '__main__':
    iteration = '001'
    project_name = 'New Project' + iteration
    template_name = 'Template' + iteration
    #create_project(project_name)
    project = get_project_by_name(project_name) # slow, but works
    #task = create_template(project_id=project['id'], name=template_name, desc=f'My {iteration} Template')
    #poll_task(task)

    #device_list = get_network_devices()
    #print(device_list)
    #for device in device_list:
    #    print(device['id'])

    # create project
    # create template with project id
    # commit template
    # deploy template

    #get_template_by_name()
    project_templates = get_project_templates(project['id'])
    target_template = None
    for template in project_templates:
        if template['name'] == template_name:
            target_template = template
            break
    if not target_template:
        exit()
    
    template_id = target_template['id']
    print(template_id)
    commit_template(template_id)

    