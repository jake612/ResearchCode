# Class holds root node and allows interaction with trie structure
class trie:

    def __init__(self):
        self.root_node = trie_node()

    # Returns true if new string added, false if already existed
    # TypeError raised if not string, ValueError raised if string is just ""
    def insert_string(self, string, delimiter, umls_code):
        if not isinstance(string, str):
            print(type(string))
            raise TypeError
        values = string.split(delimiter)
        if len(values) == 0:
            raise ValueError
        return self.root_node.insertValues(values, umls_code)


    def replace_string(self, string, delimiter):
        vals = string.split(delimiter)
        vals = list(filter(lambda a: a != "", vals))
        i = 0
        while i < len(vals):
            replace_code = None
            offset = 0
            node = self.root_node
            while True:
                if i+offset >= len(vals):

                    break
                umls_code = node.getUMLSCode(node, vals[i+offset])
                if umls_code is None:
                    break
                else:
                    if umls_code != "***":
                        replace_code = umls_code
                    node = node.getNode(vals[i+offset])
                    if node is None:
                        break

                offset += 1
            if replace_code is not None:
                vals[i] = replace_code
                while offset > 0:
                    vals.pop(i+offset)
                    offset-=1
            i += 1
        return vals




    def print_vals(self):
        self.root_node.print_vals()


class trie_node:
    def __init__(self):
        # umls_values dictionary holds key (string) and UMLS Code
        self.umls_values = {}

        # dictionary holds key (string) and reference to next possible string value
        self.next_node = {}

    def insertValues(self, values, umls_code):
        if values[0] in self.umls_values:
            if len(values) == 1:
                # if the value is placeholder, replace it with new code
                if self.umls_values[values[0]] is "***":
                    self.umls_values[values[0]] = umls_code
                    return True
                elif values[0] not in self.next_node:
                    return False
            else:
                if values[0] in self.next_node:
                    return self.next_node[values[0]].insertValues(values[1:], umls_code)
                else:
                    return False
        else:
            if len(values) == 1:
                self.umls_values[values[0]] = umls_code
                return True
            else:
                # if there are more values left in the given value list, create a new node
                new_trie_node = trie_node()
                # Set the value to a placeholder "***" to indicate that this is not an ending value
                self.umls_values[values[0]] = "***"
                self.next_node[values[0]] = new_trie_node
                return new_trie_node.insertValues(values[1:], umls_code)

    def getNode(self, value):
        if value in self.umls_values:
            if value in self.next_node:
                return self.next_node[value]
        else:
            return None
    def getUMLSCode(self, node, val):
        if val in node.umls_values:
            return node.umls_values[val]
        else:
            return None


    def print_vals(self):
        for string in self.umls_values.keys():
            print(string + ": " + self.umls_values[string])
            if string in self.next_node and self.next_node[string] is not None:
                self.next_node[string].print_vals()



