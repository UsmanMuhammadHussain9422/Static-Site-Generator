class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict[str, str] = None):
        self.tag: str = tag
        self.value: str = value
        self.children: list[HTMLNode] = children if children is not None else []
        self.props: dict[str, str] = props if props is not None else {}

    def to_html(self) -> str:
        raise NotImplementedError("Subclasses must implement the to_html method.")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"