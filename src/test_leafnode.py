import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        result = node.to_html()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
