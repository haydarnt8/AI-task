def prime (raange):
    if raange[0] == 0 or raange[0] == 1j :
       raange = range(2,raange[-1]) 
    r = []
    for n in raange:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0 :
                break
        else :
            r.append(n)
    print (r)
            
            
prime (range(0,1000))