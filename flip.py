# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:30:44 2022

@author: NOPE
"""
import copy
import random

def compare( a,b ):
    f = [a,b,a]
    k=a-b
    while((k!=1 and k!=-1)and k!=0):
        k=k//2
    return f[k]

def flip(arr):
    size=len(arr)
    restore=0
    result=0
    for i in range(arr):
        restore+=i
    result=compare(restore,size-restore)
    return result

def flip01(arr):
    idx=0
    wheredf=[]
    wheresm=[]
    where=[]
    for i in range(arr):
        if(idx!=idx+i):
            wheresm.append(copy.deepcopy(where))
            where.clear()
            where.append(idx)
        elif(idx==idx+i):
            wheredf.append(copy.deepcopy(where))
            where.clear()
            where.append(idx)
        idx+=1
    
    return 0

def flip02(arr):
    idx=0
    dfsize=0
    smsize=0
    wheredf=[]
    wheresm=[]
    where_d=[]
    where_s=[]
    for i in arr:
        if(idx!=idx+i):
            wheresm.append(copy.deepcopy(where_s))
            smsize+=1
            where_s.clear()
            where_d.append(idx)
        elif(idx==idx+i):
            wheredf.append(copy.deepcopy(where_d))
            dfsize+=1
            where_d.clear()
            where_s.append(idx)
        idx+=1
    print(wheredf)
    print(wheresm)
    return compare(smsize,dfsize)

def flip03(arr):
    restore=arr[0]
    newarr=[arr[0]]
    count=0
    for i in arr:
        if(restore!=i):
            restore=i
            newarr.append(restore)
    
    for j in newarr:
        count+=j
    print(newarr)
    return compare(count,len(newarr)-count)

def flip04(arr):
    restore=arr[0]
    newarr=copy.deepcopy(arr)
    count=0
    for i in arr:
        if(restore==newarr[count]):
            newarr.remove(newarr[count])
            count-=1
        else:
            restore=i
        print(i,newarr,count)
        count+=1
    count=0
    for j in newarr:
        count+=j
    print(newarr)
    return compare(count,len(newarr)-count)

def flip04A(arr):
    restore=arr[0]
    newarr=copy.deepcopy(arr)
    ip=1
    # print(newarr[1:])
    for i in arr:
        if(i==newarr[ip]):
            newarr.remove(newarr[ip])
        else:
            restore=i
            ip+=1
        print(i,newarr,ip)
        
    count=0
    for j in newarr:
        count+=j
    print(newarr)
    return compare(count,len(newarr)-count)

def flip04A01(arr):
    restore=arr[0]
    newarr=copy.deepcopy(arr)
    idx=1
    # print(newarr[1:])
    for i in arr[1:]:
        if(restore==newarr[idx]):
            newarr.pop(idx)
        else:
            restore=newarr[idx]
            idx+=1
        # print(restore,newarr,idx)
        
    count=0
    for j in newarr:
        count+=j
    # print(newarr)
    print(count, len(newarr))
    return compare(count,len(newarr)-count)

def flip05(arr):
    mat=[[0,0],[0,1],[1,0],[1,1]]
    restore=[]
    pattern=[]
    value=0
    variousU=0
    variousD=0
    idx=0
    size=len(arr)
    for j in arr:
        value += j
    
    for i in range(1,size):
        idx=0
        restore.clear()
        restore.append(arr[i-1])
        restore.append(arr[i])
        while(restore != mat[idx]):
            idx += 1
        if(idx == 1):
            pattern.append('u')
        elif(idx == 2):
            pattern.append('d')
    
    for k in pattern:
        if(k == 'u'):
            variousU += 1
        else:
            variousD += 1
    
    if(value >= size-value):
        return variousU
    else:
        return variousD

def flip05A(arr):
    mat=[[0,0],[0,1],[1,0],[1,1]]
    restore=[]
    pattern=[]
    value=0
    variousU=0
    variousD=0
    idx=0
    size=len(arr)
    for j in arr:
        value += j
    
    for i in range(1,size):
        idx=0
        restore.clear()
        restore.append(arr[i-1])
        restore.append(arr[i])
        while(restore != mat[idx]):
            idx += 1
        if(idx == 1):
            pattern.append('u')
        elif(idx == 2):
            pattern.append('d')
    
    for k in pattern:
        if(k == 'u'):
            variousU += 1
        else:
            variousD += 1
    
    if(value >= size-value):
        if(variousU == 0):
            return variousD
        return variousU
    else:
        if(variousD == 0):
            return variousU
        return variousD

def flip05A01(arr):
    mat=[[0,0],[0,1],[1,0],[1,1]]
    restore=[]
    pattern=[]
    value=0
    variousU=0
    variousD=0
    idx=0
    size=len(arr)
    for j in arr:
        value += j
    
    for i in range(1,size):
        idx=0
        restore.clear()
        restore.append(arr[i-1])
        restore.append(arr[i])
        while(restore != mat[idx]):
            idx += 1
        if(idx == 1):
            pattern.append('u')
        elif(idx == 2):
            pattern.append('d')
    
    for k in pattern:
        if(k == 'u'):
            variousU += 1
        else:
            variousD += 1
    
    if(value >= size-value):
        if(variousU == 0):
            return variousD
        if(arr[0]==1):
            variousU += 1
        return variousU
    else:
        if(variousD == 0):
            return variousU
        return variousD

def flip05A02(arr):
    mat=[[0,0],[0,1],[1,0],[1,1]]
    restore=[]
    pattern=[]
    value=0
    variousU=0
    variousD=0
    idx=0
    size=len(arr)
    for j in arr:
        value += j
    
    for i in range(1,size):
        idx=0
        restore.clear()
        restore.append(arr[i-1])
        restore.append(arr[i])
        while(restore != mat[idx]):
            idx += 1
        if(idx == 1):
            pattern.append('u')
        if(idx == 2):
            pattern.append('d')
    
    for k in pattern:
        if(k == 'u'):
            variousU += 1
        elif(k == 'd'):
            variousD += 1
    
    if(arr[0] == 1):
        return variousD
    elif(arr[0] == 0):
        return variousU
        
def flip05A03(arr):
    mat=[[0,0],[0,1],[1,0],[1,1]]
    restore=[]
    pattern=[]
    inpat=[0,1,2,3]
    value=0
    various=[0,0,0,0]
    idx=0
    size=len(arr)
    for j in arr:
        value += j
    
    for i in range(1,size):
        idx=0
        restore.clear()
        restore.append(arr[i-1])
        restore.append(arr[i])
        while(restore != mat[idx]):
            idx += 1
        pattern.append(inpat[idx])

    for k in pattern:
        various[k] += 1
    
    return various[1+arr[0]]

def fliptest():
    # print(flip04A01([0,0,1,1,1,0,0,0,0,1,1,1,1,1,0]))
    arr=[0,0,0,1,1,0,0]
    print(flip04A01(arr))

def fliptest01():
    arr=[]
    instr=input()
    idx=len(instr)
    for i in range(idx):
        arr.append(ord(instr[i])-48)
    
    print(flip04A01(arr))

def fliptest02():
    
    instr=input()
    N=len(instr)
    arr=[0]*(N)
    for k in range(N):
        arr[k]=ord(instr[k])&1
    
    print(flip04A01(arr))

def fliptest03():
    intable=[1,0,0,1,1,0,1,0,1,1,1,0]
    output=0
    output=flip05A03(intable)
    print(output)
    

def main():
    fliptest03()

if(__name__=="__main__"):
    main()