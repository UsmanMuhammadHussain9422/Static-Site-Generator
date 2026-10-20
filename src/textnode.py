from enum import Enum


class TextNodeType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"

class TextNode:
    def __init__(self, text: str, node_type: TextNodeType = TextNodeType.PLAIN, url: str = None):
        self.text: str = text
        self.node_type: TextNodeType = node_type
        self.url: str = url  # Optional URL for links, if applicable

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text, self.node_type, self.url) == (other.text, other.node_type, other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.node_type.value}, {self.url})"