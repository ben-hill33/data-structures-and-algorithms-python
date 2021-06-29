from data_structures.hashtable.blossom.ll import Node_One, Linked_List_Blossom
from data_structures.hashtable.blossom.bloss_lib import flower_definitions


class Blossom:
    def __init__(self, size):
        self.array_size = size
        self.array = [Linked_List_Blossom() for num in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        payload = Node_One([key, value])
        list_at_array = self.array[array_index]

        for items in list_at_array:
            if key == items[0]:
                items[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        list_at_index = self.array[array_index]

        for items in list_at_index:
            if key == items[0]:
                return items[1]
        return None

blossom = Blossom(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])


print(blossom.retrieve('daisy'))

# print(blossom.retrieve("Lang"))
# print(blossom.retrieve("Sweet"))
# print(blossom.retrieve("Too"))
# print(blossom.retrieve("Probably not"))


