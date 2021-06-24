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


def test_add_method_exists():
    life = HashMap(0)
    has_method = hasattr(life, 'add_key_value')
    assert has_method == True


def test_retrieve_method_exists():
    life = HashMap(0)
    has_method = hasattr(life, 'retrieve_keys_value')
    assert has_method == True


def test_add_key_value_():
    hash_map = HashMap(20)
    hash_map.add_key_value("Name", "Benjammin")
    expected = "Benjammin"
    actual = hash_map.retrieve_keys_value("Name")
    assert actual == expected

