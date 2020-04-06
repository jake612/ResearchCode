import pickle
import numpy as np
import time
import math

# Loads vectors of processed word2vec vectors into array of tuples for processing
# Each tuple is (word/sui, [vector array])
def load_vectors(file):
	word2index={}
	with(open(file, "r", encoding="ISO-8859-1")) as inp_file:
		vector_count, dimensions = [int(i) for i in inp_file.readline().strip().split()]
		matrix = np.zeros((vector_count, dimensions))

		i = 0
		for line in inp_file:
			vals = line.strip().split()
			if len(vals) != dimensions + 1:
				continue
			
			word2index[vals[0]] = i	
			matrix[i, :] = [float(j) for j in vals[1:]]
			i+=1
		return word2index, matrix

# Given a matrix, normalize each row based on the L2-norm
def normalize_L2(matrix):
	for i in range(matrix.shape[0]):
		matrix[i,:] /= np.linalg.norm(matrix[i,:])
	return matrix

# Create a sorted list of the closest vectors based on dot product
def dot_prod(index, matrix, kvals):
	q = matrix[index, :]
	similarity = matrix.dot(q)
	# Initialize a list to hold the returned top-k vals
	topvals = []
	# Using a minimum similarity variable to reduce size of list
	min_sim = 0
	for i in range(similarity.shape[0]):
		if similarity[i] > min_sim or len(topvals) < kvals:
			topvals, min_sim = insert_val(topvals, similarity[i], index, i, kvals)
	return topvals


# Helper function for inserting
def insert_val(list, val, target_index, word_index, kvals):
	if target_index == word_index:
		return list, val
	if len(list) >= kvals:
		list.pop(kvals-1)
	if len(list) == 0:
		list.insert(0, (word_index, val))
		return list, val

	index = binary_insert(list, val, 0, len(list) - 1)
	list.insert(index, (word_index, val))
	return list, list[len(list)-1][1]


def binary_insert(list, val, start, end):
	if start == end:
		if list[start][1] < val:
			return start
		else:
			return start+1

	if start > end:
		return start
	middle_num = math.floor((start+end)/2)
	if val < list[middle_num][1]:
		return binary_insert(list, val, middle_num+1, end)
	elif val > list[middle_num][1]:
		return binary_insert(list, val, start, middle_num-1)
	else:
		return middle_num


if __name__ == "__main__":
	print("STARTED")
	# Get the cui code dictionary
	start_time = time.time()
	#concept_dict, SUI_TO_CUI = concept_identifiers("MRCONSO.RRF")
	end_time = time.time()
	
	# Load vectors from word2vec file
	start_time=time.time()
	word2index, matrix = load_vectors("vec.txt")
	end_time = time.time()
	print("Load vectors runtime:{}".format(str((end_time-start_time)/60)))

	# Normalize matrix
	
	start_time=time.time()
	matrix = normalize_L2(matrix)
	end_time = time.time()
	print("Normalize matrix runtime:{}".format(str((end_time-start_time)/60)))
		
	index2word = dict([(i, w) for w, i in word2index.items()])

	SUI_to_string = pickle.load(open("SUIToString", "rb"))
	
	start_time=time.time()
	num_of_words = 10000
	rankings = []	

	for i in range(num_of_words):
		if index2word[i] in SUI_to_string:
			simwords = dot_prod(i, matrix, 50)
			rankings.append((index2word[i], simwords))
	end_time=time.time()
	print("Generate N:{}".format(str((end_time-start_time)/60)))
	pickle.dump(rankings, open("word-rankings.p", "wb"))
	pickle.dump(index2word, open("index2word.p", "wb"))
