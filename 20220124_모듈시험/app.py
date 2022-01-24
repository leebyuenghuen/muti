

from flask import Flask
import json
import requests


app = Flask(__name__) # flask 프로그램 시작 기본 값은 = app.py 파일을 생성


@app.route("/") 
def FlaskLab(): 
    return "Flask 데이터 응답" 

@app.route("/data1")
def FlaskData(): # startPage, pageCount, address 요청 받음

    tempURL = r"https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10&cond%5BorgZipaddr%3A%3ALIKE%5D=%EA%B0%95%EB%82%A8%EA%B5%AC&serviceKey=Q1biU84zh82ZGdfFtkbaK%2F7nyC%2BDXk8KFMeV8YIzztRHn7xTUIcrOB8DPmbZM60WEiUzD%2BQG8muLN5eJfTYjNg%3D%3D"

    dataResult = requests.get(tempURL)
   
    return json.loads(dataResult) 
 


