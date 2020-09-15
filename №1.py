#1
def Slov(key,val):
    if len(key)>len(val):
        while len(key)>len(val):
            val.append(None)
        else:
            return {key:value for key,value in zip(key, val)}  
   

key=[1,2,3,4,5]
val=["a","b",'c','d',]
print(Slov(key,val))