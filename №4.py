def Spis(arr):
    b = []
    for i in range(len(arr)):   
	    b.append(arr[(i + 1) % len(arr)] + arr[(i + len(arr) - 1) % len(arr)])
    return b
    
arr = [1, 3, 5, 6, 10]
print(Spis(arr))