def util1(x,i,g,n):
	sum = 0
	for z in range(0,n):
		sum += pow(1+g,z)*pow(1+i,n-z)*x

	return sum



def savingsTotal():
	x = input('Enter Savings for first year\n')
	i = input("percent increase in savings \n")
	g = input("percent growth per year\n")
	n  = input('Enter Number of years\n')

	i =float(i)/100
	g = float(g)/100
	print util1(x,i,g,n)	




def timeRequiredtoSave():
	req = input("Enter Required Amount\n")
	x = input('Enter Savings for first year\n')
	i = input("percent increase in savings per year\n")
	g = input("percent growth per year\n")
	i =float(i)/100
	g = float(g)/100
	n = 0
	while util1(x,i,g,n)<req: 
		n += 1
	print n	

def toSavePerMonth():
	x = input('Savings per month for first year: \n')
	r = input('percent increase in savings per year: \n')
	n = input('Number of years:\n')
	r = float(r)/100
	print pow(r+1,n)*x




print '''
		1.Amount to save after n years with x% increase every year with initial savings
		2.Total savings after n years
		3.Time required to save x 
	'''
usrinp = input()
if usrinp == 1:
	toSavePerMonth()
elif usrinp ==2:
	savingsTotal()
elif usrinp ==3:
	timeRequiredtoSave()		







