# while문

score = [[95, 90, 80, 50], [100, 50, 90, 90], [99, 60, 100, 40], [55, 80, 80, 60]]
scoreSum = []
scoreAvg = []

i = 0
while i < len(score):
    scoreSum.append(sum(score[i]))
    scoreAvg.append(scoreSum[i]/len(score))
    i += 1

# 출력하기
for i in range(len(score)):
    print("학생{0}의 합계 : {1}, 평균 : {2}".format(i+1, scoreSum[i], scoreAvg[i]))
print("전체학생의 합계 : {0}, 평균 : {1}".format(sum(scoreSum), sum(scoreAvg)/len(score)))
