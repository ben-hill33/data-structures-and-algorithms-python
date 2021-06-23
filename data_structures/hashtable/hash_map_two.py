class HashMap:
    def __init__(self, array_size):
        """
        Data structure using list and keeping track of size with additional integer variable
        """
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        """
        Hashing function takes a key and returns an index into the underlying array.

        Uses .encode() method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.
        """
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

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
        self.array[array_index] = value

    def retrieve_keys_value(self, key):
        """
        Returns the value of a given key.
        """
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]


