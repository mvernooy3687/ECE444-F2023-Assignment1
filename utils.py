class utils():
    def reversed(self, num):
        s = str(num)[::-1]
        return int(s)
    def formatter(self,num):
        b = bin(int(str(num)))
        h = oct(int(str(num)))
        return (b,h)
