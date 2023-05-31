from flask import Flask
import os

# gitaction build test - 1
app = Flask(__name__)

# 루트 경로의 요청을 처리하는 함수
@app.route('/')
def hello_world():
    # 현재 실행 중인 Pod의 이름 가져오기
    print_name = "by @namejsjeongkr"
    pod_name = os.environ['HOSTNAME']
    return pod_name + ' ' + print_name

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000",  debug=True)

