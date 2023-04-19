def cpf_validate(cpf):

	try:
		cpf = [int(i) for i in f'{int("".join([i for i in cpf if i.isnumeric()])) :011d}']
	except ValueError:
		cpf = []

	if len(set(cpf)) <= 1 or len(cpf) != 11:
		return False

	sum1 = 0
	mult = range(10, 1, -1)
	for i in range(9):
		sum1 += mult[i] * cpf[i]

	rest1 = sum1 * 10 % 11

	if rest1 == 10:
		rest1 = 0

	sum2 = 0
	mult = [11] + list(mult)

	for i in range(10):
		sum2 += cpf[i] * mult[i]

	rest2 = sum2 * 10 % 11

	if rest2 == 10:
		rest2 = 0

	if rest1 == cpf[9] and rest2 == cpf[10]:
		return True
	else:
		return False


def cpf_format(cpf):
	
	try:
		cpf = int(''.join(i for i in cpf if i.isnumeric()))
	except ValueError:
		cpf = 0

	cpf = f'{cpf:011d}'
	count = 0
	rounds = 0
	new_cpf = ''
	
	for i in cpf:
	
		if len(new_cpf) == 14:
			break
		count += 1
		new_cpf += i
	
		if count == 3:
	
			if rounds < 2:
				rounds += 1
				new_cpf += '.'
			else:
				new_cpf += '-'
			count = 0

	return new_cpf
