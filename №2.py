#2
def Numbers(string): 
    lenght = len(string)
    numbers = [] 
    i = 0 
    while i < lenght: 
        Str = '' 
        Sim = string[i] 
        while '0' <= Sim <= '9':
            Str += Sim
            i += 1
            if i < lenght: 
                Sim = string[i]
            else:
                break
        i += 1
        if Str != '': 
            numbers.append(int(Str)) 
    return numbers 

print (Numbers('ssdv23kjb4j23h1254v4j23v4'))