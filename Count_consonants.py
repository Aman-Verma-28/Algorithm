s="AmanIsTheBest Programmer"
def countConsonants(s):
    s=s.lower()
    con_count=0
    vow_count=0
    for i in s:
        if i in "aeiou":
            con_count+=1
        else:
            vow_count+=1
    return (con_count,vow_count)

print(countConsonants(s))
