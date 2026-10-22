import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_with_tag_and_value(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        expected_html = "<p>This is a paragraph.</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_with_tag_and_value_and_props(self):
        node = LeafNode(tag="a", value="Click here", props={"href": "https://example.com"})
        expected_html = '<a href="https://example.com">Click here</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_with_none_tag(self):
        node = LeafNode(tag=None, value="Just text")
        expected_html = "Just text"
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_with_none_value_raises_error(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()