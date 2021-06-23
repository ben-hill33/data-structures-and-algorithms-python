from data_structures.hashtable.hash_map_two import HashMap


def test_proof_of_life():
    life = HashMap(0)
    assert life.array == []


def test_hasattr_method_returns_false_when_given_fake_name():
    life = HashMap(0)
    has_method = hasattr(life, 'fake_one')
    assert has_method == False


def test_hash_method_exists():
    life = HashMap(0)
    has_method = hasattr(life, 'hash')
    assert has_method == True


def test_compressor_method_exists():
    life = HashMap(0)
    has_method = hasattr(life, 'compressor')
    assert has_method == True


def test_assign_method_exists():
    life = HashMap(0)
    has_method = hasattr(life, 'assign')
    assert has_method == True


def test_retrieve_method_exists():
    life = HashMap(0)
    has_method = hasattr(life, 'retrieve')
    assert has_method == True
