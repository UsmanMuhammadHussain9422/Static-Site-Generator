import unittest
from htmlnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        child1 = LeafNode("p", "Hello, world!")
        child2 = LeafNode("p", "This is a test.")
        parent = ParentNode("div", [child1, child2])
        expected_html = "<div><p>Hello, world!</p><p>This is a test.</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_to_html_with_props(self):
        child1 = LeafNode("span", "Child 1")
        child2 = LeafNode("span", "Child 2")
        parent = ParentNode(tag="section", children=[child1, child2], props={"class": "my-section"})
        expected_html = '<section class="my-section"><span>Child 1</span><span>Child 2</span></section>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_to_html_with_props_2(self):
            child1 = LeafNode("span", "Child 1", props={"style": "color: red;"})
            child2 = LeafNode("span", "Child 2", props={"style": "color: blue;"})
            parent = ParentNode(tag="section", children=[child1, child2], props={"class": "my-section"})
            expected_html = '<section class="my-section"><span style="color: red;">Child 1</span><span style="color: blue;">Child 2</span></section>'
            self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_children(self):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_no_children(self):
        parent = ParentNode(tag="div", children=[])
        with self.assertRaisesRegex(ValueError, "^ParentNode must have at least one child\\.$"):
            parent.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )