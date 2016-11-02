#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
alist = [0]
def isHappy(n):
    a = 0
    for ch in str(n):
        a += int(ch)**2
    #print alist
    #print ( "a:",a)
    b = a
    if a ==1:
        return True
    elif a in alist:
        return False
    else:
        alist.append(a)
        return isHappy(b)