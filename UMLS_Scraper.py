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
    SUIAtomics = {}
    StringToSUI = umls_trie.trie()
    with open("UMLS_Subset.txt", "r", encoding="utf8") as file:
        for line in file:
            attributes = line.split("|")
            if attributes[1] != "ENG":
                continue
            string = attributes[14].lower()
            string = re.sub(r"[^a-zA-Z0-9-]+", "", string)
            StringToSUI.insert_string(string, " ", SUI)

            SUI = attributes[5]
            AUI = attributes[7]
            if SUI not in SUIToString:
                SUIToString[SUI] = string
            if SUI not in SUIAtomics:
                SUIAtomics[SUI] = [AUI]
            elif AUI not in SUIAtomics[SUI]:
                SUIAtomics[SUI].append(AUI)

    pickle_file("StringToSUI.pickle", StringToSUI)
    pickle_file("SUIToString.pickle", SUIToString)
    pickle_file("SUIAtomics.pickle", SUIAtomics)




