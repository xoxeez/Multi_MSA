# 1. Dictionary를 이용해서 평균 점수 구하기
dicScore = { "국어": 95, "영어": 90, "수학": 80, "과학": 50 }
scoreSum = dicScore["국어"] + dicScore["영어"] + dicScore["수학"] + dicScore["과학"]
print("1. 평균 점수 : {0}".format(scoreSum / len(dicScore)))
print("-" * 10)

# 2. set을 이용해서 1~100까지 숫자 중에 3과 5의 공배수를 구함
multi3 = {i for i in range(1, 101) if i % 3 == 0}
multi5 = {i for i in range(1, 101) if i % 5 == 0}
print("2. 3과 5의 공배수 : {0}".format(multi3 & multi5))
print("2. 3과 5의 합집합 : {0}".format(multi3 | multi5))
print("-" * 10)

# 3. 리스트 데이터 : 7, 5, 3, 1, -1, -3, -5, -7 출력 (range 활용)
oddList = list(range(7, -8, -2))
print("3. 리스트 출력 : {0}".format(oddList))
print("-" * 10)

# 4. 4번째의 결과를 튜플로 변경 (형변환)
print("4. 튜플로 바꾸기 : {0}".format(tuple(oddList)))
