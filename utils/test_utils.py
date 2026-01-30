from textnode import TextNode, TextType
import unittest

class TestUtils(unittest.TestCase):

    def test_text_node_to_html_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_code(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_link(self):
        node = TextNode("This is a link text node", TextType.LINK)
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.props, {"href": node.url})

    def test_text_node_to_html_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "www.url.com")
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": node.url, "alt":node.text})

    def test_test_node_to_html_error(self):
        node = TextNode("error", None)

        self.assertRaises(ValueError, lambda: node.text_node_to_html_node())


if __name__ == "__main__":
    unittest.main()

