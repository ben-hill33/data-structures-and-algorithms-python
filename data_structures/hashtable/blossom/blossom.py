from data_structures.hashtable.blossom.ll import LinkedList
from data_structures.linked_list.node import Node

class Blossom:
    def __init__(self, size):
        self.array_size = size
        self.array = [None for item in range(size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        self.array[array_index] = [key, value]

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        payload = self.array[array_index]

        if payload[0] is None or payload[0] != key:
            return None
        if payload[0] == key:
            return payload[1]

# blossom = Blossom(10)
# blossom.assign("Name", "ben")
# blossom.assign("Lang", "ben")
# blossom.assign("Sweet", "ben")
# blossom.assign("Too", "ben")
# blossom.assign("Probably not", "ben")

# print(blossom.retrieve("Name"))
# print(blossom.retrieve("Lang"))
# print(blossom.retrieve("Sweet"))
# print(blossom.retrieve("Too"))
# print(blossom.retrieve("Probably not"))


