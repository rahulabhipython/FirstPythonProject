def divi(x,y):
     print(x/y)



def smart_dev(z):
    def c(x,y):
        if x<y:
            x,y=y,x
        return z(x,y)
    return c

divi=smart_dev(divi)

divi(2,4)