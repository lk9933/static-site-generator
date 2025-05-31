import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_props(self):
        """Test ParentNode with properties."""
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )
        
    def test_to_html_with_multiple_children(self):
        """Test ParentNode with multiple children."""
        child1 = LeafNode("First", "span")
        child2 = LeafNode("Second", "span")
        child3 = LeafNode("Third", "span")
        parent_node = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>First</span><span>Second</span><span>Third</span></div>"
        )
        
    def test_error_no_tag(self):
        """Test error when ParentNode has no tag."""
        child_node = LeafNode("child", "span")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertTrue("All parent nodes need a tag." in str(context.exception))
        
    def test_error_no_children(self):
        """Test error when ParentNode has no children."""
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertTrue("All parent nodes need a child." in str(context.exception))
        
    def test_to_html_nested_props(self):
        """Test ParentNode with nested properties."""
        grandchild = LeafNode("Link text", "a", {"href": "https://example.com"})
        child = ParentNode("li", [grandchild], {"class": "list-item"})
        parent = ParentNode("ul", [child], {"id": "nav-list"})
        self.assertEqual(
            parent.to_html(),
            '<ul id="nav-list"><li class="list-item"><a href="https://example.com">Link text</a></li></ul>'
        )
        
if __name__ == "__main__":
    unittest.main()