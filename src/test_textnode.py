import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.node = TextNode("This is a text node", TextType.BOLD)
        self.node2 = TextNode("This is a text node", TextType.BOLD)

    def test_eq(self):
        self.node = TextNode("This is a text node", TextType.BOLD)
        self.node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(self.node, self.node2)

    def test_eq_text(self):
        self.node.text = ""
        self.assertNotEqual(self.node, self.node2)

        self.node.text = 12
        self.assertNotEqual(self.node, self.node2)
        
        self.node.text = None
        self.assertNotEqual(self.node, self.node2)

    def test_eq_text_type(self):
        self.node.text_type = TextType.LINK
        self.assertNotEqual(self.node, self.node2)

        self.node.text_type = "TextType.LINK"
        self.assertNotEqual(self.node, self.node2)

        self.node.text_type = None
        self.assertNotEqual(self.node, self.node2)

    def test_eq_url(self):
        self.node2.url = "www.somewhere.local"
        self.assertNotEqual(self.node, self.node2)


if __name__ == "__main__":
    unittest.main()
