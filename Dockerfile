# Base Image로 Python 3.9 사용
FROM python:3.9-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 필요한 Python 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && \
    pip3 install flask

# 소스 코드 복사
COPY . /app/

# 포트 설정
EXPOSE 5000

# 실행할 명령어 설정
CMD ["python", "main.py"]
