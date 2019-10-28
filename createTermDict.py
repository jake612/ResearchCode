import pickle
import json
import sys
import tokenizer
def extractAttrs(fileName, field):
	words = {}
	
	with open(fileName, "r") as fileOpened:
		for line in fileOpened:
			fileJSON = json.loads(line)
			comments = fileJSON.get(field)
			if comments is None:
				continue
			tokens = tokenizer.tokenizeString(comments, lower=True)
			for token in tokens:
				if token not in words:
					words[token] = 0
				else:
					words[token]+=1

	"""j = 0
	for key, value in sorted(words.items(), key = lambda itemCount: itemCount[1], reverse=True):
		if j < 100:
			print("%20s: %6d" % (key, value))
			j+=1
		else:
			break"""
	with open("WordsDict.pickle", "wb") as newFile:
		pickle.dump(words, newFile) 
if __name__ == "__main__":
	wordDict = extractAttrs("../Files/RC_2019-05", "body")
	
