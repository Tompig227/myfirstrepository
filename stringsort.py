def mysort(data):
    #有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。高阶方式
     frontindex=0
     endindex=0
     length=len(data)
     while frontindex+endindex<length:
             if data[frontindex]=='-':
                     frontindex += 1
             else:
                     data[frontindex],data[length-endindex-1]=data[length-endindex-1],data[frontindex]
                     endindex+=1
             return data