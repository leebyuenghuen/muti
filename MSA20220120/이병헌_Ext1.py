# 1. 4개의 과목을 합계 + 평균( 개인 평균 / 4명의 합)
DicData1 = {'국어' : 95, '영어' : 95, '수학': 95, '과학':50}
DicData2 = {'국어' : 100, '영어' : 50, '수학' : 90, '과학' : 90}
DicData3 = {'국어' : 99, '영어' : 60, '수학' : 100, '과학' : 40}
DicData4 = {'국어' : 55, '영어' : 80, '수학' : 80, '과학' : 60}

DicVal1 = dict.values(DicData1)
total = 0
for i in DicVal1:
    total = total + i
SumVal1 = total  # 홍길동1 의 합계
DicAve1 = SumVal1/len(DicData1) # 홍길동1 의 평균

DicVal2 = dict.values(DicData2)
total = 0
for i in DicVal2:
    total = total + i
SumVal2 = total  # 홍길동2 의 합계
DicAve2 = SumVal2/len(DicData2)  # 홍길동2 의 평균

DicVal3 = dict.values(DicData3)
total = 0
for i in DicVal3:
    total = total + i
SumVal3 = total  # 홍길동3 의 합계
DicAve3 = SumVal3/len(DicData3)  # 홍길동3 의 평균

DicVal4 = dict.values(DicData4)
total = 0
for i in DicVal4:
    total = total + i
SumVal4 = total  # 홍길동4 의 합계
DicAve4 = SumVal4/len(DicData4)  # 홍길동4 의 평균

SumTot = SumVal1 + SumVal2 + SumVal3 + SumVal4 # 각 합계의 총합 : 4명의 합계
SumAve = DicAve1 + DicAve2 + DicAve3 + DicAve4 # 각 평균의 총 합
AveTot = SumAve/4 # 4명의 평균

temp = 0
