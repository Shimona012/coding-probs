class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        sum_b=str(bin(a+b))
        return sum_b[2:]
        