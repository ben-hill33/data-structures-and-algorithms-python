from data_structures.devry.ceis295.week_one_project.ArrayList import ArrayList
from data_structures.devry.ceis295.week_one_project.Quicksort import Quicksort
from data_structures.devry.ceis295.week_one_project.ArrayListActualSpeed import *


def test_array_list_import():
    new_arr = ArrayList()
    expected = True
    actual = new_arr.is_empty()
    assert actual == expected


def test_quick_sort_import():
    new_qs_obj = Quicksort()
    assert new_qs_obj
