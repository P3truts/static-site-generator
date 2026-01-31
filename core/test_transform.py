from src.textnode import TextNode, TextType
from core.transform import Transform
import unittest

class TestTransform(unittest.TestCase):


    def test_text_node_to_html_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = Transform.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = Transform.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC_TEXT)
        html_node = Transform.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_code(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = Transform.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_link(self):
        node = TextNode("This is a link text node", TextType.LINK)
        html_node = Transform.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.props, {"href": node.url})

    def test_text_node_to_html_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "www.url.com")
        html_node = Transform.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": node.url, "alt":node.text})

    def test_text_node_to_html_error(self):
        node = TextNode("error", None)

        self.assertRaises(ValueError, lambda: Transform.text_node_to_html_node(node))

    def test_text_to_textnodes_single(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        expected = [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]

        res = Transform.text_to_textnodes(text)

        self.assertEqual(expected, res)

    def test_text_to_textnodes_multiple(self):
        text = "This is a **text** and another **one** with an _italic_ word and another _one_ and a `code block` and another `one` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and another one ![img](www.url.com) and a [link](https://boot.dev) and another one [link2](www.url2.com)"

        expected = [
                TextNode("This is a ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("one", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and another ", TextType.PLAIN_TEXT),
                TextNode("one", TextType.ITALIC_TEXT),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("one", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and another one ", TextType.PLAIN_TEXT),
                TextNode("img", TextType.IMAGE, "www.url.com"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another one ", TextType.PLAIN_TEXT),
                TextNode("link2", TextType.LINK, "www.url2.com"),
            ]

        res = Transform.text_to_textnodes(text)

        self.assertEqual(expected, res)

    def test_text_to_textnodes_mixed(self):
        text = "This is an _italic_ **text** with an _italic_ word and a **bold** `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and another ![img](www.url.com) and some end text."

        expected = [
                TextNode("This is an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("img", TextType.IMAGE, "www.url.com"),
                TextNode(" and some end text.", TextType.PLAIN_TEXT),
            ]

        res = Transform.text_to_textnodes(text)

        self.assertEqual(expected, res)


if __name__ == "__main__":
    unittest.main()

