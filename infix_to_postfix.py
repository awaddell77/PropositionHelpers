
def prec(operatr):
	if operatr in ('+', '-'): return 1
	if operatr in ('*', '/'): return 2
	return 0

def infix_to_postfix(expr):
	if not expr: return ''
	operatrs = ('*', '/', '+', '-')
	lst = []
	postFixExp = ''
	for i in range(0, len(expr)):
		if expr[i] not in operatrs and expr[i] not in ('(', ')'): postFixExp += expr[i]
		if expr[i] in operatrs:
			while(lst and lst[-1] != '(' and prec(expr[i]) <= prec(lst[-1])):
				postFixExp = postFixExp + str(lst.pop())
			lst.append(expr[i])
		if expr[i] == '(': lst.append(expr[i])
		if expr[i] == ')': 
			while(lst[-1] != '('):
				postFixExp = postFixExp + str(lst.pop())
			lst.pop()
		print(f"Step #{i}: c: {expr[i]}, Stack: {lst}, PostFixExp: {postFixExp}, Remark: ")
	while(lst):
		postFixExp = postFixExp + str(lst.pop())
	return postFixExp
expr = "A*B+C-D/(E+F)"
print(f"Expression: {expr}")
print(infix_to_postfix("A*B+C-D/(E+F)"))