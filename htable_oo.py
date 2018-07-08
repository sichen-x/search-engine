"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""
class HashTable:
    def __init__(self, size=31):
        """Init a list of nbuckets lists"""
        self.nbuckets = size
        self.the_table = []
        for i in range(self.nbuckets):
            self.the_table.append([])

    def hashcode(self, o):
        """
        Return a hashcode for strings and integers; all others return None
        For integers, just return the integer value.
        For strings, perform operation h = h*31 + ord(c) for all characters in the string
        """
        if isinstance(o, int):
            return o
        elif isinstance(o, str):
            h = 0
            for char in o:
                h = h * 31 + ord(char)
            return h
        else:
            return None

    def buckets_str(self):
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
        if self.the_table == None:
            return None
        output = """"""
        for i in range(len(self.the_table)):
            output += str(i).zfill(4)
            output += '->'
            for node in self.the_table[i]:
                output += str(node[0]) + ':' + str(node[1])
                output += ', '
            output = output.rstrip(', ') # delete the redundant "," in the end
            output += '\n'
        return output


    def __str__(self):
        """
        Return what str(table) would return for a regular Python dict such as {parrt:99}.
        The order should be bucket order and then insertion order in the bucket.
        The insertion order is guaranteed when you append to the buckets in put.
        """

        if self.the_table == None:
            return None

        output = '{'
        for i in range(len(self.the_table)):
            for node in self.the_table[i]:
                output += str(node[0]) + ':' + str(node[1])
                output += ', '
        output = output.rstrip(', ')
        output += '}'
        return output

    def put(self, key, value):
        """
        Perform table[key] = value
        Find the appropriate bucket indicated by key and then append a value to the bucket.
        If the bucket for key already has a key, value pair with that key then replace it.
        Make sure that you are only adding (key, value) associations to the buckets.
        """
        if self.the_table == None or len(self.the_table) == 0:
            return
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
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

    def get(self, key):
        """
        Return the equivalent of table[key].
        Find the appropriate bucket indicated by the key and look for the
        association with the key. Return the value (not the key and not
        the association!). Return None if key not found.
        """
        if self.the_table == None or len(self.the_table) == 0:
            return None
        bucket_index = self.hashcode(key) % len(self.the_table)
        bucket = self.the_table[bucket_index]
        for node in bucket:
            if node[0] == key:
                return node[1]
        return None


    def bucket_indexof(self, key):
        """
        Return the element within a specific bucket; the bucket is table[key].
        You have to search the bucket linearly.
        """
        if self.the_table == None or len(self.the_table) == 0:
            return None
        output = '{'
        for node in self.the_table[key]:
            output += str(node[0]) + ':' + str(node[1])
            output += ', '
        output = output.rstrip(', ')
        output += '}'
        return output

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


# for self testing purpose only
if __name__ == '__main__':
    h = HashTable()
    h['a'] = 34
    print(h['a'])

    table = HashTable(5)
    for i in range(1, 11):
        table.put( i, i)
    print(table.bucket_indexof(0))