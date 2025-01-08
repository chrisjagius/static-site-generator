import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "http://www.boot.dev", "target": "_blank"})
        result = node.props_to_html()
        expected = 'href="http://www.boot.dev" target="_blank"'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
