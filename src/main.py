from src.textnode import TextNode, TextType
from src.core.generate import Generate

def main():
    test = TextNode("test", TextType.PLAIN_TEXT, "http://thisisaurl.com")
    print(test)

    Generate.move_files("static", "public")
    Generate.generate_page("content/index.md", "template.html", "public/index.html")

main()
