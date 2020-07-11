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
def spilitdataSet(dataSet,i,value):
        '''
        分割数据集
        '''
        retdataSet=[]
        for featVec in dataSet:
                if featVec[i]==value:
                        reduceFeatvec=featVec[:i]
                        reduceFeatvec.extend(featVec[i+1:])
                        retdataSet.append(reduceFeatvec)
        return retdataSet

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

def caculconditionalEnt(dataSet,i,featList,uniqueVals):
        '''
        计算条件熵H（X/Y）
        '''
        ctEnt=0.0
        for value in uniqueVals:
                dubDataset=spilitdataSet(dataSet,i,value)
                prob=len(dubDataset)/float(len(dataSet))
                ctEnt+=prob*caculshannonEnt(dubDataset)
        return ctEnt

def caculKLIC(dataSet,baseEntropy,i):
        '''
        计算信息增益
        '''
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEnt=caculconditionalEnt(dataSet,i,featList,uniqueVals)
        infoEnt=baseEntropy-newEnt
        return infoEnt


def choosebestfeature(dataSet):
        '''
        选择最好的属性
        '''
        numfeatures = len(dataSet[0])-1
        baseEntropy=caculshannonEnt(dataSet)
        bestinfoEnt=0.0
        bestfeature=-1
        for i in range(numfeatures):
                infoEnt=caculKLIC(dataSet,baseEntropy,i)
                if(infoEnt>bestinfoEnt):
                        bestinfoEnt=infoEnt
                        bestfeature=i
        return bestfeature


def createTree(dataSet,featureName):
        '''
        创建决策树
        '''
        classList=[example[-1] for example in dataSet]# 类别列表
        if classList.count(classList[0]) == len(classList):# 统计属于列别classList[0]的个数
                return classList[0]# 当类别完全相同则停止继续划分
        if len(dataSet[0]) == 1:# 当只有一个特征的时候，遍历所有实例返回出现次数最多的类别
                return majorityCnt(classList)# 返回类别标签
        bestfeat=choosebestfeature(dataSet)#最佳特征对应的索引
        bestfeatLabel=featureName[bestfeat]#最佳特征
        tree={bestfeatLabel:{}}# map 结构，且key为featureLabel
        del(featureName[bestfeat])
        # 找到需要分类的特征子集
        featValue=(example[bestfeat] for example in dataSet)
        uniqueValue=set(featValue)#set函数删除重复
        for value in uniqueValue:
                subLabel=featureName[:]# 复制操作
                tree[bestfeatLabel][value]=createTree(spilitdataSet(dataSet,bestfeat,value),subLabel)
        return tree

# 测试决策树的构建
tree=createTree(dataSet,featureName)
print(tree)