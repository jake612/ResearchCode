import pickle
import re
import UMLS_Trie as umls_trie
import json

def pickle_file(name, struct):
    try:
        pickle.dump(struct, open(name, "wb"))
    except Exception as e:
        print("Pickle file {} for couldn't save".format(name))
        print(e)

def parse_comments(comment_file):
    comments = []
    # Formats comment for use in the word2vec algorithm
    with open(comment_file, "r") as file:
        line_num = 0
        for line in file:
            attributes = json.loads(line)
            body = attributes["body"]
            body = body.lower()
            body = re.sub(r"[^a-zA-Z0-9-\s\n]+", "", body)
            body = body.replace("\n", " ")
            words = StringToSUI.replace_string(body, " ")
            final_string = ""
            for word in words:
                final_string += word + " "
            final_string = final_string[:-1] + "\n"
            comments.append(final_string)
            line_num += 1

    with open("parsed_comments.txt", "w") as file:
        for line in comments:
            file.write(line)


if __name__ == "__main__":
    parse_UMLS("MRCONSO.RRF")
    parse_comments("RC_2019-05")





