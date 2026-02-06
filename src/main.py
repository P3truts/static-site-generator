from src.core.generate import Generate

def main():
    Generate.move_files("static", "public")
    Generate.generate_pages_recursive("content/", "template.html", "public/")

main()
