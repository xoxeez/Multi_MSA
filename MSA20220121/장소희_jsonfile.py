# 파일 열기 및 쓰기 : with -> try ~ exception 변경
import json

try:
    jsonFile = open("Day07\\mydata.json", "rb")
    tempData = json.load(jsonFile)
    reusltData1 = tempData["name"]
    reusltData2 = tempData["age"]
    reusltData3 = tempData["address"]
    reusltData4 = tempData["email"]
    reusltData5 = tempData["empcheck"]
except Exception as error:
    print("1번째 오류 발생. 오류 : " + error)
else:
    jsonFile.close()


jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }


try:
    writeFile = open("Day07\\mydata2.json", "w")
    json.dump(jsonData1, writeFile)
except Exception as error:
    print("2번째 오류 발생. 오류 : " + error)
else:
    writeFile.close()


try:
    writeFile = open("Day07\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False)
except Exception as error:
    print("3번째 오류 발생. 오류 : " + error)
else:
    writeFile.close()


try:
    writeFile = open("Day07\\mydata4.json", "w")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except Exception as error:
    print("4번째 오류 발생. 오류 : " + error)
else:
    writeFile.close()


try:
    writeFile = open("Day07\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except Exception as error:
    print("5번째 오류 발생. 오류 : " + error)
else:
    writeFile.close()


#디버깅 변수 선언함(임시)
temp = 0
