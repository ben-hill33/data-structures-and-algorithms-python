class HashMap:
    def __init__(self, array_size):
        """
        Data structure using list and keeping track of size with additional integer variable
        """
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        """
        Hashing function takes a key and returns an index into the underlying array.

        Uses .encode() method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.
        """
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        """
        Transforms hashed values into useful indices.
        """
        return hash_code % self.array_size

    def add_key_value(self, key, value):
        """
        Assigns HashMap's array indices to compressor() and hash() methods.
        """
        array_index = self.compressor(self.hash(key))
        current_val = self.array[array_index]

        if current_val is None:
            self.array[array_index] = [key, value]
            return
        if current_val[0] == key:
            self.array[array_index] = [key, value]
            return

        number_collisions = 1

        while current_val[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_val = self.array[new_array_index]

            if current_val is None:
                self.array[array_index] = [key, value]
                return
            if current_val[0] == key:
                self.array[array_index] = [key, value]
                return
            number_collisions += 1
        return

    def retrieve_keys_value(self, key):
        """
        Returns the value of a given key.
        """
        array_index = self.compressor(self.hash(key))
        possible_value = self.array[array_index]

        if possible_value is None:
            return None

        if possible_value[0] == key:
            return possible_value[1]
        
        retrieval_collisions = 1
        
        while possible_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieve_index = self.compressor(new_hash_code)
            possible_value = self.array[retrieve_index]

            if possible_value is None:
                return None
            if possible_value[0] == key:
                return possible_value[1]
            
            retrieval_collisions += 1
        return

hash_map = HashMap(20)
hash_map.add_key_value("Name", "Ben")
hash_map.add_key_value("Name", "Claire")
hash_map.add_key_value("Ninja Turles", "Leondardo")
hash_map.add_key_value("Teacher", "Roger")


