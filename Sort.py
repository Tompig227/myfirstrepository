def Sort(datas):
	#有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法
     a=len(datas)
     b=0
     while b<a:
             if '+' in datas[b]:
                     print('+',end=' ')
             b=b+1
     b=0
     while b<a:
             if '-' in datas[b]:
                     print('-',end=' ')
             b=b+1
     print()