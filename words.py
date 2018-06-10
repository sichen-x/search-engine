import os
import re
import string
import glob

def filelist(root):
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(root) for f in filenames]

def get_text(fileName):
    f = open(fileName)
    s = f.read()
    f.close()
    return s

# The implementation by professor Parr. I used it by default
def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words

# The implementation by myself which was implemented before 
# professor Parr provided his code
def words_2(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    word_list = []
    if len(text) < 3:
        return word_list

    # Replace char '|' at first because it conflicts the OR logic operator
    # used for regex. Then escape this char later on.
    regex_pattern_str = re.escape(string.punctuation)
    t = iter(regex_pattern_str)
    # insert OR operator | every other chars in regex_pattern_str
    regex_pattern_str = '|'.join(a+b for a,b in zip(t, t))
    regex_pattern_str += '|[0-9]|\r|\t|\n|]'

    pattern = re.compile(regex_pattern_str)
    text_with_space = re.sub(pattern, ' ', text)
    word_list = text_with_space.split(' ')
    list_len = len(word_list)
    i = 0
    while i < list_len:
        word_list[i] = word_list[i].lower()
        if len(word_list[i]) < 3:
            word_list.pop(i)
            list_len -= 1
        else:
            i += 1
    return word_list



def compile_relevant_content(file, terms):
    line_set = set()
    with open (file, 'r') as myfile:
        for line in myfile:
            words_in_line = words(line)
            for i in range(len(terms)):
                if terms[i] in words_in_line:
                    line_set.add(line)
                    if len(line_set) == 2: return line_set
    return line_set

def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    if terms == None:
        terms_in_str = ' !!!nothing to be found!!! '
    else:
        terms_in_str = ' '.join(terms)

    if docs == None or len(docs) == 0:
        number_of_docs = 0
    else:
        number_of_docs = len(docs)

    html_content = '<html>\n<body>\n'
    html_h2 = '<h2>Search results for <b>' + terms_in_str + '</b> in ' + str(number_of_docs) + ' files</h2>'
    html_content += html_h2
    html_content += '\n\n'

    if number_of_docs:
        section_counter = 0
        for file in docs:
            file_local_url = 'file://' + file
            html_each_section = '<p><a href="' + file_local_url + '">' + file + '</a><br>'
            lines = compile_relevant_content(file, terms)
            html_lines = ''
            for line in lines:
                html_lines += line + '<br>'
            html_each_section += html_lines
            html_each_section += '<br>'
            html_each_section += '\n\n'
            html_content += html_each_section
            section_counter += 1
            if section_counter >= 100: break

    html_content += '</body>\n</html>\n'
    return html_content




def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]


if __name__ == '__main__':
    test_str_a = 'aaaa!bbbb"cccc#dddd$eeee%ffff&gggg\'hhhh(iiii)jjjj*kkkk+llll' \
             ',mmmm-nnnn.oooo/pppp:qqqq;rrrr<ssss=tttt>uuuu?vvvv@wwww' \
             '[xxxx\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print words(test_str_a)
    print words_2(test_str_a)
    test_str_b = """I am a bunny
        who are you!	I am a wolf. wait5seconds!!!! No Way"""
    print words(test_str_b)
    print words_2(test_str_b)
