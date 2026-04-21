def twosums(n,t):
    hashmap={}
    for i in range(len(n)):
        comp=t-n[i]
        if comp in hashmap:
            return [hashmap[comp],i]
        hashmap[n[i]]=i
