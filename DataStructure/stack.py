# Stack in Python

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        return str(self.items)
    def numberOfElements(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items)==0
    def showMeTheTop(self):
        if not self.isEmpty():
            return self.items[-1]

s=Stack()
s.push("AMAN")
s.push("XYZ")
s.push("ABC")
print(s)
s.pop()
print(s)
print(s.showMeTheTop())

