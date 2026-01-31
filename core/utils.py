from src.textnode import TextNode, TextType
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
        if not old_nodes:
            raise ValueError("Nodes are missing!")

        res_list = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                res_list.append(node)
            else:
                new_nodes = node.text.split(delimiter, 2)
                if len(new_nodes) < 3 or len(new_nodes) % 2 == 0: 
                    raise Exception("Invalid Markdown syntax!")
                for new_node in new_nodes:
                    if new_nodes.index(new_node) % 2 == 0:
                        res_node = TextNode(new_node, TextType.PLAIN_TEXT)
                    else:
                        res_node = TextNode(new_node, text_type)
                    res_list.append(res_node)

        return res_list
