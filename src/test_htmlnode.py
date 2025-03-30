import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def setUp(self):
        self.para1 = HTMLNode("p", "This is my first paragraph")
        self.anch1 = HTMLNode(
            "a", "Click me!", None, {"href": "www.cool.thing", "target": "_blank"}
        )

    def test_repr(self):
        self.assertEqual(
            'HTMLNode(tag=p, value="This is my first paragraph", children=None, props=None)',
            repr(self.para1),
        )
