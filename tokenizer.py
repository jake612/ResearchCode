

# Method takes in a string and returns a list of tokens
def tokenizeString(string, **kwargs):
	tokens = []
	delimiter = ' '
	if string is None:
		return []
	try:
		if kwargs['lower'] is True:
			string.lower()
		tokens = string.split()
		for token in tokens:
			token = token.strip(".,?!:;")
	except Exception as e:
		print(str(e))
	return tokens

		
