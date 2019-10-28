import json
import re
import pickle

comments = []
# Formats comment for use in the word2vec algorithm
with open("R.txt", "r") as file:
    StringToSUI = pickle.load(open("StringToSUI.pickle", "rb"))
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




