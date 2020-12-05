def criarvetor(num):
    vetor=[1,2,3,5,7]
    for c in range (1,num+1,2):
        for a in range (0,len(vetor)):
                             if c%vetor[a]==0:
                                 vetor=vetor
                             else:
                                 vetor.append(c)
    print(vetor)                            
    return sum( vetor)
print(criarvetor(10))
