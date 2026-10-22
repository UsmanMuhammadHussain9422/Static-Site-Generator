from enum import Enum
from src.leafnode import LeafNode

class TextNodeType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"

class TextNode:
    def __init__(self, text: str, node_type: TextNodeType = TextNodeType.TEXT, url: str = None):
        self.text: str = text
        self.node_type: TextNodeType = node_type
        self.url: str = url  # Optional URL for links, if applicable

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text, self.node_type, self.url) == (other.text, other.node_type, other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.node_type.value}, {self.url})"

    def text_node_to_html_node(self) -> LeafNode:
        if self.node_type == TextNodeType.TEXT:
            return LeafNode(tag=None, value=self.text)
        elif self.node_type == TextNodeType.BOLD:
            return LeafNode(tag="b", value=self.text)
        elif self.node_type == TextNodeType.ITALIC:
            return LeafNode(tag="i", value=self.text)
        elif self.node_type == TextNodeType.CODE:
            return LeafNode(tag="code", value=self.text)
        elif self.node_type == TextNodeType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": self.url, "alt": self.text})
        elif self.node_type == TextNodeType.LINK:
            return LeafNode(tag="a", value=self.text, props={"href": self.url})
        else:
            raise ValueError(f"Unsupported TextNodeType: {self.node_type}")