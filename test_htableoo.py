from htable_oo import HashTable


def test_empty():
    table = HashTable(5)
    assert str(table) == "{}"
    assert table.buckets_str() == """0000->
0001->
0002->
0003->
0004->
"""


def test_single():
    table = HashTable(5)
    table.put("parrt", 99)
    assert str(table) == "{parrt:99}"
    assert table.buckets_str() == """0000->
0001->
0002->
0003->parrt:99
0004->
"""

def test_a_few():
    table = HashTable(5)
    for i in range(1, 11):
        table.put( i, i)
    s = str(table)
    assert s=="{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    s = table.buckets_str()
    assert s == """0000->5:5, 10:10
0001->1:1, 6:6
0002->2:2, 7:7
0003->3:3, 8:8
0004->4:4, 9:9
"""


def test_str_to_set():
    table = HashTable(5)
    table.put("parrt", {2, 99, 3942})
    table.put("tombu", {6, 3, 1024, 99, 102342})
    assert str(table)== "{tombu:{1024, 99, 3, 102342, 6}, parrt:{2, 99, 3942}}"
    assert table.buckets_str() == """0000->
0001->tombu:{1024, 99, 3, 102342, 6}
0002->
0003->parrt:{2, 99, 3942}
0004->
"""
