from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/meraki-webhook', methods=['POST'])
def meraki_alert():
    data: dict = request.get_json()

    print("RECEIVED MERAKI ALERT!!!")
    print(data) # logs full JSON payload

        # Optional: parse specific fields
    alert_type = data.get('alertType')
    device_name = data.get('deviceName')
    time = data.get('occurredAt')

    print(f"[{time}] {alert_type} on {device_name}")

    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)


