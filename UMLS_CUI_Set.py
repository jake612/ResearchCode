import pickle
import numpy as np
import time

# Builds dictionary of cui codes and their associated sui codes
def concept_identifiers(file):
	concept_dict = {}
	with(open(file, "r")) as conso_file:
		for line in conso_file:
			atts = line.split("|")
			cui = atts[0]
			sui = atts[5]
			if cui not in concept_dict:
				concept_dict[cui] = set()
			concept_dict[cui].add(sui)
	return concept_dict

# Loads vectors of processed word2vec vectors into array of tuples for processing
# Each tuple is (word/sui, [vector array])
def load_vectors(file):
	word2index={}
	with(open(file, "r")) as inp_file:
		vector_count, dimensions = [int(i) for i in inp_file.readline().strip().split()]
		matrix = np.zeros((vector_count, dimensions]

		i = 0
		for line in inp_file:
			vals = line.strip().split()
			assert len(vals) == dimensions + 1
			
			word2index[vals[0]] = i	
			matrix[i, :] = [float(j) for j in vals[1:]]
			i+=1
		return word2index, matrix

# Given a matrix, normalize each row based on the L2-norm
def normalize_L2(matrix):
	for i in range(matrix.shape[0]):
		m[i,:] /= np.linalg.norm(m[i,:])



if __name__ == "__main__":
	# Get the cui code dictionary
	start_time = time.time()
	concept_dict = concept_identifiers("MRCONSO.RRF")
	end_time = time.time()
	print("CUI dictionary runtime:{}".format(str((end_time-start_time/60))))	
	
	# Load vectors from word2vec file
	start_time=time.time()
	word2index, matrix = load_vectors("vec.txt")
	end_time = time.time()
	print("Load vectors runtime:{}".format(str((end_time-start_time)/60)))

	# Normalize matrix
	
	start_time=time.time()
	normalize_L2(matrix)
	end_time = time.time()
	print("Normalize matrix runtime:{}".format(str((end_time-start_time)/60)))
	
	index2word = dict([(i, w) for w, i in word2index.items()])
