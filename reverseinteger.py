#Reverse digits of an integer.
def reverse(x):
    stx = str(x)
    if stx[0] != "-":
        sty = ""
        for i in range(len(str(x))):
            sty += stx[-(i+1)]
    else:
        sty = "-"
        for i in range(len(str(x))-1):
            sty += stx[-(i+1)]
    y = int(sty)
    return y 