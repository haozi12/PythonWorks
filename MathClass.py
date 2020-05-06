class method():

    def __init__(self,a,b,c,d,e):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.e = float(e)

    def add(self):
        return self.a + self.b + self.c + self.d + self.e

    def average(self):
        return (self.a + self.b + self.c + self.d + self.e)*(1/5)
#5 numbers
    def sum(self):
        i = self.a
        S = 0
        while i<= self.a + 99:
            S = S + i
            i = i + 1
        return S
# sum n ---> n+99    (100 numbers)
    def sqrt(self):
        return self.b**(1/2)

    def sq(self):
        return self.c**2
    
    def factorial(self):
        i = 1
        result = 1
        while i<= self.c :
            result = result * i
            i = i + 1
            
        x = result
        return x
