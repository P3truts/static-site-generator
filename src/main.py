from src.core.generate import Generate
import sys

def main():
    basepath = "/"
    try:
        basepath = sys.argv[1]
    except:
        print("No basepath provided. Defaulted to root '/'!")

    Generate.move_files("static", "docs")
    Generate.generate_pages_recursive("content", "template.html", "docs", basepath)

main()
