from textnode import TextNode, TextType


def main():
    test_node = TextNode("This is a link", TextType.ANCHOR, "https://www.boot.dev")
    test_node_2 = TextNode("This is _emphasis_", TextType.ITALIC)
    print(test_node)
    print(test_node_2)


main()
