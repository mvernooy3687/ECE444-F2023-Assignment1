class utils():
    def reversed(self, num):
        s = str(int(num))[::-1]
        return int(s)
    def formatter(self,num):
        b = bin(int(str(int(num))))
        h = oct(int(str(int(num))))
        return (b,h)
