

class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for _ in range(self.size)]


    def __setitem__(self, key, value):
        hsh = self.hash_function(key)
        found = False

        for idx, element in enumerate(self.arr[hsh]):
            if len(element) == 2 and element[0] == key:
                self.arr[hsh][idx] = (key, value)
                found = True
                break
            if not found:
                self.arr[hsh].append((key, value))



    def __getitem__(self, key):
        hsh = self.hash_function(key)
        return self.arr[hsh]


    def __delitem__(self, key):
        hsh = self.hash_function(key)
        self.arr[hsh] = None


    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size



if __name__ == '__main__':
    ht = HashTable(size=10)
    ht['names=='] = 'pranay'
    ht['name'] = 'sranay'
    print(ht.arr)
    del ht['name']
    print(ht.arr)