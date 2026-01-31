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


