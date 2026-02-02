from parentnode import ParentNode
from leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_tagless(self):
        child_node = LeafNode(None, "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>child</div>")

    def test_to_html_with_children_props(self):
        child_node = LeafNode("span", "child")
        props = {"color":"red"}
        parent_node = ParentNode("div", [child_node], props)
        expected = "<div color=\"red\"><span>child</span></div>"

        self.assertEqual(parent_node.to_html(), expected) 

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("p", "grandgrandchild")
        grandchild_node = ParentNode("b", [grandgrandchild_node])
        child_node = ParentNode("h1", [grandchild_node])
        parent_node = ParentNode("h2", [child_node])

        expected = "<h2><h1><b><p>grandgrandchild</p></b></h1></h2>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_multiple_children(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("h", "second child")
        third_child = LeafNode("p", "third child")
        parent_node = ParentNode("div", [first_child, second_child, third_child])

        expected = "<div><span>first child</span><h>second child</h><p>third child</p></div>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_multiple_grandchildren(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("h1", "second child")
        third_child = LeafNode("p", "third child")
        first_parent_node = ParentNode("h2", [first_child])
        second_parent_node = ParentNode("div", [second_child, third_child])
        node = ParentNode("div", [first_parent_node, second_parent_node])

        expected = "<div><h2><span>first child</span></h2><div><h1>second child</h1><p>third child</p></div></div>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_multiple_types_children_grandchildren(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("h", "second child")
        third_child = ParentNode("p", [second_child])
        parent_node = ParentNode("div", [first_child, third_child])

        expected = "<div><span>first child</span><p><h>second child</h></p></div>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_eq_nodes(self):
        child = LeafNode("h1", "child")
        props = {"color":"red"}
        first_node = ParentNode("p", [child], props)
        second_node = ParentNode("p", [child], props)

        self.assertEqual(first_node, second_node)

    def test_not_eq_nodes_tags(self):
        child = LeafNode("h1", "child")
        props = {"color":"red"}
        first_node = ParentNode("p", [child], props)
        second_node = ParentNode("b", [child], props)

        self.assertNotEqual(first_node, second_node)

    def test_not_eq_nodes_child(self):
        child = LeafNode("h1", "child")
        second_child = LeafNode("h1", "second child")
        props = {"color":"red"}
        first_node = ParentNode("p", [child], props)
        second_node = ParentNode("p", [second_child], props)

        self.assertNotEqual(first_node, second_node)

    def test_not_eq_nodes_props(self):
        child = LeafNode("h1", "child")
        props = {"color":"red"}
        second_props = {"color":"blue"}
        first_node = ParentNode("p", [child], props)
        second_node = ParentNode("p", [child], second_props)

        self.assertNotEqual(first_node, second_node)

    def test_to_html_not_eq_with_children(self):
        child_node = LeafNode("error", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_not_eq_with_children_props(self):
        child_node = LeafNode("error", "child")
        props = {"color":"red"}
        parent_node = ParentNode("div", [child_node], props)
        expected = "<div color=\"red\"><span>child</span></div>"

        self.assertNotEqual(parent_node.to_html(), expected) 

    def test_to_html_not_eq_with_grandchildren(self):
        grandchild_node = LeafNode("error", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertNotEqual(parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>")

    def test_to_html_not_eq_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("p", "grandgrandchild")
        grandchild_node = ParentNode("b", [grandgrandchild_node])
        child_node = ParentNode("h1", [grandchild_node])
        parent_node = ParentNode("h2", [child_node])

        expected = "<h2><h1><error><p>grandgrandchild</p></error></h1></h2>"
        self.assertNotEqual(parent_node.to_html(), expected)

    def test_to_html_not_eq_with_multiple_children(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("h", "second child")
        third_child = LeafNode("p", "third child")
        parent_node = ParentNode("div", [first_child, second_child, third_child])

        expected = "<div><span>first child</span><h>error</h><p>third child</p></div>"
        self.assertNotEqual(parent_node.to_html(), expected)

    def test_to_html_not_eq_with_multiple_grandchildren(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("h1", "second child")
        third_child = LeafNode("p", "third child")
        first_parent_node = ParentNode("h2", [first_child])
        second_parent_node = ParentNode("div", [second_child, third_child])
        node = ParentNode("div", [first_parent_node, second_parent_node])

        expected = "<div><h2><span>error</span></h2><div><h1>second child</h1><p>third child</p></div></div>"
        self.assertNotEqual(node.to_html(), expected)

    def test_to_html_not_eq_with_multiple_types_children_grandchildren(self):
        first_child = LeafNode("span", "first child")
        second_child = LeafNode("h", "second child")
        third_child = ParentNode("p", [second_child])
        parent_node = ParentNode("div", [first_child, third_child])

        expected = "<div><error>first child</error><p><h>second child</h></p></div>"
        self.assertNotEqual(parent_node.to_html(), expected)

    def test_to_html_raise_tag_ValueError(self):
        child = LeafNode("p", "child")
        node = ParentNode("", [child])

        self.assertRaises(ValueError, lambda: node.to_html())

    def test_to_html_raise_child_ValueError(self):
        node = ParentNode("p", [])

        self.assertRaises(ValueError, lambda: node.to_html())


if __name__ == "main":
    unittest.main()
