def connection_finder(array):
    array1=[]
    array2=[]
    for x in array:
        value= compare(x,array)
        array2.append(value)
        array1.append(array2)
    return array1

def compare(x,array):
    array1=[]
    array2=[]
    for y in array:
        a=0
        for x1 in x[0]:
            count=y[1].count(x1)
            if x[0]==y[1]:
                array2.append(['non'])
            elif count==1:
                array2.append([a,x1,x[0]])
                a=a+1
        array1.append(array2)
    return array1

def array_find(array):
    array_loops=[]
    for num in len(array):
        new_puzzle.append(findloops(array[num],array))
    return array_loops

def findloops(array1,array2):
    a=array1
    while len(a)>0:
        for x in a:
            b=rest(a)
            for y in b:
                
        
        
        
            
            
    
        