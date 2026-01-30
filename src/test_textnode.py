import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_wo_url(self):
        first_node = TextNode("This is a text node", TextType.BOLD_TEXT)
        second_node = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertEqual(first_node, second_node)

    def test_eq_w_url(self):
        first_node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.url.com")
        second_node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.url.com")

        self.assertEqual(first_node, second_node)

    def test_not_eq_text(self):
        first_node = TextNode("This is a text node", TextType.BOLD_TEXT)
        second_node = TextNode("This is a another text node", TextType.BOLD_TEXT)

        self.assertNotEqual(first_node, second_node)

    def test_not_eq_type(self):
        first_node = TextNode("This is a text node", TextType.BOLD_TEXT)
        second_node = TextNode("This is a text node", TextType.ITALIC_TEXT)

        self.assertNotEqual(first_node, second_node)

    def test_not_eq_url(self):
        first_node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.url.com")
        second_node = TextNode("This is a text node", TextType.ITALIC_TEXT, "www.aurl.com")

        self.assertNotEqual(first_node, second_node)


if __name__ == "__main__":
    unittest.main()
