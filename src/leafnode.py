from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        result = ""
        properties = ""
        if self.props is not None:
            for prop, value in self.props.items():
                properties += f" {prop}=\"{value}\""
        if not self.value:
            raise ValueError("HTMLNode value is missing!")
        if self.tag == None:
            result = self.value
        else:
            result = f"<{self.tag}{properties}>{self.value}</{self.tag}>"

        return result

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

