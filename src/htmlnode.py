

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        text = ""
        if self.props is None or not self.props:
            return text

        for k, v in self.props.items():
            text += f" {k}=\"{v}\""

        return text

    def __eq__(self, other):
        t = self.tag == other.tag
        v = self.value == other.value
        c = self.children == other.children
        p = self.props == other.props
        return t and v and c and p

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, val={self.value}, kids={self.children}, props={self.props})"
