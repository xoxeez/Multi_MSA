from flask import Flask, request, jsonify
import json
import requests

# 변수 선언 - 프로그램의 이름 저장하는 변수(파일 이름 저장 변수)
# application server 개발 app 변수를 많이 사용
app = Flask(__name__) # flask 프로그램 시작 기본 값은 = app.py 파일을 생성

@app.route("/")
def FlaskLab():
    return "Flask 데이터 OK"

# 공공데이터활용지원센터_코로나19 예방접종 위탁의료기관 조회서비스
@app.route("/data")
def FlaskData(): #(startPage, pageCount, address): # 요청 받음
    keyValue = r"ot0oXQeMZ7pF89mIjzPmKFnwFrMVH87sFbvETvoqMm2Y%2FCPRhvO6hmmtI7BxQIDC1lMGt3XD0obgMAkB5fGzFA%3D%3D"   

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond%5BorgZipaddr%3A%3ALIKE%5D=%EA%B0%95%EB%82%A8%EA%B5%AC" #강남구
    dataURL += "&serviceKey=" + keyValue
    
    dataResult = requests.get(dataURL)
    #공공데이터 요청 후 데이터 받기 : flask - request / requests 기능 사용"
    return dataResult.json()
    #return json.loads(dataResult) # 공공데이터 결과 값 응답

if __name__ == "__main__":
    app.run()
