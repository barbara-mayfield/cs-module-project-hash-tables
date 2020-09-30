class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.

        The load factor is the number of keys stored in the hash table divided by the capacity.
        The size should be chosen so that the load factor is less than 1.
        """
        return self.size / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211
        FNV_offset_basis = 14695981039346656037

        hashed = FNV_offset_basis

        string = key.encode()

        for char in string:
            hashed = hashed * FNV_prime
            hashed = hashed ^ char
        return hashed

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key:
            hash = (hash * 33) + ord(i)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # find the index for the key in the table
        # looks for a node with key in the array/LL
        # if there is none, add a node with the key and value to the array/LL
        idx = self.hash_index(key)
        node = HashTableEntry(key, value)
        table = self.table[idx]
        self.size += 1

        if table:
            self.table[idx] = node
            self.table[idx].next = table
        else:
            self.table[idx] = node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.put(key, None)
        self.size -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Looks for a node with key in the arr/LL
        # Returns the value in that node, if there is no
        # such node, return None.

        idx = self.hash_index(key)
        table = self.table[idx]

        while table:
            if table.key == key:
                return table.value
            table = table.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        old_capacity = self.capacity

        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for idx in range(old_capacity):
            old = old_table[idx]

            while old != None:
                self.put(old.key, old.value)
                old = old.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
