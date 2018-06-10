"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    the_table = []
    for i in range(nbuckets):
        the_table.append([])
    return the_table


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if isinstance(o, int):
        return o
    elif isinstance(o, basestring):
        h = 0
        for char in o:
            h = h * 31 + ord(char)
        return h
    else:
        return None


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    pass


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append value
    to that bucket. If the bucket for key already has a (key,value) pair
    with that key then replace it.  Make sure that you are only adding
    (key,value) associations to the buckets.
    """
    if table == None or len(table) == 0:
        return
    bucket_index = hashcode(key) % len(table)
    bucket = table[bucket_index]
    new_item_flag = True
    # Do the linear search in the list of that bucket
    for i in range(len(bucket)):
        if bucket[i][0] == key:
            # update the (key, value) tuplip with merging two sets
            new_value = bucket[i][1] | value
            bucket[i] = (key, new_value)
            new_item_flag = False
            break

    # If the key doesn't exist in the bucket, append the new (key, value)
    # pair to the end of the list.
    if new_item_flag:
        bucket.append((key, value))



def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    if table == None or len(table) == 0:
        return None
    bucket_index = hashcode(key) % len(table)
    bucket = table[bucket_index]
    for node in bucket:
        if node[0] == key:
            return node[1]
    return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    if table == None:
        return None
    output = """"""
    for i in range(len(table)):
        output += str(i).zfill(4)
        output += '->'
        for node in table[i]:
            output += str(node[0]) + ':' + str(node[1])
            output += ', '
        output = output.rstrip(', ') # delete the redundant "," in the end
        output += '\n'
    return output


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    if table == None:
        return None

    output = '{'
    for i in range(len(table)):
        for node in table[i]:
            output += str(node[0]) + ':' + str(node[1])
            output += ', '
    output = output.rstrip(', ')
    output += '}'
    return output