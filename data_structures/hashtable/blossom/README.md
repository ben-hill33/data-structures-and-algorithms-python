# Hash map project

The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library. With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.

In this project, we are going to implement a hash map to relate the names of flowers to their meanings. In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. We will implement the Linked List data structure for each of these separate chains.

## Building out the hash map

1. The underlying data structure for Blossom is going to be a key-value store that uses the common names for flowers as the key and saves the floral meaning of the flower as the value. In order to implement this functionality, we’re going to build out a hash map with separate chains of linked lists at every index.
2. The first thing that we’ll need for our hash map is an array. Python’s lists behave similar to an array, but we’ll need to keep track and enforce the list’s size to make the resemblance stronger.
   - Give `Blossom` a constructor that takes a size parameter. Save size into `self.array_size`.
   - After that, create a list of `None` objects of length size and save it into `self.array`.
3. In order to implement a hash map, we need to implement four different methods.
   - The first two are the internal methods someone interacting with the hash map will use:
     - `hash()`
       - All of `Blossoms` keys are going to be strings, which need to calculate a number for each string.
       - Sum up the the character encodings of each character in the string and use that.
     - `compress()`
   - The next two are external methods someone will use:
     - `set_key_value()`
     - `get_keys_value()`
