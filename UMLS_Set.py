import pickle

# Builds dictionary of cui codes and their associated sui codes
def concept_identifiers(file):
    concept_dict = {}
    SUI_TO_CUI = {}
    with(open(file, "r")) as conso_file:
        for line in conso_file:
            atts = line.split("|")
            cui = atts[0]
            sui = atts[5]
            if atts[1] != "ENG":
                continue
            SUI_TO_CUI[sui] = cui
            if cui not in concept_dict:
                concept_dict[cui] = set()
            if sui not in concept_dict[cui]:
                concept_dict[cui].add(sui)
    return concept_dict, SUI_TO_CUI

def pickle_save(object, filename):
    pickle.dump(object, open(filename, "wb"))

def pickle_load(filename):
    return pickle.load(open(filename, "rb"))

def calc_prec_and_recall(array, target_term, index2word, cui_sets, sui_to_cui):
    target_set = cui_sets[sui_to_cui[target_term]]
    if len(target_set) <= 1:
        return 0, 1
    retrieved_in_set = 0
    for term_set in array:
        term = index2word[term_set[0]]
        if term in target_set:
            retrieved_in_set+=1

    precision = retrieved_in_set/len(array)
    # target set - 1 because one of the terms is the one you retrieved
    recall = retrieved_in_set / (len(target_set) - 1)
    return precision, recall

if __name__ == "__main__":
    sui_prec_recall = []
    seen_cuis = set()
    index2word = pickle_load("index2word.p")
    SUIToString = pickle_load("SUIToString")
    concept_dict, SUI_TO_CUI = concept_identifiers("MRCONSO.RRF")
    for topk_list in pickle_load("word-rankings.p"):
        term = topk_list[0]
        # term not an identifier
        if term not in SUI_TO_CUI:
            continue
        elif SUI_TO_CUI[term] in seen_cuis:
            continue
        precision, recall = calc_prec_and_recall(topk_list[1], term, index2word, concept_dict, SUI_TO_CUI)
        sui_prec_recall.append((SUIToString[term], precision, recall))
        seen_cuis.add(SUI_TO_CUI[term])

    sui_prec_recall.sort(key=lambda x: x[1], reverse=True)
    print("term    precision    recall")
    for i in sui_prec_recall: print(i)





