def cpf_validate(cpf:str) -> bool:
	"""
	Returns True if the CPF is valid and False if it's invalid.
	"""
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


def cpf_format(cpf: str) -> str:
	"""
	Returns the CPF value in the pattern XXX.XXX.XXX-XX
	"""
	try:
		cpf = int(''.join(i for i in cpf if i.isnumeric()))
	except ValueError:
		cpf = 0
	
	cpf = f'{cpf:011d}'

	return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
