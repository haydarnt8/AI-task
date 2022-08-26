import string


def srting (x):
    character = {c:1 for c in x}
    r = {c : False for c in x}
    
    for c in range(0,len(x)-1) :
        for c2 in range(c+1,len(x)-1):
            if x[c] == x[c2]:
                if r[x[c]] == False:
                    character[x[c]] += 1
        r[x[c]] = True
        
    print (max(character, key=character.get))
        
        
srting ("haydar")