__author__ = 'chenwei'
#coding:utf-8       #设置python文件的编码为utf-8，这样就可以写入中文注释
import datetime
def primeRange(n):
    myArray=[1 for x in range(n+1)]  ##列表解析，生成长度为(n+1)的列表，每个数值都为1
    myArray[0]=0
    myArray[1]=0
    startPos=2
    count=0
    while startPos <= n:
        if myArray[startPos]==1:
            key=2
            resultPos = startPos * key  #可知startPos的整数倍都不是素数，设置startPos的整数倍的位置为0表示非素数
            while resultPos <= n:
                myArray[resultPos] =0
                key += 1
                resultPos = startPos *key
                count +=1
        startPos += 1
    print count
    resultList=[]   ##将最终的素数保存在resultList列表返回
    startPos=2
    while startPos <= n:
        if myArray[startPos] == 1:
            resultList.append(startPos)
        startPos += 1
    return resultList

numString=raw_input("Input the Range(>3):")
numInt=int(numString)
starttime = datetime.datetime.now()
if numInt <= 3:
    print "The Number Need to be greater than 3"
else:
    primeResult=primeRange(numInt)
    #print "The Result is:",primeResult
    print len(primeResult)
endtime = datetime.datetime.now()
print (endtime - starttime)
