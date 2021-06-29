from data_structures.hashtable.blossom.ll import LinkedList
from data_structures.hashtable.blossom.blossom import Blossom


def test_blossom_proof_of_life():
    blossom = Blossom(0)
    assert blossom.array == []
    

def test_hasattr_method_returns_false_when_given_fake_name():
    life = Blossom(0)
    has_method = hasattr(life, 'fake_one')
    assert has_method == False


def test_hash_method_exists():
    life = Blossom(0)
    has_method = hasattr(life, 'hash')
    assert has_method == True


def test_compressor_method_exists():
    life = Blossom(0)
    has_method = hasattr(life, 'compressor')
    assert has_method == True


def test_assign_method_exists():
    life = Blossom(0)
    has_method = hasattr(life, 'assign')
    assert has_method == True


def test_retrieve_method_exists():
    blossom = Blossom(0)
    has_method = hasattr(blossom, 'retrieve')
    assert has_method == True
