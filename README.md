# CPF-validator
Este é um script simples para validação e formatação de CPF.
This is a simple script to validate and format CPF (Brazilian ID number).


# Exemplo de uso (Usage example):

<pre>
<code>
from cpf_validator import *

cpf = input('Type a CPF: ')

formatted_cpf = cpf_format(cpf)

if cpf_validate(formatted_cpf):
    print(f'CPF {formatted_cpf} is valid.')

else:
    print(f'CPF {formatted_cpf} is NOT valid.')
</code>
</pre>
