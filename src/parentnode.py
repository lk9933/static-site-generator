from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes need a tag.")
        elif not self.children:
            raise ValueError("All parent nodes need a child.")
        else:
            props = self.props_to_html() if self.props else ""
            child_vals = []
            for child in self.children:
                child_vals.append(child.to_html())
            value = "".join(child_vals)
            return f"<{self.tag}{props}>{value}</{self.tag}>"