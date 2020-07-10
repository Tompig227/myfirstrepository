from math import log
dataSet = [['青绿', '蜷缩', '浊响', '清晰', '凹陷','硬滑','是'],
                ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷','硬滑','是'],
                ['乌黑', '蜷缩', '浊响', '清晰', '凹陷','硬滑','是'],
                ['青绿', '蜷缩', '沉闷', '清晰', '凹陷','硬滑','是'],
                ['浅白', '蜷缩', '浊响', '清晰', '凹陷','硬滑','是'],
                ['青绿', '稍蜷', '浊响', '清晰', '稍凹','软粘','是'],
                ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹','软粘','是'],
                ['乌黑', '稍蜷', '浊响', '清晰', '稍凹','硬滑','是'],
                ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹','硬滑','否'],
                ['青绿', '硬挺', '清脆', '清晰', '平坦','软粘','否'],
                ['浅白', '硬挺', '清脆', '模糊', '平坦','硬滑','否'],
                ['浅白', '蜷缩', '浊响', '模糊', '平坦','软粘','否'],
                ['青绿', '稍蜷', '浊响', '稍糊', '凹陷','硬滑','否'],
                ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷','硬滑','否'],
                ['乌黑', '稍蜷', '浊响', '清晰', '稍凹','软粘','否'],
                ['浅白', '蜷缩', '浊响', '模糊', '平坦','硬滑','否'],
                ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹','硬滑','否'],
                ]
featureName = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '好瓜']
def spilitdataSet():
        '''
        分割数据集
        '''
        pass

def caculshannonEnt(dataSet):
        '''
        计算信息熵（香农熵）
        '''
        numlength=len(dataSet)
        labelCounts={}
        for featVec in dataSet:
                curruntLabel=featVec[-1]
                if curruntLabel not in labelCounts.keys():
                        labelCounts[curruntLabel]=0
                labelCounts[curruntLabel]+=1
        shannonEnt=0.0
        for key in labelCounts:
                prob=float(labelCounts[key])/numlength
                shannonEnt-=prob*log(prob,2)
        return shannonEnt
print(caculshannonEnt(dataSet))

def caculconditionalEnt():
        '''
        计算条件熵H（X/Y）
        '''
        pass

def caculKLIC():
        '''
        计算信息增益
        '''
        pass

def choosebestfeature():
        '''
        选择最好的属性
        '''
        pass

def createTree():
        '''
        创建决策树
        '''
        pass