import json

try: 
    fileName = open("datalab\\mydata.json", mode="rt", encoding="utf-8")
    tempData = json.load(fileName)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
    print("정상")
except:
    print("오류")
else:
    fileName.close()

jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

try:
    writeFile = open("datalab\\mydata2.json", mode = "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)

except:
    print("오류")
finally:
    writeFile.close()


temp = 0
