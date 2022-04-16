caps=['F','F','B','B','B','F','B','B','B','F','F','B','F']

cap2=['F','F','B','B','B','F','B','B','B','F','F','F','F']
def pleaseConformOnepass(caps):
    caps=caps+[caps[0]]
    for i in range(1,len(caps)):
        if caps[i]!=caps[i-1]:
                if caps[i]!=caps[0]:
                    print('People in positions',i,end=' ')
                else:
                    print(' through ',i-1,'flip your caps')

pleaseConformOnepass(caps)