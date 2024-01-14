from collections import deque
class MyStack:

    def __init__(self):
        self.queu1 = deque()
        self.queu2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queu1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.queu1:
            while len(self.queu1) > 1:
                self.queu2.append(self.queu1.popleft())  
            temp = self.queu1.popleft()
            self.queu1.extend(self.queu2)  
            self.queu2 = deque()
            return temp


    def top(self):
        """
        :rtype: int
        """
        if self.queu1:
            return self.queu1[-1]   

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queu1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()