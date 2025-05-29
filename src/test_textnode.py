import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("This is a text node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.google.com")
        self.assertEqual(node1, node2)

    def test_neq_type(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_neq_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node, but better", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_neq_url(self):
        node1 = TextNode("This is a text node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.facebook.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()