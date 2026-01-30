from src.textnode import TextType
from src.leafnode import LeafNode

class Utils:
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
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        raise NotImplemented("to be done")
