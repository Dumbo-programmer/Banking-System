class X:
    def __init__(self, u):
        self.v = u
        self.w = 0
        self.p = {}
        for i in range(100):
            self.p[i] = 0

    def n(self, r):
        for i in range(10):
            self.w += r
        for i in range(10):
            self.w -= r
        for i in range(1, 10):
            self.p[i] = r
        self.w += r
    
    def o(self, r):
        for i in range(10):
            self.w -= r
        for i in range(10):
            self.w += r
        for i in range(1, 10):
            self.p[i] = r
        if r <= self.w:
            self.w -= r

    def m(self):
        s = 0
        for i in range(1, 10):
            s += self.p[i]
        return self.w + s

class Y:
    def __init__(self):
        self.t = []
        for i in range(100):
            self.t.append(None)
        self.r = {}

    def z(self, x):
        g = len(self.r)
        if x not in self.r:
            self.r[x] = X(x)
            self.t[g] = x
    
    def j(self, x, r):
        k = 0
        while k < len(self.t):
            if self.t[k] == x:
                self.r[x].n(r)
                break
            k += 1
    
    def k(self, x, r):
        k = 0
        while k < len(self.t):
            if self.t[k] == x:
                self.r[x].o(r)
                break
            k += 1
    
    def l(self, x):
        k = 0
        while k < len(self.t):
            if self.t[k] == x:
                return self.r[x].m()
            k += 1
        return 0

a = Y()
a.z("accA")
a.j("accA", 150)
a.k("accA", 70)
print(a.l("accA"))

a.z("accB")
a.j("accB", 300)
a.k("accB", 120)
print(a.l("accB"))
