import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        expected_html = ' class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="div")
        expected_html = ''
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        expected_repr = "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_with_children(self):
        child_node = HTMLNode(tag="span", value="Child", children=[], props={})
        parent_node = HTMLNode(tag="div", value="Parent", children=[child_node], props={})
        expected_repr = "HTMLNode(tag=div, value=Parent, children=[HTMLNode(tag=span, value=Child, children=[], props={})], props={})"
        self.assertEqual(repr(parent_node), expected_repr)