from data_structures.hashtable.hash_map_two import HashMap


def test_proof_of_life():
    life = HashMap(0)
    assert life.array == []


def test_hash_method_life():
    life = HashMap(0)
    assert life.hash
