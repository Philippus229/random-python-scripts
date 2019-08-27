class cmplx:
    def add(cn0, cn1):
        return [cn0[0]+cn1[0], cn0[1]+cn1[1]]
    
    def substract(cn0, cn1):
        return [cn0[0]-cn1[0], cn0[1]-cn1[1]]

    def multiply(cn0, cn1):
        return [cn0[0]*cn1[1]+cn0[1]*cn1[0], cn0[1]*cn1[1]-cn0[0]*cn1[0]]

    def divide(cn0, cn1):
        return [cmplx.multiply(cn0, [-cn1[0],cn1[1]])[0]/cmplx.multiply(cn1, [-cn1[0],cn1[1]])[1], cmplx.multiply(cn0, [-cn1[0],cn1[1]])[1]/cmplx.multiply(cn1, [-cn1[0],cn1[1]])[1]]

    def isprime(n):
        return "idk"
        
class generic:
    def isprime(n):
        if n > 1:
            d = 2
            while d <= n/d:
                if n/d == int(n/d):
                    return False
                d += 1
            return True
        else:
            return False

    def primelist(minnum, maxnum):
        pl = []
        while minnum <= maxnum:
            if minnum > 1:
                d = 2
                ip = True
                while d <= minnum/d:
                    if minnum/d == int(minnum/d):
                        d = minnum/d
                        ip = False
                    d += 1
                if ip:
                    pl.append(minnum)
            minnum += 1
        return pl
