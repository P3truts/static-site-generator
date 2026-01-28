from textnode import TextNode, TextType

def main():
    test = TextNode("test", TextType.PLAIN_TEXT, "http://thisisaurl.com")
    print(test)



main()
