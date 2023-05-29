from flask import Flask
from kubernetes import client, config
import os

# gitaction build test - 1
app = Flask(__name__)

# Kubernetes API 구성
config.load_incluster_config()
v1 = client.CoreV1Api()

# 루트 경로의 요청을 처리하는 함수
@app.route('/')
def hello_world():
    # 현재 실행 중인 Pod의 이름 가져오기
    pod_name = os.environ['HOSTNAME']
    return pod_name

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

if __name__ == '__main__':
    app.run()

