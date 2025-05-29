from textnode import TextType, TextNode

def main() -> None:
    test_node = TextNode("This is some bold text", TextType.BOLD)
    print(test_node)

if __name__=="__main__":
    main()