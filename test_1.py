import unittest

from lab6_1 import Node, search, insert, delete


class TestSearch(unittest.TestCase):
    def test_search_finds_existing_value(self):
        tree = Node(5, Node(3), Node(7))
        self.assertTrue(search(tree, 3))

    def test_search_returns_false_for_missing_value(self):
        tree = Node(5, Node(3), Node(7))
        self.assertFalse(search(tree, 10))

    def test_search_on_empty_tree(self):
        self.assertFalse(search(None, 1))


class TestInsert(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        tree = insert(None, 5)
        self.assertEqual(tree.val, 5)

    def test_insert_new_value_in_correct_position(self):
        tree = Node(5)
        tree = insert(tree, 3)
        tree = insert(tree, 7)

        self.assertEqual(tree.left.val, 3)
        self.assertEqual(tree.right.val, 7)

    def test_insert_duplicate_returns_unchanged_tree(self):
        tree = Node(5)
        new_tree = insert(tree, 5)

        self.assertIs(tree, new_tree)

class TestDelete(unittest.TestCase):
    def test_delete_leaf_node(self):
        tree = Node(5, Node(3), Node(7))
        tree = delete(tree, 3)

        self.assertFalse(search(tree, 3))

    def test_delete_node_with_one_child(self):
        tree = Node(5, Node(3, Node(2)), Node(7))
        tree = delete(tree, 3)

        self.assertTrue(search(tree, 2))
        self.assertFalse(search(tree, 3))

    def test_delete_node_with_two_children(self):
        tree = Node(5, Node(3, Node(2), Node(4)), Node(7))

        tree = delete(tree, 3)
        
        self.assertFalse(search(tree, 3))
        self.assertTrue(search(tree, 2))
        self.assertTrue(search(tree, 4))

if __name__ == "__main__":
    unittest.main() 