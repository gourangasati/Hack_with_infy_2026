class MinStack:

    def __init__(self):
        self.main_s = []
        self.min_s = []
    def push(self, val: int) -> None:
        self.main_s.append(val)
        if not self.min_s or val <= self.min_s[-1]:
            self.min_s.append(val)
    def pop(self) -> None:
        if self.main_s and self.min_s[-1] == self.main_s[-1]:
            self.main_s.pop()
            self.min_s.pop()
        elif self.main_s:
            self.main_s.pop()
    def top(self) -> int:
        if self.main_s:
            return self.main_s[-1]
        return None
    def getMin(self) -> int:
        if self.min_s:
            return self.min_s[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()