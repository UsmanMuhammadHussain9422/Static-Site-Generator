from textnode import TextNode, TextNodeType

def main():
    # Create a new text node
    text_node = TextNode("This is some anchor text", node_type=TextNodeType.LINK, url="https://www.boot.dev")

    # Print the content of the text node
    print(text_node)

if __name__ == "__main__":
    main()