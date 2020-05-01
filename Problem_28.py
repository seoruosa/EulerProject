class Spiral:
    def __init__(self):
        self.side = {-1:0, 0:1}
        self.totalElements = {-1:0, 0:1}
    
    def sideInCircleN(self, n):
        if n not in self.side:
            self.side[n] = self.sideInCircleN(n-1)+2
        return self.side[n]
    
    def totalElementsCircleN(self, n):
        if n not in self.totalElements:
            self.totalElements[n] = self.totalElementsCircleN(n-1) + self.elementsInCircleN(n)
        return self.totalElements[n]

    def elementsInCircleN(self, n):
        return 4*self.sideInCircleN(n) - 4

    def neElementCircleN(self, n):
        return self.totalElementsCircleN(n)
    
    def seElementCircleN(self, n):
        if n not in self.side or n not in self.totalElements:
            a = self.totalElementsCircleN(n)
            a = self.sideInCircleN(n)
        return self.totalElements[n] - self.side[n-1] - 1
        # return -1

    def swElementCircleN(self, n):
        if n not in self.side or n not in self.totalElements:
            a = self.totalElementsCircleN(n)
            a = self.sideInCircleN(n)
        return self.totalElements[n-1] + self.side[n] - 1
    
    def nwElementCircleN(self, n):
        if n not in self.side or n not in self.totalElements:
            a = self.totalElementsCircleN(n)
            a = self.sideInCircleN(n)
        return self.swElementCircleN(n) + self.side[n] - 1
    
    def strSpiral(self, n):
        return f"{self.neElementCircleN(n)} -- {self.seElementCircleN(n)} -- {self.swElementCircleN(n)} -- {self.nwElementCircleN(n)}"


if __name__=='__main__':
    spi = Spiral()
    i = 0
    sumSpiral = 0
    while spi.sideInCircleN(i) <= 1001:
        sumSpiral += spi.neElementCircleN(i) + spi.seElementCircleN(i) + spi.swElementCircleN(i) + spi.nwElementCircleN(i)
        i += 1
    print(sumSpiral)