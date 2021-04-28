# Python program to convert infix expression to postfix

# Class to convert the expression
class Conversion:
	
	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		# This array is used a stack
		self.array = []
		# Precedence setting
		self.output = []
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
	
	# check if the stack is empty
	def isEmpty(self):
		return True if self.top == -1 else False
    
	# Return the value of the top of the stack
	def peek(self):
		return self.array[-1]
	
	# Pop the element from the stack
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
    
	# Push the element to the stack
	def push(self, op):
		self.top += 1
		self.array.append(op)

	# A utility function to check is the given character
	# is operand
	def isOperand(self, ch):
		return ch.isalpha()

	# Check if the precedence of operator is strictly
	# less than top of stack or not
	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False
			
	# The main function that
	# converts given infix expression
	# to postfix expression
	def infixToPostfix(self, exp):
		
		# Iterate over the expression for conversion
		for i in exp:
			# If the character is an operand,
			# add it to output
			if self.isOperand(i):
				self.output.append(i)
			
			# If the character is an '(', push it to stack
			elif i == '(':
				self.push(i)

			# If the scanned character is an ')', pop and
			# output from the stack until and '(' is found
			elif i == ')':
				while( (not self.isEmpty()) and
								self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			# An operator is encountered
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		# pop all the operator from the stack
		while not self.isEmpty():
			self.output.append(self.pop())

		return self.output
      
class infix_to_prefix:
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
    def __init__(self):
        self.items=[]
        self.size=-1
    def push(self,value):
        self.items.append(value)
        self.size+=1
    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def isempty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def seek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.size]
    def is0perand(self,i):
        if i.isalpha() or i in '1234567890':
            return True
        else:
            return False
    def reverse(self,expr):
        rev=""
        for i in expr:
            if i is '(':
                i=')'
            elif i is ')':
                i='('
            rev=i+rev
        return rev
    def infixtoprefix (self,expr):
        prefix=""
        for i in expr:
            if(len(expr)%2==0):
                print("Incorrect infix expr")
                return False
            elif(self.is0perand(i)):
                prefix +=i
            elif(i in '+-*/^'):
                while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]):
                    prefix+=self.pop()
                self.push(i)
            elif i is '(':
                self.push(i)
            elif i is ')':
                o=self.pop()
                while o!='(':
                    prefix +=o
                    o=self.pop()

        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                prefix+=self.pop()
        return prefix
            
# Python program for expression tree

# An expression tree node
class Et:

	# Constructor to create a node
	def __init__(self , value):
		self.value = value
		self.left = None
		self.right = None

# A utility function to check if 'c'
# is an operator
def isOperator(c):
	if (c == '+' or c == '-' or c == '*'
		or c == '/' or c == '^'):
		return True
	else:
		return False

# A utility function to do inorder traversal
def inorder(t):
	if t is not None:
		inorder(t.left)
		print(t.value),
		inorder(t.right)

# Returns root of constructed tree for
# given postfix expression
def constructTree(postfix):
	stack = []

	# Traverse through every character of input expression
	for char in postfix :

		# if operand, simply push into stack
		if not isOperator(char):
			t = Et(char)
			stack.append(t)

		# Operator
		else:

			# Pop two top nodes
			t = Et(char)
			t1 = stack.pop()
			t2 = stack.pop()
			
			# make them children
			t.right = t1
			t.left = t2
			
			# Add this subexpression to stack
			stack.append(t)

	# Only element will be the root of expression tree
	t = stack.pop()
	
	return t

def evaluateExpressionTree(root):
  
    # empty tree
    if root is None:
        return 0
  
    # leaf node
    if root.left is None and root.right is None:
        return int(root.value)
  
    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
  
    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
  
    # check which operation to apply
    if root.value == '+':
        return left_sum + right_sum
      
    elif root.value == '-':
        return left_sum - right_sum
      
    elif root.value == '*':
        return left_sum * right_sum
    elif root.value == '^':
        tmp = left_sum
        for i in range(0,right_sum):
            tmp = tmp * left_sum
            
        return tmp
    else:
        return left_sum / right_sum
    
    

print("\n--------------  Welcome To Algebric Expression  ---------------\n")
print("_________________________________________________________________")
choice = 'yes'  
while(choice == 'yes'):
    exp = input('Enter the expression   ->  ')
    obj = Conversion(len(exp))
    postfix2 = obj.infixToPostfix(exp)

    s=infix_to_prefix()
    rev=""
    rev=s.reverse(exp)
    result=s.infixtoprefix(rev)
    if (result!=False):
        prefix=s.reverse(result)
        print("\nthe prefix expr of is   :  ")
        print(prefix)

        postfix = ""
        for i in postfix2:
            postfix = postfix + i
    
        print("\nthe postfix expr of is  :  ")
        print(postfix)   
        li = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']

        choice = 'yes'
        while(choice == 'yes'):
            thisdict = {}

            for j in postfix2:
                if(j in li):
                    if(j not in thisdict):
                        temp = input("Enter value for "+j+"       : ") 
                        thisdict[j] =  temp
                        postfix = postfix.replace(j,temp)
           
            r = constructTree(postfix)
            result = evaluateExpressionTree(r)
            print("\nThe Evaluation of Algebric Expression.")
            print(result)
        
            print("\nYou Want to Change Variable Values : ")
            choice = input()
            postfix = ""
            for i in postfix2:
                postfix = postfix + i
            
        print("\nYou Want to Continue or Quit (yes/no) : ")
        choice = input()

