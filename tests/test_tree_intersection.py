from challenges.tree_intersection.tree_intersection import Node, tree_intersection


# def test_bt_one_root():
#     bt_one = Node(150)
#     bt_one.left = Node(100)
#     bt_one.right = Node(250)
#     bt_one.left.left = Node(75)
#     bt_one.left.right = Node(160)
#     bt_one.right.left = Node(200)
#     bt_one.right.right = Node(350)
#     bt_one.left.right.left = Node(125)
#     bt_one.left.right.right = Node(175)
#     bt_one.right.right.left = Node(300)
#     bt_one.right.right.right = Node(500)

#     bt_two = Node(42)
#     bt_two.left = Node(100)
#     bt_two.right = Node(600)
#     bt_two.left.left = Node(15)
#     bt_two.left.right = Node(160)
#     bt_two.right.left = Node(200)
#     bt_two.right.right = Node(350)
#     bt_two.left.right.left = Node(125)
#     bt_two.left.right.right = Node(175)
#     bt_two.right.right.left = Node(4)
#     bt_two.right.right.right = Node(500)

#     actual = tree_intersection(bt_two, bt_two)
#     expected = [100, 160, 125, 175, 200, 350, 500]
#     assert actual == expected
