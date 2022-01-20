# if문

score = [[95, 90, 80, 50], [100, 50, 90, 90], [99, 60, 100, 40], [55, 80, 80, 60]]
scoreSum = []
scoreAvg = []

i = 0
while i < len(score):
    if i == 0:
        scoreSum.append(sum(score[0]))
        scoreAvg.append(scoreSum[0]/len(score))
    elif i == 1:
        scoreSum.append(sum(score[1]))
        scoreAvg.append(scoreSum[1]/len(score))
    elif i == 2:
        scoreSum.append(sum(score[2]))
        scoreAvg.append(scoreSum[2]/len(score))
    else:
        scoreSum.append(sum(score[3]))
        scoreAvg.append(scoreSum[3]/len(score))
    i += 1

# 출력하기
for i in range(len(score)):
    print("학생{0}의 합계 : {1}, 평균 : {2}".format(i+1, scoreSum[i], scoreAvg[i]))
print("전체학생의 합계 : {0}, 평균 : {1}".format(sum(scoreSum), sum(scoreAvg)/len(score)))
