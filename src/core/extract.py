import re

class Extract:

    @staticmethod
    def extract_markdown_images(text):
        patt = r"\!\[(.*?)\]\((.*?)\)"

        res = re.findall(patt, text)

        return res

    @staticmethod
    def extract_markdown_links(text):
        patt = r"\[(.*?)\]\((.*?)\)"

        res = re.findall(patt, text)

        return res

    @staticmethod
    def extract_title(md):
        patt = r"# (.*)"

        res = re.findall(patt, md)

        if not res:
            raise Exception("Title is missing!")

        return res[0]
