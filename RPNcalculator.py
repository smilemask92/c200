import math

class stack:
    def __init__(self):
        self.s = []

    def __str__(self):
        return str(self.s)

    def pop(self):
        top = self.s[0]
        self.s = self.s[1:]
        return top

    def push(self,item):
        try:
            item = float(item) #float 로 전환 못시키면 에러
            self.s = [item] + self.s
        except ValueError as err:
            raise err

    def empty(self):
        self.s = []

    def peek(self):
        return self.s[0] if len(self.s) else None
        
class calc:
    def __init__(self):
        self.s = stack()

    def __str__(self):
        return str(self.s)

    def _op1(self,f):
        # f is a function that takes one operand
        # apply f to top item in stack.  
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        if len(self.s.s) <= 0:
            ierror = IndexError("list index out of range")
            raise(ierror)
        n1 = self.s.pop()
        try:
            number = f(n1)
            self.s.push(number)
            return number
        except ValueError as verror:
            self.push(n1)
            raise(verror)

    def _op2(self,f):
        # f is a function that takes two operands
        # apply f to top two items in stack. 
        # top element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        if len(self.s.s) < 2:
            ierror = IndexError("list index out of range")
            raise(ierror)
        else:
            n1 = self.s.pop()
            n2 = self.s.pop()
        try:
            number = f(n1, n2)
            self.s.push(number) #class여서 self 생략
            return number
        except ValueError as err:
            self.push(n2)
            self.push(n1)
            raise err
        except ZeroDivisionError as zeroerr:
            self.push(n2)
            self.push(n1)
            raise zeroerr

    def clear(self):
        # clear the stack 
        self.s.empty()

    def e(self):
        # push math.e on stack
        self.s.push(math.e)

    def ln(self):
        # compute math.log(top of stack) (see math module)
        # use _op1
        return self._op1(lambda x : math.log(x)) 

    def add(self):
        # add top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x,y : y + x)

    def div(self):
        # divide top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x,y : y / x)

    def mult(self):
        # multiply top two elements on stack 
        # use _op2
        # return top element or exception
        return self._op2(lambda x,y : y * x)

    def minus(self):
        # subtract top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x,y : y - x)

    def exp(self):
        # compute x**y with top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x,y : y ** x)
    
    def push(self,data):
        self.s.push(data)

    def work(self,data):
        try:
            if data == 'c': #clear all. Make it as empty list
                self.clear()
                return "Starting new computation"
            elif data == 'e':
                return str(self.e())
            elif data == 'ln':
                return str(self.ln())
            elif data == '+':
                return str(self.add())
            elif data == '-':
                return str(self.minus())
            elif data == '*':
                return str(self.mult())
            elif data == '/':
                return str(self.div())
            elif data == '^':
                return str(self.exp())
            elif data == 'show':
                return str(self)
            else: # if it is not a operend
                str(self.push(data))
        except Exception as err:
            return str(err)
    


if __name__ == "__main__":
    # at the beginning, create calc object,
    # and then calc object will create stack object
    w = calc() 
    i = 0 # trial number
    while True: # while not pressing 'q'
        # uncomment the following to help debugging
        # print(w)
        data = input(f"[{i}]: ").strip()
        if data == 'q':
            print('Terminated')
            break
        else:
            result = w.work(data)
            if result != None:
                print(result)
        i = 0 if data == 'c' else i+1