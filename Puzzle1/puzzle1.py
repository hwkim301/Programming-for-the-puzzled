caps=['F','F','B','B','B','F','B','B','B','F','F','B','F']

cap2=['F','F','B','B','B','F','B','B','B','F','F','F','F']

def pleaseConform(caps):
    #Initialization
    start=forward=backward=0 
    intervals=[]
    
    #Determine intervals where acps are on in the same direction
    for i in range(1,len(caps)):
        if caps[start]!=caps[i]:
            # each interval is a tuple with 3 elements(start,end,type)
            intervals.append((start,i-1,caps[start]))
            if caps[start]=='F':
                forward+=1 
            else:
                backward+=1
            start=i 
    #Need to add the last interval after for llop completes execution
    intervals.append((start,len(caps)-1,caps[start]))
    if caps[start]=='F':
        forward+=1
    else:
        backward+=1
    if forward<backward:
        flip='F'
    else:
        flip='B'
    for t in intervals:
        if t[2]==flip:
            print('People in positions',t[0],'through',t[1],'flip your caps!')

pleaseConform(caps)

