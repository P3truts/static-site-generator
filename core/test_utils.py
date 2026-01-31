from src.textnode import TextNode, TextType
from core.utils import Utils
import unittest

class TestUtils(unittest.TestCase):

    def test_text_node_to_html_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = Utils.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = Utils.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC_TEXT)
        html_node = Utils.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_code(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = Utils.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, node.text)

    def test_text_node_to_html_link(self):
        node = TextNode("This is a link text node", TextType.LINK)
        html_node = Utils.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.props, {"href": node.url})

    def test_text_node_to_html_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "www.url.com")
        html_node = Utils.text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": node.url, "alt":node.text})

    def test_text_node_to_html_error(self):
        node = TextNode("error", None)

        self.assertRaises(ValueError, lambda: Utils.text_node_to_html_node(node))

    def test_split_nodes_delimiter_wo_md(self):
        node = TextNode("This is a plain text node", TextType.BOLD_TEXT)

        res = Utils.split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        self.assertEqual(1, len(res))
        self.assertEqual(node.text, res[0].text)
        self.assertEqual(node.text_type, res[0].text_type)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is a **bold** text node", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        self.assertEqual(3, len(res))
        self.assertEqual("This is a ", res[0].text)
        self.assertEqual("bold", res[1].text)
        self.assertEqual(" text node", res[2].text)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.BOLD_TEXT, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is a _italic_ text node", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        self.assertEqual(3, len(res))
        self.assertEqual("This is a ", res[0].text)
        self.assertEqual("italic", res[1].text)
        self.assertEqual(" text node", res[2].text)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.ITALIC_TEXT, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is a `code` text node", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

        self.assertEqual(3, len(res))
        self.assertEqual("This is a ", res[0].text)
        self.assertEqual("code", res[1].text)
        self.assertEqual(" text node", res[2].text)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.CODE_TEXT, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_multiple_nodes_delimiter_mixed(self):
        first_node = TextNode("This is a `code` text node", TextType.PLAIN_TEXT)
        second_node = TextNode("This is a plain text node", TextType.ITALIC_TEXT)

        res = Utils.split_nodes_delimiter([first_node, second_node], "`", TextType.CODE_TEXT)

        self.assertEqual(4, len(res))
        self.assertEqual("This is a ", res[0].text)
        self.assertEqual("code", res[1].text)
        self.assertEqual(" text node", res[2].text)
        self.assertEqual(second_node.text, res[3].text)
        self.assertEqual(first_node.text_type, res[0].text_type)
        self.assertEqual(TextType.CODE_TEXT, res[1].text_type)
        self.assertEqual(first_node.text_type, res[2].text_type)
        self.assertEqual(second_node.text_type, res[3].text_type)

    def test_split_nodes_delimiter_error(self):
        self.assertRaises(ValueError, lambda: Utils.split_nodes_delimiter([],
                                                "_", TextType.ITALIC_TEXT))


    def test_split_nodes_delimiter_exception(self):
        node = TextNode("This is a plain text node", TextType.PLAIN_TEXT)

        self.assertRaises(Exception, lambda: Utils.split_nodes_delimiter([node], 
                                                "_", TextType.ITALIC_TEXT))

    def test_extract_markdown_images_single(self):
        text = "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)"

        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]

        res = Utils.extract_markdown_images(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_images_multiple(self):
        text = "This is a text with multiple images: ![image](https://i.imgur.com/zjjcJKZ.png) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        res = Utils.extract_markdown_images(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_images_none(self):
        text = "This is a text with no images"

        expected = []

        res = Utils.extract_markdown_images(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_links_single(self):
        text = "This is a text with a link [to boot.dev](https://www.boot.dev)"

        expected = [("to boot.dev", "https://www.boot.dev")]

        res = Utils.extract_markdown_links(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_links_multiple(self):
        text = "This is a text with a link [to boot.dev](https://www.boot.dev) and [to youtube.com](https://www.youtube.com)"

        expected = [("to boot.dev", "https://www.boot.dev"), ("to youtube.com", "https://www.youtube.com")]

        res = Utils.extract_markdown_links(text)

        self.assertEqual(expected, res)

    def test_extract_markdown_links_none(self):
        text = "This is a text with no links"

        expected = []

        res = Utils.extract_markdown_links(text)

        self.assertEqual(expected, res)

    def test_split_nodes_links_single(self):
        node = TextNode("This is a node with a link [link](www.url.com)", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_links([node])

        self.assertEqual(3, len(res))
        self.assertEqual("This is a node with a link ", res[0].text)
        self.assertEqual("link", res[1].text)
        self.assertEqual("www.url.com", res[1].url)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.LINK, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_links_multiple(self):
        node = TextNode("This is a node with a link [link](www.url.com) and another link [link2](www.url2.com)", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_links([node])

        self.assertEqual(5, len(res))
        self.assertEqual("This is a node with a link ", res[0].text)
        self.assertEqual("link", res[1].text)
        self.assertEqual("www.url.com", res[1].url)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.LINK, res[1].text_type)
        self.assertEqual(" and another link ", res[2].text)
        self.assertEqual("link2", res[3].text)
        self.assertEqual("www.url2.com", res[3].url)
        self.assertEqual(node.text_type, res[2].text_type)
        self.assertEqual(TextType.LINK, res[3].text_type)
        self.assertEqual(node.text_type, res[4].text_type)

    def test_split_nodes_links_error(self):
        self.assertRaises(ValueError, lambda: Utils.split_nodes_links([]))


    def test_split_nodes_links_exception(self):
        node = TextNode("This is a plain text node", TextType.PLAIN_TEXT)

        self.assertRaises(Exception, lambda: Utils.split_nodes_links([node]))

    def test_split_nodes_images_single(self):
        node = TextNode("This is a node with a photo ![img](www.url.com)", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_images([node])

        self.assertEqual(3, len(res))
        self.assertEqual("This is a node with a photo ", res[0].text)
        self.assertEqual("img", res[1].text)
        self.assertEqual("www.url.com", res[1].url)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.IMAGE, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_images_multiple(self):
        node = TextNode("This is a node with a photo ![img](www.url.com) and another photo ![img2](www.url2.com)", TextType.PLAIN_TEXT)

        res = Utils.split_nodes_images([node])

        self.assertEqual(5, len(res))
        self.assertEqual("This is a node with a photo ", res[0].text)
        self.assertEqual("img", res[1].text)
        self.assertEqual("www.url.com", res[1].url)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.IMAGE, res[1].text_type)
        self.assertEqual(" and another photo ", res[2].text)
        self.assertEqual("img2", res[3].text)
        self.assertEqual("www.url2.com", res[3].url)
        self.assertEqual(node.text_type, res[2].text_type)
        self.assertEqual(TextType.IMAGE, res[3].text_type)
        self.assertEqual(node.text_type, res[4].text_type)

    def test_split_nodes_images_error(self):
        self.assertRaises(ValueError, lambda: Utils.split_nodes_images([]))


    def test_split_nodes_images_exception(self):
        node = TextNode("This is a plain text node", TextType.PLAIN_TEXT)

        self.assertRaises(Exception, lambda: Utils.split_nodes_images([node]))



if __name__ == "__main__":
    unittest.main()

