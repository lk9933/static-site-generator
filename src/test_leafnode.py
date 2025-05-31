import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode(tag="a", value="Click me", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click me</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")
        
    def test_leaf_to_html_with_empty_props(self):
        node = LeafNode(tag="span", value="Some text", props={})
        self.assertEqual(node.to_html(), "<span>Some text</span>")
        
    def test_leaf_to_html_with_special_characters(self):
        node = LeafNode(tag="div", value="Special chars: & < >")
        self.assertEqual(node.to_html(), "<div>Special chars: & < ></div>")
        
    def test_leaf_to_html_no_value_error(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_initialization(self):
        # Test initialization with all parameters
        node = LeafNode(tag="h1", value="Title", props={"class": "header"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Title")
        self.assertEqual(node.props, {"class": "header"})
        
        # Test with default parameters
        default_node = LeafNode(value="Default")
        self.assertIsNone(default_node.tag)
        self.assertEqual(default_node.value, "Default")
        self.assertIsNone(default_node.props)

if __name__ == "__main__":
    unittest.main()