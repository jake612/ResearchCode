import pickle
import re
import UMLS_Trie as umls_trie


def pickle_file(name, struct):
    try:
        pickle.dump(struct, open(name, "wb"))
    except Exception as e:
        print("Pickle file {} for couldn't save".format(name))
        print(e)


if __name__ == "__main__":
    SUIToString = {}
    SUI_To_CUI = {}
    cui_dict = {}
    StringToSUI = umls_trie.trie()
    with open("MRCONSO.rrf", "r", encoding="utf8") as file:
        for line in file:
            attributes = line.split("|")
            if attributes[1] != "ENG":
                continue
            string = attributes[14].lower()
            StringToSUI.insert_string(string, " ", SUI)

            cui = attributes[0]
            SUI = attributes[5]

            if cui not in cui_dict:
                cui_dict[cui] = set()
            
            cui_dict[cui].add(sui)

            if sui not in SUI_To_CUI:
                SUI_To_CUI[sui] = set()
            SUI_To_CUI[sui].add(sui)

            if SUI not in SUIToString:
                SUIToString[SUI] = string

    pickle_file("StringToSUI.pickle", StringToSUI)
    pickle_file("SUIToString.pickle", SUIToString)
    pickle_file("SUI_To_CUI.pickle", SUI_To_CUI)
    pickle_file("cui_dict.pickle", cui_dict)



