from src.textnode import TextNode, TextType
from core.transform import BlockType, Transform
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

    def test_block_to_block_type_heading(self):
        block = "### this is a heading"

        res = Transform.block_to_blocktype(block)

        self.assertEqual(BlockType.HEADING, res)

    def test_block_to_block_type_code(self):
        block = "```\n this is a code ```"

        res = Transform.block_to_blocktype(block)

        self.assertEqual(BlockType.CODE, res)

    def test_block_to_block_type_quote(self):
        block = "> this is a quote"

        res = Transform.block_to_blocktype(block)

        self.assertEqual(BlockType.QUOTE, res)

    def test_block_to_block_type_uno_list(self):
        block = "- this is a list\n- an unordered one"

        res = Transform.block_to_blocktype(block)

        self.assertEqual(BlockType.UNORDERED_LIST, res)

    def test_block_to_block_type_o_list(self):
        block = "1. this is a list\n2. an ordered one"

        res = Transform.block_to_blocktype(block)

        self.assertEqual(BlockType.ORDERED_LIST, res)

    def test_block_to_block_type_paragraph(self):
        block = "this is a paragraph"

        res = Transform.block_to_blocktype(block)

        self.assertEqual(BlockType.PARAGRAPH, res)

    def test_block_to_block_type_not_heading(self):
        block = "this # is a heading"

        res = Transform.block_to_blocktype(block)

        self.assertNotEqual(BlockType.HEADING, res)

    def test_block_to_block_type_not_code(self):
        block = "``\n this is a code ``"

        res = Transform.block_to_blocktype(block)

        self.assertNotEqual(BlockType.CODE, res)

    def test_block_to_block_type_not_quote(self):
        block = " this> is a quote"

        res = Transform.block_to_blocktype(block)

        self.assertNotEqual(BlockType.QUOTE, res)

    def test_block_to_block_type_not_uno_list(self):
        block = "stuff below: - this is a list\n- an unordered one"

        res = Transform.block_to_blocktype(block)

        self.assertNotEqual(BlockType.UNORDERED_LIST, res)

    def test_block_to_block_type_not_o_list(self):
        block = "stuff below: 1. this is a list\n2. an ordered one"

        res = Transform.block_to_blocktype(block)

        self.assertNotEqual(BlockType.ORDERED_LIST, res)

    def test_markdown_to_html_node_paragraph(self):
        md = """
                This is **bolded** paragraph
                text in a p
                tag here

                This is another paragraph with _italic_ text and `code` here

            """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_markdown_to_html_node_heading(self):
        md = """
                ### This is **bolded** heading
                text in a p
                tag here

                ##### This is another heading with _italic_ text and `code` here

            """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3> This is <b>bolded</b> heading\ntext in a p\ntag here</h3><h5> This is another heading with <i>italic</i> text and <code>code</code> here</h5></div>",
        )

    def test_markdown_to_html_node_quote(self):
        md = """
                > This is **bolded** quote
                text in a p
                tag here

                >This is another quote with _italic_ text and `code` here

            """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote> This is <b>bolded</b> quote\ntext in a p\ntag here</blockquote><blockquote>This is another quote with <i>italic</i> text and <code>code</code> here</blockquote></div>",
        )

    def test_markdown_to_html_node_unordered_list(self):
        md = """
                # This is a heading

                This is an unordered list:

                - This is the first list item in a list block
                - This is a list item
                - This is another list item
             """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1> This is a heading</h1><p>This is an unordered list:</p><ul><li>- This is the first list item in a list block</li>\n<li>- This is a list item</li>\n<li>- This is another list item</li>\n</ul></div>",
        )

    def test_markdown_to_html_node_ordered_list(self):
        md = """
                # This is a heading

                This is an ordered list:

                1. This is the first list item in a list block
                2. This is a list item
                3. This is another list item
             """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1> This is a heading</h1><p>This is an ordered list:</p><ol><li>1. This is the first list item in a list block</li>\n<li>2. This is a list item</li>\n<li>3. This is another list item</li>\n</ol></div>",
        )

    def test_markdown_to_html_node_code(self):
        md = """
                ```
                This is text that _should_ remain
                the **same** even with inline stuff
                ```
            """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_markdown_to_html_node_paragraph_not_eq(self):
        md = "         "

        node = Transform.markdown_to_html_node(md)

        self.assertRaises(ValueError, lambda: node.to_html())

    def test_markdown_to_html_node_heading_not_eq(self):
        md = """
                #This is **bolded** heading
                text in a p
                tag here

                #####This is another heading with _italic_ text and `code` here
            """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertNotEqual(
            html,
            "<div><h3> This is <b>bolded</b> heading\ntext in a p\ntag here</h3><h5> This is another heading with <i>italic</i> text and <code>code</code> here</h5></div>",
        )

    def test_markdown_to_html_node_quote_not_eq(self):
        md = """
                <> This is **bolded** quote
                text in a p
                tag here

                 >This is another quote with _italic_ text and `code` here

            """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertNotEqual(
            html,
            "<div><blockquote> This is <b>bolded</b> quote\ntext in a p\ntag here</blockquote><blockquote>This is another quote with <i>italic</i> text and <code>code</code> here</blockquote></div>",
        )

    def test_markdown_to_html_node_unordered_list_not_eq(self):
        md = """
                # This is a heading

                This is an unordered list:

                 This is the first list item in a list block
                - This is a list item
                -This is another list item
             """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertNotEqual(
            html,
            "<div><h1> This is a heading</h1><p>This is an unordered list:</p><ul><li>- This is the first list item in a list block</li>\n<li>- This is a list item</li>\n<li>- This is another list item</li>\n</ul></div>",
        )
    def test_markdown_to_html_node_ordered_list_not_eq(self):
        md = """
                # This is a heading

                This is an ordered list:

                1 This is the first list item in a list block
                . This is a list item
                 This is another list item
             """

        node = Transform.markdown_to_html_node(md)
        html = node.to_html()
        self.assertNotEqual(
            html,
            "<div><h1> This is a heading</h1><p>This is an ordered list:</p><ol><li>1. This is the first list item in a list block</li>\n<li>2. This is a list item</li>\n<li>3. This is another list item</li>\n</ol></div>",
        )

    def test_markdown_to_html_node_code_raises_Ex(self):
        md = """
                ``
                This is text that _should_ remain
                the **same** even with inline stuff
                `
            """

        self.assertRaises(Exception, lambda: Transform.markdown_to_html_node(md))


if __name__ == "__main__":
    unittest.main()

