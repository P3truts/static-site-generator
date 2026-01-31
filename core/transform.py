from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from core.split import Split

class Transform:
    @staticmethod
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        if text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})

        raise ValueError(f"TextNode is missing text type!")

    @staticmethod
    def text_to_textnodes(text):
        node = TextNode(text, TextType.PLAIN_TEXT)
        bold_nodes = Split.split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        italic_nodes = Split.split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC_TEXT)
        code_nodes = Split.split_nodes_delimiter(italic_nodes, "`", TextType.CODE_TEXT)
        image_nodes = Split.split_nodes_images(code_nodes)
        link_nodes = Split.split_nodes_links(image_nodes)

        return link_nodes


