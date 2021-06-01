a = 1
def d(a):  
    b = 0
    c = 0
    d = 0
    e = 0
    d_array = []
    d_set = []
    res = []
    for a in range(0,10000):
        if a<10:
            b = a//1
            d_array.append(a+b)
        elif (a>=10) and (a<100):
            b = a//10
            c = a%10
            d_array.append(a+b+c)
        elif (a>=100) and (a<1000):
            b = a//100
            c = (a%100)//10
            d = a%10
            d_array.append(a+b+c+d)
        elif (a>=1000)and (a<10000):
            b = a//1000
            c = (a%1000)//100
            d = (a%100)//10
            e = a%10
            d_array.append(a+b+c+d+e)
    d_array.sort()

    for i in d_array:
        if i not in d_set:
            d_set.append(i)

    temp = list(range(10000))
    res = list(set(temp)-set(d_set))
    res.sort()

    for j in range(0, len(res)):
        print(res[j])
    return res
d(a)