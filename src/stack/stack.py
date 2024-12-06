class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return f'{self.stack}'

    def __repr__(self):
        return f'{self.stack}'

    def push (self, num : int):
        self.stack.append(num)
        return num
    
    def pop (self):
        num = self.stack[-1]
        self.stack=self.stack[0:-1]
        return num
    
stack = Stack()
for i in range(2):
    for j in range(4):
        if i==0:
            stack.push(j)
            
        else:
            if j!=0 and j!=3:
                stack.pop()
            
            if j==3:
                print(f'FILO {0}-{stack.pop()}')

            if j==0:
                print(f'LIFO {3}-{stack.pop()}')