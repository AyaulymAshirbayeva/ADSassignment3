def ishap(n):
    seen=set()
    def next(num):
        sum=0
        while num>0:
            digit=num%10
            sum+=digit**2
            num=num//10
        return sum
    while n !=1  and n not in seen:
        seen.add(n)
        n=next(n)
    return n==1

#t.c and s.c are O(logn)
n = 19
print(ishap(n)) 


