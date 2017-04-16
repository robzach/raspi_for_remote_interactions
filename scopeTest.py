a = 10

def doubler(num):
    global a
    print ("a = ", a)
    a += 1
    print (num * 2)
    b = 20
    print ("b = ", b)
    b += 1
    return a
