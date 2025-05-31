from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(value=value, tag=tag, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        elif not self.tag:
            return self.value
        else:
            props = self.props_to_html() if self.props else ""
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"