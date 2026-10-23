from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] = None):
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag name cannot be None for ParentNode.")
        if not self.children or len(self.children) == 0:
            raise ValueError("ParentNode must have at least one child.")

        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children)
        return f"{opening_tag}{children_html}{closing_tag}"