def fiunch(s):
    count={}
    for i in range(len(s)):
        ch=s[i]
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    for i in range(len(s)):
        if count[s[i]]==1:
            return i
    return -1

s="leetcode"
print(fiunch(s))

