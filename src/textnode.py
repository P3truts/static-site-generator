from enum import Enum

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

