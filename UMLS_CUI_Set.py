import pickle

# Builds dictionary of cui codes and their associated sui codes
def concept_identifiers(file):
	concept_dict = {}
	with(open(file, "r")) as conso_file:
		for line in conso_file:
			atts = line.split("|")
			cui = atts[0]
			sui = atts[5]
			if cui not in concept_dict:
				concept_dict[cui] = []
			concept_dict[cui].append(sui)
	return concept_dict

# Loads vectors of processed word2vec vectors into array of tuples for processing
# Each tuple is (word/sui, [vector array])
def load_vectors(file):
	vectors = []
	with(open(file, "r")) as inp_file:
		for line in inp_file:
			vals = line.split(" ")
			word = vals[0]

			int_vecs = []
			i = 1
			# Type conversion of string to int
			while i < len(vals):
				int_vecs.append(int(vals[i]))	
			vectors.append(word, int_vecs)

	return vectors

if __name__ == "__main__":
	# Get the cui code dictionary
	concept_dict = concept_identifiers("MRCONSO.RRF")
	
	# Load vectors from word2vec file
	vectors = load_vectors("vec.txt")
