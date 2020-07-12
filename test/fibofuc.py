def createfuc(axis,position):
	m=n=1
	fibolist=[]
	i=position-1
	for example in range(axis):
		fibolist.append(m)
		m,n=n,m+n
	print(fibolist[i])
createfuc(100,10)