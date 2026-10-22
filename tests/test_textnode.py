import unittest
from src.textnode import TextNode, TextNodeType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a link", TextNodeType.LINK, url="https://example.com")
        node2 = TextNode("This is a link", TextNodeType.LINK, url="https://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_with_different_url(self):
        node = TextNode("This is a link", TextNodeType.LINK, url="https://example.com")
        node2 = TextNode("This is a link", TextNodeType.LINK, url="https://different.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_with_url_and_other_type(self):
        node = TextNode("This is a link", TextNodeType.LINK, url="https://example.com")
        node2 = TextNode("This is a text node", TextNodeType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a different text node", TextNodeType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        self.assertNotEqual(node, "This is a string")

    def test_text(self):
        node = TextNode("This is a text node", TextNodeType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextNodeType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextNodeType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextNodeType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_image(self):
        node = TextNode("This is an image", TextNodeType.IMAGE, url="https://example.com/image.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "This is an image"})