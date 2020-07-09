from math import log
dataSet = [['青年', '否', '否', '一般', '拒绝'],
                ['青年', '否', '否', '好', '拒绝'],
                ['青年', '是', '否', '好', '同意'],
                ['青年', '是', '是', '一般', '同意'],
                ['青年', '否', '否', '一般', '拒绝'],
                ['中年', '否', '否', '一般', '拒绝'],
                ['中年', '否', '否', '好', '拒绝'],
                ['中年', '是', '是', '好', '同意'],
                ['中年', '否', '是', '非常好', '同意'],
                ['中年', '否', '是', '非常好', '同意'],
                ['老年', '否', '是', '非常好', '同意'],
                ['老年', '否', '是', '好', '同意'],
                ['老年', '是', '否', '好', '同意'],
                ['老年', '是', '否', '非常好', '同意'],
                ['老年', '否', '否', '一般', '拒绝'],
                ]
featureName = ['年龄', '有工作', '有房子', '信贷情况']
numlength=len(dataSet)
labelCounts={}
for featVec in dataSet:
        curruntLabel = featVec[-1]
        if curruntLabel not in labelCounts.keys():
                labelCounts[curruntLabel]=0
        labelCounts[curruntLabel]+=1
shannonEnt=0.0
for key in labelCounts:
        prob=float(labelCounts[key])/numlength
        shannonEnt-=prob*log(prob,2)
print(shannonEnt)
print (labelCounts)
classList = [example[-1] for example in dataSet] # 类别列表
print(classList)