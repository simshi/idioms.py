_Words = {
	1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
	10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
	20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
}

def _form_one_section(v):
	h, v = divmod(v, 100)

	fields = [_Words[h] + ' hundred'] if h > 0 else []

	if v in _Words:
		fields.append(_Words[v])
	elif v > 0:
		t, d = divmod(v, 10)
		fields.append(_Words[t*10] + ' ' + _Words[d])

	return ' and '.join(fields)

_Sections = ((1000000000, 'billion'), (1000000, 'million'), (1000, 'thousand'))
def _form_sections(v):
	for radix, name in _Sections:
		n, v = divmod(v, radix)
		if n > 0:
			yield _form_one_section(n) + ' ' + name

	yield _form_one_section(v)

def spell_number(v):
	return ', '.join(filter(bool, _form_sections(v))) if v > 0 else 'zero'
