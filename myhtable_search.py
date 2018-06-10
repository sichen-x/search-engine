# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    if len(files) <=0:
        return None

    table = htable(4011)
    for i in range(len(files)):
        file_content = get_text(files[i])
        key_words = words(file_content)
        for word in key_words:
            # because the value is a set, whenever a value
            # is added to hash table here, if the key is
            # is already in the hash table, the new value
            # is going to merged to the existing value.
            htable_put(table, word, set([i]))
    return table


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    if files == None or index == None or terms == None or \
        len(files) == 0 or len(index) == 0 or len(terms) == 0:
        return None
    ret_file_list = []
    list_of_sets = []
    for term in terms:
        value = htable_get(index, term)
        if value:
            list_of_sets.append(value)
        else:
            return None # at least one term is not found

    if len(list_of_sets) > 0:
        intersection_ids = set.intersection(*list_of_sets)
        for id in intersection_ids:
            ret_file_list.append(files[id])
    else:
        return None
    return ret_file_list




