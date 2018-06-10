from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    if len(files) <= 0:
        return None

    index = defaultdict(set)
    for i in range(len(files)):
        file_content = get_text(files[i])
        key_words = words(file_content)
        for word in key_words:
            index[word].add(i)
    return index


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    doc IDs whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    if files == None or index == None or terms == None or \
        len(files) == 0 or len(index) == 0 or len(terms) == 0:
        return None
    ret_file_list = []
    list_of_sets = []
    for term in terms:
        value_set = index.get(term)
        if value_set: # not None
            list_of_sets.append(index[term])
        else:
            return None # at least one term is not found


    if len(list_of_sets) > 0:
        intersection_ids = set.intersection(*list_of_sets)
        for id in intersection_ids:
            ret_file_list.append(files[id])
    else:
        return None
    return ret_file_list
