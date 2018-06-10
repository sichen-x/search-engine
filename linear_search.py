# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    if files == None or terms == None or len(files) == 0 or len(terms) == 0:
        return None
    ret_docs = []

    for file in files:
        file_content = get_text(file)
        all_terms_not_found = False
        words_in_file = words(file_content)
        for term in terms:
            if term not in words_in_file:
                # if any term is not found in the file
                # set the flag all_terms_not_found dirty
                all_terms_not_found = True
                break
        if all_terms_not_found is False:
            ret_docs.append(file)
    return ret_docs
