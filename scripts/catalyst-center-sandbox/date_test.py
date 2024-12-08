from datetime import datetime
import json

time = datetime.now()
print(time)

#data = {
#    'date': time.isoformat()
#}

#with open('test.json', 'w') as file:
#    json.dump(fp=file, obj=data, indent=4)

with open('test.json', 'r') as file:
    data = json.load(file)
    print(data)
    earlier = datetime.fromisoformat(data['date'])
    time_diff = time - earlier
    minutes = int(time_diff.total_seconds() /60)
    print(minutes)
