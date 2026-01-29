from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_w_prop(self):
        props = {"href": "www.url.com"}
        node = LeafNode("p", "Hello, world!", props)

        expected = "<p href=\"www.url.com\">Hello, world!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_w_multiple_props(self):
        props = {"href": "www.url.com", "color": "red"}
        node = LeafNode("p", "Hello, world!", props)

        expected = "<p href=\"www.url.com\" color=\"red\">Hello, world!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_eq(self):
        first_node = LeafNode("p", "text")
        second_node = LeafNode("p", "text")

        self.assertEqual(first_node, second_node)

    def test_leaf_not_eq(self):
        first_node = LeafNode("h1", "text")
        second_node = LeafNode("p", "another text")

        self.assertNotEqual(first_node, second_node)

    def test_leaf_no_value(self):
        node = LeafNode("p", None)

        self.assertRaises(ValueError, lambda: node.to_html())

    def test_leaf_to_html_wo_tag(self):
        node = LeafNode(None, "text")

        expected = "text"

        self.assertEqual(expected, node.to_html())


if __name__ == "__main__":
    unittest.main()
