class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        let_den={chr(i): i - 64 for i in range(65, 91)}
        col = 0
        for i in columnTitle:
            col=col*26+let_den[i]
        return col