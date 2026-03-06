class MinStack(object):

    def __init__(self):
        self.st=[]
        self.mini=[]

    def push(self, val):
        self.st.append(val)
        if not self.mini or val<=self.mini[-1]:
            self.mini.append(val)
        

    def pop(self):
        if self.st[-1]==self.mini[-1]:
            self.mini.pop()
        self.st.pop()


    def top(self):
        return self.st[-1]
        

    def getMin(self):
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()