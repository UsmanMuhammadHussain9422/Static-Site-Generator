from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] = None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Value cannot be None for LeafNode.")
        if self.tag is None:
            return self.value  # If tag is None, return only the value without any HTML tags.
        
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{self.value}{closing_tag}"

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"