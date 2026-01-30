from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain"
    ITALIC_TEXT = "italic"
    BOLD_TEXT = "bold"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        txt = self.text == other.text
        typ = self.text_type == other.text_type
        url = self.url == other.url
        return txt and typ and url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type == TextType.PLAIN_TEXT:
            return LeafNode(None, self.text)
        if self.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE_TEXT:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href":self.url})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src":self.url, "alt":self.text})

        raise ValueError(f"TextNode is missing text type!")

