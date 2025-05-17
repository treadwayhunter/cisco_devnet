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
        "templateContent": "banner motd {{ HOSTNAME }}",
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

if __name__ == '__main__':
    iteration = '006'
    project_name = 'New Project' + iteration
    template_name = 'Template' + iteration
    create_project(project_name)
    project = get_project_by_name(project_name) # slow, but works
    task = create_template(project_id=project['id'], name=template_name, desc=f'My {iteration} Template')
    poll_task(task)