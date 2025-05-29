import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        html = node.props_to_html()
        self.assertEqual(html, " href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_initialization(self):
        # Test with all parameters
        node = HTMLNode(
            tag="div", 
            value="Hello World", 
            children=[HTMLNode(tag="p")], 
            props={"class": "container"}
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.props, {"class": "container"})
        
        # Test with default parameters
        default_node = HTMLNode()
        self.assertIsNone(default_node.tag)
        self.assertIsNone(default_node.value)
        self.assertIsNone(default_node.children)
        self.assertIsNone(default_node.props)
    
    def test_props_to_html_empty(self):
        # Test with empty props
        node = HTMLNode(props={})
        html = node.props_to_html()
        self.assertEqual(html, "")
    
    def test_props_to_html_none(self):
        # Test with None props
        node = HTMLNode()
        with self.assertRaises(AttributeError):
            node.props_to_html()
    
    def test_to_html_not_implemented(self):
        # Test that to_html raises NotImplementedError
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_repr(self):
        # Test the __repr__ method
        node = HTMLNode(
            tag="div", 
            value="content", 
            children=[], 
            props={"class": "container"}
        )
        expected = "HTMLNode(div, content, [], {'class': 'container'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()