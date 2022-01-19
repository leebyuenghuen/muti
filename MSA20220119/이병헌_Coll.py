# 1. 딕셔너리로 평균 점수 구하기
DicData1 = {'국어' : 95, '영어' : 90, '수학': 80, '과학':50}
DicData2 = dict.values(DicData1)
SubNum = len(DicData1)
DicAverage = sum(DicData2)/SubNum


# 2. set을 이용해서 1~100까지 숫자 중에 공배수를 구함 : 5 와 3의 공배수의 합집합 구하기
SetData1 = {i for i in range(1,101) if i % 5== 0}
SetData2 = {j for j in range(1,101) if j % 3== 0}

SetData3 = SetData1 | SetData2 # 3과 5의 합집합
SetData4 = SetData1 & SetData2 # 3과 5의 공배수 (교집합)

# 3. list 데이터 : 7,5,3,1,-1,-3,-5,-7 출력 range 를 사용할것
ListData1 = [i for i in range(7,-8,-2)]

# 4. 4번째의 결과를 튜플로 변경(형변환)
TupData1 = tuple(ListData1)


temp = 0