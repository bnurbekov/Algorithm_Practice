def evaluateExpression(exp):
	opndSt = []
	lastOperator = None

	temp = ""

	for c in exp:
		if c!="*" and c!="+":
			temp += c
		else:
			opndSt.append(int(temp))

			if lastOperator is not None:
				if lastOperator == "*":
					opndSt.append(opndSt.pop() * opndSt.pop())
				elif c == "+":
					opndSt.append(opndSt.pop() + opndSt.pop())
				
			lastOperator = c
			temp = ""

	opndSt.append(int(temp))

	if lastOperator is not None and lastOperator == "*":
		opndSt.append(opndSt.pop() * opndSt.pop())

	return sum(opndSt)




if __name__ == "__main__":
	print evaluateExpression("2+4+3*3")