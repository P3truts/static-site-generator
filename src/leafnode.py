from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        result = ""
        properties = ""
        if self.props is not None:
            properties = self.props_to_html()
        if not self.value and self.tag != "img":
            raise ValueError("HTMLNode value is missing!")
        if self.tag is None:
            result = self.value
        else:
            result = f"<{self.tag}{properties}>{self.value}</{self.tag}>"

        return result

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

