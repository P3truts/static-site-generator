from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode tag is missing!")
        if not self.children:
            raise ValueError("ParentNode children are missing!")

        parent_props = ""
        if self.props:
            for prop, val in self.props.items():
                parent_props += f" {prop}=\"{val}\""

        result = f"<{self.tag}{parent_props}>"
        if self.children:
            for child in self.children:
                if not child.children:
                    props_res = ""
                    if child.props:
                        for prop, val in child.props.items():
                            props_res += f" {prop}=\"{val}\""
                    child_res = f"<{child.tag}{props_res}>{child.value}</{child.tag}>"
                    result += child_res
                else:
                    result += child.to_html()

        result += f"</{self.tag}>"
        return result

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        t = self.tag == other.tag
        c = self.children == other.children
        p = self.props == other.props
        return t and c and p

