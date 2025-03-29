# print('hello world')

from textnode import *

def main():
    first_node = TextNode(
        "This is my sample text", TextType.BOLD, "www.bonski.consulting"
    )

    print(first_node)


main()
