from src.textnode import TextNode, TextType
from core.split import Split
import unittest

class TestSplit(unittest.TestCase):

    def test_split_nodes_delimiter_wo_md(self):
        node = TextNode("This is a plain text node", TextType.BOLD_TEXT)

        res = Split.split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        self.assertEqual(1, len(res))
        self.assertEqual(node.text, res[0].text)
        self.assertEqual(node.text_type, res[0].text_type)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is a **bold** text node", TextType.PLAIN_TEXT)

        res = Split.split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        self.assertEqual(3, len(res))
        self.assertEqual("This is a ", res[0].text)
        self.assertEqual("bold", res[1].text)
        self.assertEqual(" text node", res[2].text)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.BOLD_TEXT, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is a _italic_ text node", TextType.PLAIN_TEXT)

        res = Split.split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        self.assertEqual(3, len(res))
        self.assertEqual("This is a ", res[0].text)
        self.assertEqual("italic", res[1].text)
        self.assertEqual(" text node", res[2].text)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.ITALIC_TEXT, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is a `code` text node", TextType.PLAIN_TEXT)

        res = Split.split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

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

        res = Split.split_nodes_delimiter([first_node, second_node], "`", TextType.CODE_TEXT)

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
        self.assertRaises(ValueError, lambda: Split.split_nodes_delimiter([],
                                                "_", TextType.ITALIC_TEXT))


    def test_split_nodes_delimiter_exception(self):
        node = TextNode("This is an error_ text node", TextType.PLAIN_TEXT)

        self.assertRaises(Exception, lambda: Split.split_nodes_delimiter([node], 
                                                "_", TextType.ITALIC_TEXT))

    def test_split_nodes_links_single(self):
        node = TextNode("This is a node with a link [link](www.url.com)", TextType.PLAIN_TEXT)

        res = Split.split_nodes_links([node])

        self.assertEqual(2, len(res))
        self.assertEqual("This is a node with a link ", res[0].text)
        self.assertEqual("link", res[1].text)
        self.assertEqual("www.url.com", res[1].url)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.LINK, res[1].text_type)

    def test_split_nodes_links_multiple(self):
        node = TextNode("This is a node with a link [link](www.url.com) and another link [link2](www.url2.com)", TextType.PLAIN_TEXT)

        res = Split.split_nodes_links([node])

        self.assertEqual(4, len(res))
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

    def test_split_nodes_links_error(self):
        self.assertRaises(ValueError, lambda: Split.split_nodes_links([]))


    def test_split_nodes_links_exception(self):
        node = TextNode("This is an error link](url text node", TextType.PLAIN_TEXT)

        self.assertRaises(Exception, lambda: Split.split_nodes_links([node]))

    def test_split_nodes_images_single(self):
        node = TextNode("This is a node with a photo ![img](www.url.com)", TextType.PLAIN_TEXT)

        res = Split.split_nodes_images([node])

        self.assertEqual(3, len(res))
        self.assertEqual("This is a node with a photo ", res[0].text)
        self.assertEqual("img", res[1].text)
        self.assertEqual("www.url.com", res[1].url)
        self.assertEqual(node.text_type, res[0].text_type)
        self.assertEqual(TextType.IMAGE, res[1].text_type)
        self.assertEqual(node.text_type, res[2].text_type)

    def test_split_nodes_images_multiple(self):
        node = TextNode("This is a node with a photo ![img](www.url.com) and another photo ![img2](www.url2.com)", TextType.PLAIN_TEXT)

        res = Split.split_nodes_images([node])

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
        self.assertRaises(ValueError, lambda: Split.split_nodes_images([]))


    def test_split_nodes_images_exception(self):
        node = TextNode("This is an error ![image text node", TextType.PLAIN_TEXT)

        self.assertRaises(Exception, lambda: Split.split_nodes_images([node]))


if __name__ == "__main__":
    unittest.main()

