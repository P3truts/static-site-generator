import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_eq_wo_children_props(self):
        first_node = HTMLNode("h1", "This is a header!")
        second_node = HTMLNode("h1", "This is a header!")
        self.assertEqual(first_node, second_node)

    def test_eq_w_children_props(self):
        first_node_child = HTMLNode("h1", "Child 1")
        second_node_child = HTMLNode("h1", "Child 1")

        first_node_props = {"href": "https://url.com"}
        second_node_props = {"href": "https://url.com"}

        first_node = HTMLNode("h1", "HTMLNode", [first_node_child], first_node_props)
        second_node = HTMLNode("h1", "HTMLNode", [second_node_child], second_node_props)
        self.assertEqual(first_node, second_node)

    def test_eq_props_to_html(self):
        node_props = {"href": "www.url.com"}
        child = HTMLNode()
        node = HTMLNode("h1", "TestNode", [child], node_props) 

        expected_props = " href=www.url.com"
        result_props = node.props_to_html()
        self.assertEqual(expected_props, result_props)

    def test_not_eq_htmlnode(self):
        first_node = HTMLNode("h1", "This is a header")
        second_node = HTMLNode("h2", "This is another header", props={"href": "link"})
        self.assertNotEqual(first_node, second_node)

    def test_not_eq_url(self):
        node = HTMLNode("h2", props={"href": "www.aurl.com"})
        expected_props = "bad result" 
        result_props = node.props_to_html()

        self.assertNotEqual(expected_props, result_props)

if __name__ == "__main__":
    unittest.main()

