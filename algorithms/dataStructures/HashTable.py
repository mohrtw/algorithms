"""
HashTable implements a hashtable without using python dictionaries.
hashtables support fast lookups.
"""
from collections import namedtuple

Entry = namedtuple('Entry', 'key value')

class HashTable(object):
    """
    HashTable implenets a hash table for fast lookups.

    size : integer number of buckets
    entries : integer number of entries
    _load_factor : float entries/size
    _buckets : list of lists containing Entries
    """

    def __init__(self, size=100):
        self._load_factor = 0
        self._size = size
        self._entries = 0
        self._buckets = [[] for _ in range(size)]

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size 
        self.load_factor = self.entries/size

    @property
    def entries(self):
        return self._entries

    @entries.setter
    def entries(self, entries):
        self._entries = entries
        self.load_factor = entries/self.size

    @property
    def load_factor(self):
        return self._load_factor

    @load_factor.setter
    def load_factor(self, load_factor):
        self._load_factor = load_factor
        if load_factor >= .5:
            _increase_buckets()

    def __getitem__(self, item):
        h = hash(item)
        b = self._buckets[h % self.size]
        if not b:
            raise KeyError(item + " is not in HashTable")

        for e in b:
            if e.key == item:
                return e.value

        raise KeyError(item + " is not in HashTable")


    def __setitem__(self, key, value):
        h = hash(key)
        self._buckets[h % self.size].append(Entry(key, value))
        self.entries += 1

    def __delitem__(self, item):
        h = hash(item)
        b = self._buckets[h % self.size]
        if not b:
            raise KeyError(item + " is not in HashTable")

        for e in b:
            if e.key == item:
                b.remove(e)
                self.entries -= 1
                return

        raise KeyError(item + " is not in HashTable")

    def _increase_buckets(self):
        self._buckets.extend([[]] * self.size)
        self.size *= 2

# TODO : implement __delitem__
