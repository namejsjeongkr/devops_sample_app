from flask import Flask
import os
import time

count = 0

while count < 60:
    print("Sleep for Lifecycle of Pod !!")
    time.sleep(1)
    count += 1
    
print("cat /var/run/secrets/test")

app = Flask(__name__)

# root path
@app.route('/')
def hello_world():
    print_name = "by @namejsjeongkr"
    pod_name = os.environ['HOSTNAME']
    
    return pod_name + ' ' + print_name

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000",  debug=True)

