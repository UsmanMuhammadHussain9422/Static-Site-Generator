import unittest
from textnode import TextNode, TextNodeType


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

if __name__ == "__main__":
    unittest.main()