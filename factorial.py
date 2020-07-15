def cacaulFactorial(num,axis=0,res=1):
	numlist=[]
	for i in range(1,num+1):
		numlist.append(i)
	res*=numlist[axis]
	if axis==0:
		for example in range(len(numlist)-1):
			axis+=1
			res = cacaulFactorial(num,axis,res)
	return res
res=cacaulFactorial(6)
print(res)